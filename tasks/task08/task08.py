from aiohttp import web
import json

routes = web.RouteTableDef()


def __init__():
    app = web.Application()
    app.add_routes(routes)
    return app


def main():
    app = __init__()
    web.run_app(app)


@routes.get("/sum")
async def sum_(request):  # handler
    print(request)
    try:
        result = 0
        key_data_query = request.query.values()
        # (a,b,c...)가 주어지지 않았을 때,
        if len(key_data_query) == 0:
            raise ValueError
        for key in request.query.values():
            # key 값 중 숫자가 아닌 수가 있을 경우
            if key.isdigit() is not True:
                raise TypeError
            result += int(key)
        response_obj = {"status": "success", "result": result}
        return web.Response(text=json.dumps(response_obj), status=200)
    except TypeError:
        response_obj = {"status": "failed", "message": "Input only integer"}
        return web.Response(text=json.dumps(response_obj), status=400)
    except ValueError:
        response_obj = {"status": "failed", "message": "Input sum data"}
        return web.Response(text=json.dumps(response_obj), status=400)


@routes.get("/{name}", name="sum")
async def wrong_path_error(request):
    return web.Response(text="wrong path! 404 error! {}".format(request.match_info["name"]))


if __name__ == "__main__":
    main()
