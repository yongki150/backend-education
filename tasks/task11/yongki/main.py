import json
import string
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


async def send_success_msg(result):
    resp = {"status": "success", "message": str(result.data)}
    return web.Response(text=json.dumps(resp, ensure_ascii=False), status=200)


async def send_failed_msg(msg, status):
    resp = {"status": "failed", "message": msg}
    return web.Response(text=json.dumps(resp), status=status)


@routes.post('/login')
async def handle_login(request):
    try:
        alphabet = string.ascii_letters + string.digits
        key = ''.join(secrets.choice(alphabet) for i in range(8))

        while key in INFO:
            key = ''.join(secrets.choice(alphabet) for i in range(8))

        data = await request.json()
        resp_login = await IntranetAPI.Login.fetch(data["id"], data["passwd"])

        if resp_login.reason != "Found":
            resp = {"status": "failed", "message": "incorrect login data" }
            return web.Response(text=json.dumps(resp), status=400)

        result = IntranetAPI.Login.parse(resp_login)
        INFO[key] = result.data["cookies"]
        # print(INFO)

        resp = {"status": "success", "message": f"welcome! your enter key is {key}"}
        return web.Response(text=json.dumps(resp), status=200)

    except KeyError:
        return send_failed_msg("incorrect key", 400)

    except json.decoder.JSONDecodeError:
        return send_failed_msg("incorrect json format", 400)


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
        print(result)

        return await send_success_msg(result)
    else:
        return await send_failed_msg("login first", 401)


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
        print(result)

        return await send_success_msg(result)
    else:
        return await send_failed_msg("login first", 401)


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
        print(result)

        return await send_success_msg(result)
    else:
        return await send_failed_msg("login first", 401)


@routes.get('/{wrong_path}')
async def handle_wrong_path(request):
    return web.Response(text="{} is wrong path".format(request.match_info['wrong_path']), status=404)

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    print(server["message"])
    web.run_app(app, port=server["port"], host=server["host"])