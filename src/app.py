import uvicorn

from common import load_args
from apirest import app


if __name__ == "__main__":
    args = load_args()

    uvicorn.run(
        app,
        host=args['host'],
        port=args['port']
    )
