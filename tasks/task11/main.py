import json

from aiohttp import web
from biblebot import IntranetAPI

server = {
    "host": "localhost",
    "port": 8080,
    "message": "server on 8080 port"
}

INFO = {
    "cookie": "",
}

routes = web.RouteTableDef()


@routes.post('/login')
async def handle_login(request):
    try:
        data = await request.json()
        resp_login = await IntranetAPI.Login.fetch(data["id"], data["passwd"])

        if resp_login.reason != "Found":
            resp = {"status": "failed", "message": "incorrect login data" }
            return web.Response(text=json.dumps(resp), status=400)

        result = IntranetAPI.Login.parse(resp_login)
        INFO["cookie"] = result.data["cookies"]

        resp = {"status": "success", "message": "welcome!"}
        return web.Response(text=json.dumps(resp), status=200)

    except KeyError:
        resp = {"status": "failed", "message": "incorrect key"}
        return web.Response(text=json.dumps(resp), status=400)
    except json.decoder.JSONDecodeError:
        resp = {"stats": "failed", "message": "incorrect json format"}
        return web.Response(text=json.dumps(resp), status=400)


@routes.post('/chapel')
async def handle_chapel(request):
    data = await request.json()

    if INFO["cookie"] == "":
        resp = {"status": "failed", "message": "login first"}
        return web.Response(text=json.dumps(resp), status=401)

    resp_chapel = await IntranetAPI.Chapel.fetch(
        cookies=INFO["cookie"],
        semester=data["semester"]
    )
    result = IntranetAPI.Chapel.parse(resp_chapel)
    print(result)

    resp = {"status": "success", "message": str(result.data)}
    return web.Response(text=json.dumps(resp, ensure_ascii=False), status=200)


@routes.post('/timetable')
async def handle_chapel(request):
    data = await request.json()

    if INFO["cookie"] == "":
        resp = {"status": "failed", "message": "login first"}
        return web.Response(text=json.dumps(resp), status=401)

    resp_chapel = await IntranetAPI.Timetable.fetch(
        cookies=INFO["cookie"],
        semester=data["semester"]
    )
    result = IntranetAPI.Timetable.parse(resp_chapel)
    print(result)

    resp = {"status": "success", "message": str(result.data)}
    return web.Response(text=json.dumps(resp, ensure_ascii=False), status=200)


@routes.post('/course')
async def handle_chapel(request):
    data = await request.json()

    if INFO["cookie"] == "":
        resp = {"status": "failed", "message": "login first"}
        return web.Response(text=json.dumps(resp), status=401)

    resp_chapel = await IntranetAPI.Course.fetch(
        cookies=INFO["cookie"],
        semester=data["semester"]
    )
    result = IntranetAPI.Course.parse(resp_chapel)
    print(result)

    resp = {"status": "success", "message": str(result.data)}
    return web.Response(text=json.dumps(resp, ensure_ascii=False), status=200)


@routes.get('/{wrong_path}')
async def handle_wrong_path(request):
    return web.Response(text="{} is wrong path".format(request.match_info['wrong_path']), status=404)

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    print(server["message"])
    web.run_app(app, port=server["port"], host=server["host"])