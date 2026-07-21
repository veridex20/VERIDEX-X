from fastapi import FastAPI

app = FastAPI(
    title="VERIDEX X",
    description="Nature Intelligence Operating System",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "name": "VERIDEX X",
        "status": "ONLINE",
        "mode": "Development",
        "message": "Observation Engine coming next."
    }
