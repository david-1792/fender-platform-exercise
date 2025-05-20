from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.core.db import ModelBase
from app.core.config import settings
from app.api.main import router as api_router

logger = logging.getLogger('uvicorn')

app_config: dict = {
    'title': 'Fender Engineering Challenge 🎸 - Auth API 🔐',
    'description': 'A simple authentication and user management API. \
        Made by [David Jiménez Rodríguez](https://linkedin.com/in/david-jr1792) as part of the recruitment process for the **Software Engineer** role at Fender.',
    'version': '0.1.0'
}

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Starting the API...')

    # Make sure the DynamoDB table exists
    if not ModelBase.exists():
        logger.info('Creating the DynamoDB table...')
        ModelBase.create_table(wait=True, billing_mode='PAY_PER_REQUEST')
        logger.info('Successfully created the DynamoDB table')

    yield
    logger.info('Stopping the API...')

app_config['lifespan'] = lifespan

app = FastAPI(**app_config)

@app.get('/health')
def health():
    return JSONResponse({'status': 'OK'})

app.include_router(api_router, prefix=settings.API_PREFIX)