from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/sysinfo')
async def sysinfo():
    return os.system('cat /proc/cpuinfo')