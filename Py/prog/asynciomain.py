import asyncio
import logging
logger = logging.getLogger(__name__)

async def sum(num):
    return num *(num+1)/2

async def square(num):
    return num*num

async def main():
    
    logging.basicConfig(level=logging.INFO)
    ret = await asyncio.gather(sum(10), square(10))
    logger.info(ret)

asyncio.run(main())


