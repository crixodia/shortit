from fastapi import FastAPI
from fastapi import Path

app = FastAPI(
    title="URL Shortener API",
    description="A simple URL shortner API",
    version="0.0.1"
)


@app.post("/{url}")
def short_url(url: str):
    pass


@app.get("/{url}")
def get_url():
    pass


@app.put("/{url}")
def update_url():
    pass


@app.delete("/{url}")
def delete_url():
    pass
