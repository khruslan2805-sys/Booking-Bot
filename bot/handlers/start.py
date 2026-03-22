from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.states.lead_state import LeadState

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await state.set_state(LeadState.name)

    await message.answer("👋 Привет!\n\nВведите ваше имя:")
         