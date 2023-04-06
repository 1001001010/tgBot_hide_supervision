from telebot import types

menuUser = types.ReplyKeyboardMarkup(True)
menuUser.add("🔍 Найти сливы!").add("🛍 Мои покупки", "📷 Примеры")
menuSearch = types.InlineKeyboardMarkup(row_width=1)
menuSearch.add(
    types.InlineKeyboardButton(text="ВКонтакте", callback_data="vk"),
    types.InlineKeyboardButton(text="Instagram", callback_data="instagram")
)
menuBack = types.InlineKeyboardMarkup()
menuBack.add(
    types.InlineKeyboardButton(text="Назад", callback_data="social_back")
)
menuBuy = types.InlineKeyboardMarkup(row_width=1)
menuBuy.add(
    types.InlineKeyboardButton('💳 Приобрести архив', callback_data='openMenu'),
    types.InlineKeyboardButton('💳 Купить безлимит', callback_data='openMenu')
)
menuPay = types.InlineKeyboardMarkup()
menuPay.add(
    types.InlineKeyboardButton(text="💳 Оплатить Картой", callback_data="buy_archive")
).add(
    types.InlineKeyboardButton(text="🟣 Оплатить ЮМАНИ", callback_data="buy_archive")
).add(
    types.InlineKeyboardButton(text="Назад", callback_data="social_back")
)
menuAdmin = types.ReplyKeyboardMarkup(True)
menuAdmin.add("Рассылка", "Статистика").add("Рефералы")
menuPhoto = types.ReplyKeyboardMarkup(True)
menuPhoto.add("С фото", "Без фото").add("Отмена")
cancel = types.ReplyKeyboardMarkup(True)
cancel.add("Отмена")
menuCheck = types.InlineKeyboardMarkup()
menuCheck.add(
    types.InlineKeyboardButton(text="⏳ Проверить Оплату", callback_data="checkPay")
)
