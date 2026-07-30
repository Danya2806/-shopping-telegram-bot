from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())

async def start_command(message: Message):

    await message.answer(

        "Привет! 👋\n\n"

        "Я помогу вести список покупок.",

        reply_markup=main_menu,

    )