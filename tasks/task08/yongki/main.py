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
    data = request.query
    query_sum = sum(int(val) for key, val in data.items())

    if query_sum == 0:
        print("입력이 필요합니다.")
        response_obj = {"stats": "failed", "message": "need input"}
    else:
        response_obj = {"status": "success", "result": query_sum}
    return web.Response(text=json.dumps(response_obj), status=200)


app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    print(server["message"])
    web.run_app(app, port=server["port"], host=server["host"])
