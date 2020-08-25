from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/sum')
async def handler(request):
    try:
        num = request.query

        if num:
            result = 0
            for value in num.values():
                result += float(value)

            return web.Response(text=f"결과: {result}", status=200)

        else:
            return web.Response(text="Please add a Variable.", status=400)

    except ValueError:
        return web.Response(text="Bad Request\n"
                                 "Server unable to understand request due to incorrect grammar.", status=400)

    except Exception:
        print("There was an unexpected error in the processing you requested.")


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8080, host="localhost")
