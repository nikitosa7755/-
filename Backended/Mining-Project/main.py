from fastapi import FastAPI
from router import router as consts_router

app = FastAPI()
app.include_router(consts_router)
