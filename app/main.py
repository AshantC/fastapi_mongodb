from fastapi import FastAPI
from router.route import router


app = FastAPI()


app.include_router(router)