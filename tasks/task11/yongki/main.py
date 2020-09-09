import secrets

from aiohttp import web
from biblebot import IntranetAPI

server = {
    "host": "localhost",
    "port": 8080,
    "message": "server on 8080 port"
}

INFO = {}

routes = web.RouteTableDef()


@web.middleware
async def error_middleware(request, handler) -> web.StreamResponse:
    try:
        response = await handler(request)

        if response.status == 200:
            return response

    except web.HTTPException as ex:
        return web.json_response({"status": "failed", "reason": ex.reason, "status_code": ex.status_code})


@routes.post('/login')
async def handle_login(request):
    key = secrets.token_urlsafe(16)

    while key in INFO:
        key = secrets.token_urlsafe(16)

    data = await request.json()
    resp_login = await IntranetAPI.Login.fetch(data["id"], data["passwd"])

    if resp_login.reason != "Found":
        raise web.HTTPBadRequest

    result = IntranetAPI.Login.parse(resp_login)
    INFO[key] = result.data["cookies"]

    data_msg = f"welcome! your enter key is {key}"
    return web.json_response({"status": "success", "message": data_msg})


@routes.get('/chapel')
async def handle_chapel(request):
    data = request.query
    enter_key = data["key"]

    if enter_key in INFO:
        resp_chapel = await IntranetAPI.Chapel.fetch(
            cookies=INFO[enter_key],
            semester=data["semester"]
        )
        result = IntranetAPI.Chapel.parse(resp_chapel)

        return web.json_response({"status": "success", "message": result.data})
    else:
        raise web.HTTPUnauthorized


@routes.get('/timetable')
async def handle_timetable(request):
    data = request.query
    enter_key = data["key"]

    if enter_key in INFO:
        resp_chapel = await IntranetAPI.Timetable.fetch(
            cookies=INFO[enter_key],
            semester=data["semester"]
        )
        result = IntranetAPI.Timetable.parse(resp_chapel)

        return web.json_response({"status": "success", "message": result.data})
    else:
        raise web.HTTPUnauthorized


@routes.get('/course')
async def handle_course(request):
    data = request.query
    enter_key = data["key"]

    if enter_key in INFO:
        resp_chapel = await IntranetAPI.Course.fetch(
            cookies=INFO[enter_key],
            semester=data["semester"]
        )
        result = IntranetAPI.Course.parse(resp_chapel)

        return web.json_response({"status": "success", "message": result.data})
    else:
        raise web.HTTPUnauthorized

app = web.Application(middlewares=[error_middleware])
app.add_routes(routes)

if __name__ == '__main__':
    print(server["message"])
    web.run_app(app, port=server["port"], host=server["host"])