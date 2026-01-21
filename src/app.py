import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.common.exceptions import APIException
from src.identity.endpoints import router as identity_router


app = FastAPI()

@app.exception_handler(APIException)
async def api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.error_response.model_dump(by_alias=True)
    )

app.include_router(identity_router)

@app.get("/", tags=["maintenance"])
@app.get("/health", tags=["maintenance"])
async def health():
    """
    Health check endpoint.
    """
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
