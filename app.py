from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/sysinfo')
async def sysinfo():
    return subprocess.check_output(['cat', '/proc/cpuinfo'])