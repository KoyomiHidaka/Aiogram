import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN

#from app.handlers import router

bot = Bot(token=TOKEN)
dp = Dispatcher


async def main():
    dp.include_router(router) # type: ignore
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
