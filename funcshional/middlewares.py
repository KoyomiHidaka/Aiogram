from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from aiogram.types import TelegramObject








class TestMiddleware(BaseMiddleware):
    async def __call__(self, handler:Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]) -> Any:
        print("Actions before h")
        result = await handler(event, data)
        print("Action after h")
        return result