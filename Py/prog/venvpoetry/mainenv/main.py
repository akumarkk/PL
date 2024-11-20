import asyncio, logging
logger = logging.getLogger()


async def main():
    logging.basicConfig(level=logging.INFO)
    logger.info("hello!")
    await asyncio.sleep(1)
    logger.info("bye")

asyncio.run(main())
