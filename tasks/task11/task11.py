import json

import asyncio
from aiohttp import web
from biblebot import IntranetAPI

routers = web.RouteTableDef()
data = {}


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
    for key, val in req.query.items():
        user_data[key] = val
    resp = await IntranetAPI.Login.fetch(user_data['id'], user_data['pw'])
    result = IntranetAPI.Login.parse(resp)
    try:
        data['cookie'] = result.data['cookies']
    except AttributeError:
        raise
    return web.Response(text="login_success: " + str(data))


@routers.get('/chapel')
async def get_chapel(req):
    if len(data) != 0:
        try:
            resp = await IntranetAPI.Chapel.fetch(cookies=data.get('cookie'), semester="20201")
            result = IntranetAPI.Chapel.parse(resp)
            return web.Response(text=json.dumps(result.data), status=400)
        except web.HTTPForbidden:
            raise
    raise AttributeError


@routers.get('/timetable')
async def get_timetable(req):
    if len(data) != 0:
        try:
            resp = await IntranetAPI.Timetable.fetch(cookies=data.get('cookie'), semester="20201")
            result = IntranetAPI.Timetable.parse(resp)
            return web.Response(text=json.dumps(result.data), status=400)
        except web.HTTPForbidden:
            raise


@routers.get('/course')
async def get_course(req):
    if len(data) != 0:
        try:
            resp = await IntranetAPI.Course.fetch(cookies=data.get('cookie'), semester="20201")
            result = IntranetAPI.Course.parse(resp)
            return web.Response(text=json.dumps(result.data), status=400)
        except web.HTTPForbidden:
            raise

        
if __name__ == "__main__":
    main()
