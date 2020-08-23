import json

from aiohttp import web

server = {
    "host": "localhost",
    "port": 8080,
    "message": "server on 8080 port"
}
routes = web.RouteTableDef()


@routes.get('/sum')
async def handle(request):
    try:
        data = request.query

        if not data:
            response_obj = {"stats": "failed", "message": "need input"}
            return web.Response(text=json.dumps(response_obj), status=400)

        else:
            query_sum = 0
            for val in data.values():
                if float(val):
                    query_sum += float(val)

            response_obj = {"status": "success", "result": query_sum}
            return web.Response(text=json.dumps(response_obj), status=200)

    except ValueError as e:  # 영문, 한글, 특수문자에 대한 처리
        response_obj = {"status": "failed", "message(ValueError)": "please input number"}
        return web.Response(text=json.dumps(response_obj), status=400)
    except Exception:
        print("message: unexpected error, contact admin")


@routes.get('/{wrong_path}', name="sum")
async def handle_wrong_path(request):
    return web.Response(text="{} is wrong path".format(request.match_info['wrong_path']), status=404)

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    print(server["message"])
    web.run_app(app, port=server["port"], host=server["host"])
