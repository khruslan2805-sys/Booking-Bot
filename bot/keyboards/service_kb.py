from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

service_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💻 Разработка", callback_data="service_dev")],
        [InlineKeyboardButton(text="📈 Маркетинг", callback_data="service_marketing")],
        [InlineKeyboardButton(text="🎨 Дизайн", callback_data="service_design")],
    ]
)
