import json

import secrets
from aiohttp import web
from biblebot import IntranetAPI

routers = web.RouteTableDef()
data = dict()


def __init__():
    app = web.Application(middlewares=[error_middleware])
    app.add_routes(routers)
    return app


def main():
    app = __init__()
    web.run_app(app)


@web.middleware
async def error_middleware(req, handler):
    try:
        resp = await handler(req)
        if resp.status != 404:
            return resp
        message = resp.text
    except AttributeError:
        message = "로그인을 다시 시도해주세요."
    except web.HTTPForbidden:
        message = "로그인을 우선 해주세요."
    except web.HTTPNotFound:
        message = "페이지를 찾을 수 없습니다."
    return web.json_response({'error': message})


@routers.post('/login')
async def post_login(req):
    user_data = {'id': None, 'pw': None}
    user_secrets_url = secrets.token_urlsafe(32)

    for key, val in req.query.items():
        user_data[key] = val
    resp = await IntranetAPI.Login.fetch(user_data['id'], user_data['pw'])
    result = IntranetAPI.Login.parse(resp)
    try:
        data[user_secrets_url] = result.data['cookies']
    except AttributeError:
        raise
    return web.Response(text= user_secrets_url)


@routers.get('/chapel')
async def get_chapel(req):
    if data[req.query_string] is not None:
        try:
            resp = await IntranetAPI.Chapel.fetch(cookies=data[req.query_string], semester="20201")
            result = IntranetAPI.Chapel.parse(resp)
            print(result)
            return web.Response(text=json.dumps(result.data), status=400)
        except web.HTTPForbidden:
            raise
    raise AttributeError


@routers.get('/timetable')
async def get_timetable(req):
    if data[req.query_string] is not None:
        try:
            resp = await IntranetAPI.Timetable.fetch(cookies=data[req.query_string], semester="20201")
            result = IntranetAPI.Timetable.parse(resp)
            return web.Response(text=json.dumps(result.data), status=400)
        except web.HTTPForbidden:
            raise


@routers.get('/course')
async def get_course(req):
    if data[req.query_string] is not None:
        try:
            resp = await IntranetAPI.Course.fetch(cookies=data[req.query_string], semester="20201")
            result = IntranetAPI.Course.parse(resp)
            return web.Response(text=json.dumps(result.data), status=400)
        except web.HTTPForbidden:
            raise

        
if __name__ == "__main__":
    main()
