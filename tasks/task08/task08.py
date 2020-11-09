import asyncio
from aiohttp import web
import json

routes = web.RouteTableDef()


def __init__(loop):
    app = web.Application(loop=loop)
    app.add_routes(routes)
    return app


def main():
    loop = asyncio.get_event_loop()
    app = __init__(loop)
    web.run_app(app)


@routes.get("/sum")
async def sum_(request):  # handler
    print(request)
    try:
        result = 0
        keydatas = request.query.values()
        # (a,b,c...)가 주어지지 않았을 때,
        if len(keydatas) == 0:
            raise ValueError
        for key in request.query.values():
            # key값 중 숫자가 아닌 수가 있을 경우
            if key.isdigit() != True:
                raise TypeError
            result += int(key)
        response_obj = {"result": result}
        return web.Response(text=json.dumps(response_obj), status=200)
    except TypeError:
        response_obj = {"status": "failed", "message": "Input only integer"}
        return web.Response(text=json.dumps(response_obj), status=500)
    except ValueError:
        response_obj = {"status": "failed", "message": "Input sum data"}
        return web.Response(text=json.dumps(response_obj), status=500)


@routes.get("/{name}", name="sum")
async def Wrong_path_error(request):
    return web.Response(text="wrong path! {}".format(request.match_info["name"]))


if __name__ == "__main__":
    main()
