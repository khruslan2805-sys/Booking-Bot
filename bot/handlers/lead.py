from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from bot.states.lead_state import LeadState
from bot.keyboards.phone_kb import phone_keyboard
from bot.keyboards.service_kb import service_keyboard
from bot.config import ADMIN_ID

router = Router()

service_names = {
    "dev": "💻 Разработка",
    "marketing": "📈 Маркетинг",
    "design": "🎨 Дизайн"
}


# 1️⃣ Имя
@router.message(LeadState.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(LeadState.phone)

    await message.answer(
        "📞 Отправьте номер телефона:",
        reply_markup=phone_keyboard
    )


# 2️⃣ Телефон (контакт)
@router.message(LeadState.phone, F.contact)
async def get_phone_contact(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    await process_phone(message, state, phone)


# 2️⃣ Телефон (текст)
@router.message(LeadState.phone)
async def get_phone_text(message: Message, state: FSMContext):
    phone = message.text
    await process_phone(message, state, phone)


# обработка телефона
async def process_phone(message: Message, state: FSMContext, phone: str):
    await state.update_data(phone=phone)
    await state.set_state(LeadState.service)

    await message.answer(
        "Выберите услугу:",
        reply_markup=service_keyboard
    )


# 3️⃣ Услуга
@router.callback_query(LeadState.service, F.data.startswith("service"))
async def choose_service(callback: CallbackQuery, state: FSMContext):
    service = callback.data.split("_")[1]

    await state.update_data(service=service)

    data = await state.get_data()

    text = (
        "🔥 Новая заявка\n\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {data['phone']}\n"
        f"Услуга: {service_names.get(service)}"
    )

    await callback.message.bot.send_message(ADMIN_ID, text)

    await callback.message.answer(
        "✅ Спасибо! Мы скоро свяжемся с вами.",
        reply_markup=ReplyKeyboardRemove()
    )

    await state.clear()
    await callback.answer()
     