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
        response_obj = {}
        if not data:
            print("입력이 필요합니다.")
            response_obj = {"stats": "failed", "message": "need input"}

            return web.Response(text=json.dumps(response_obj), status=404)

        else:
            query_sum = 0
            for key, val in data.items():
                if val.isalpha():
                    response_obj = {"status": "failed", "message": "type is not int"}
                    return web.Response(text=json.dumps(response_obj), status=500)

                elif val.isdecimal():
                    query_sum += int(val)
                    response_obj = {"status": "success", "result": query_sum}

            return web.Response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        print("message: " + str(e))

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    print(server["message"])
    web.run_app(app, port=server["port"], host=server["host"])
