from starlette.applications import Starlette
from starlette.routing import Mount
from mcpserver import mcp
import common

if __name__ == "__main__":
    args = common.load_args()

    if args['transport'] == 'stdio':
        mcp.run()
    else:
        import uvicorn
        mcp_app = mcp.http_app(path='/')
        routes = [Mount("/", app=mcp_app)]
        uvicorn.run(
            app=Starlette(routes=routes, lifespan=mcp_app.lifespan),
            host=args['host'],
            port=args['port']
        )
