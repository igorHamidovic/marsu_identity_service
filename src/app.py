import logging
import time
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.common.exceptions import APIException
from src.identity.endpoints import router as identity_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Middleware to log all incoming requests and outgoing responses.
    """
    # Log request
    logger.info(f"Request: {request.method} {request.url.path}")
    logger.info(f"Request headers: {dict(request.headers)}")
    
    # Get request body if present
    if request.method in ["POST", "PUT", "PATCH"]:
        body = await request.body()
        if body:
            logger.info(f"Request body: {body.decode('utf-8')}")
    
    # Process request and measure time
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    # Log response
    logger.info(f"Response: {response.status_code} (processed in {process_time:.3f}s)")
    
    # Get and log response body
    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk
    
    logger.info(f"Response body: {response_body.decode('utf-8')}")
    
    # Create new response with the body we just read
    from fastapi.responses import Response
    return Response(
        content=response_body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )

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
