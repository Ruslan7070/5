from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Дальше", callback_data="next_button_2")
    markup.add(button)
    quiestion = "Что такое PYTHON?"
    answers = [
        "Змея",
        "Игрушка",
        "Язык програмирования",
        "Новый сленг",
        "Школа программированния",
        "Межгалактическая планета"
    ]
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="ТЫ ТУПОЙ ЧТОЛИ!",
        open_period=10,
        reply_markup=markup
    )


async def quiz_3(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Дальше", callback_data="next_button_3")
    markup.add(button)
    quiestion = "Как должен выглядеть современный программист?"
    answers = [
        "Это неприметная девушка",
        "это парень в очках",
        "Это замученный парень с рюкзаком ",
        "ЭТо привлекательная девушка",
        "Совершенно без разницы им может быть любой чел",
        "ничего из перечисленного"
    ]
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="ТЫ ТУПОЙ ЧТОЛИ!",
        open_period=10,
        reply_markup=markup
    )

async def quiz_4 (callback: types.CallbackQuery):
    await callback.message.answer("На этом все!")


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")
    dp.register_callback_query_handler(quiz_4, text = "next_button_3")

