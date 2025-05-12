# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 挂载 static 目录用于托管 HTML、JS、CSS 等静态资源
app.mount("/static", StaticFiles(directory="./../static"), name="static")

# 允许所有源访问（开发阶段用，生产环境应限制来源）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或改为 ["http://127.0.0.1:5500"] 等你HTML页面实际来源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return RedirectResponse(url="/static/index.html")

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)