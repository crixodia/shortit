from fastapi import FastAPI
from fastapi import Path
from routers import url


app = FastAPI(
    title="URL Shortener API",
    description="A simple URL shortner API",
    version="0.0.1"
)

app.include_router(url.router)
