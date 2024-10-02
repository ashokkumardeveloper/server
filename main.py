from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes.translate_routes import router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    print("Starting up...")
    yield
    # Code to run on shutdown
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

app.include_router(router=router,tags=["translate"])
