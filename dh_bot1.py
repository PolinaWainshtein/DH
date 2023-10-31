import telebot
from telebot import types


title = "@vegan_meall_bot"
your_bot = "6974488548:AAETaUWM7HAAd460oaS4xhybRHBoibwPUkQ"
bot = telebot.TeleBot(your_bot)

@bot.message_handler(commands=["start"])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True) 
    item1=types.KeyboardButton("Идеи основных блюд") 
    item2=types.KeyboardButton("Идеи перекусов")
    item3=types.KeyboardButton("Идеи дессертов")
    item4=types.KeyboardButton("Где посмотреть другие рецепты?")
    markup.row(item1) 
    markup.row(item3, item4)
    markup.row(item2)
    bot.send_message(message.chat.id, 'Приветствуем! Вы задались вопросом, что поесть веганского? Этот бот поможет с выбором.' , reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Идеи основных блюд':
        meal1 = "Паста с томатным соусом и овощами"
        meal2 = "Тако с нутом, овощами и соусом"
        meal3 = "Боул с киноа, бататом и брокколи"
        bot.send_message(message.chat.id, meal1)
        bot.send_message(message.chat.id, meal2)
        bot.send_message(message.chat.id, meal3)
    elif message.text.strip() == 'Идеи перекусов':
        snack1 = "Смузи из банана, ягод и арахисовой пасты"
        snack2 = "Хумус с морковными палочками и сельдереем"
        snack3= "Мятый авокадо с соевым соусом и крекерами"
        bot.send_message(message.chat.id, snack1)
        bot.send_message(message.chat.id, snack2)
        bot.send_message(message.chat.id, snack3)
    elif message.text.strip() == "Идеи дессертов":
        dessert1 = "Хлеб из банана с изюмом и клюквой"
        dessert2 = "Тыквенный пирог с апельсиновой глазурью"
        dessert3 = "Печенье орео с порезанными фруктами"
        bot.send_message(message.chat.id, dessert1)
        bot.send_message(message.chat.id, dessert2)
        bot.send_message(message.chat.id, dessert3)
    elif message.text.strip() == "Где посмотреть другие рецепты?":
        text = "Больше сотни рецептов веганской еды можно найти тут: https://www.bbcgoodfood.com/recipes/collection/vegan-recipes"
        bot.send_message(message.chat.id, text)
    else:
        text1 = "Пожалуйста, выберите ответ из предложенных"
        bot.send_message(message.chat.id, text1)

bot.polling(none_stop=True, interval=0)


