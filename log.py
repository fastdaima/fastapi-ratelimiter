
from fastapi import FastAPI, Request

from fastapi import APIRouter 

router = APIRouter()

import logging 

logger = logging.getLogger(__name__)

@router.get('/root')
async def root(request: Request): 
    logger.info(' I am here ')
    return "Hello World" 


app = FastAPI() 


app.include_router(router, prefix='/api/v1') 



