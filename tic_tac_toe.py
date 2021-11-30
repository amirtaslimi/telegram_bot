from pyrogram import Client
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, \
    InlineQuery, InlineQueryResultArticle, InputTextMessageContent
api_id = 3980855
api_hash = '74c285c81af4920c00fedbd427766a9c'
client = Client(session_name='mybot' ,
    bot_token='1624312397:AAG9Ad01NBwjg5BWZKgVp94BsO_ONtIe7Rk', api_id = api_id , api_hash = api_hash)
data = [[['-', '1'] , ['-', '2'] ,['-', '3']] , [['-', '4'] , ['-', '5'] ,['-', '6']] , [['-', '7'] , ['-', '8'] ,['-', '9']]]
def IKM(data):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd)] for text, cbd in data])

IKM9 = InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)])


lst = ['-','-','-','-','-','-','-','-','-']

def chek(data):
    if (data[0][0][0] == 'X' and data[0][0][0] == data[0][1][0] and data[0][1][0] == data[0][2][0]) or (data[1][0][0] == 'X' and data[1][0][0] == data[1][1][0] and data[1][1][0] == data[1][2][0]) or (data[2][0][0] == 'X' and data[2][0][0] == data[2][1][0] and data[2][1][0] == data[2][2][0]):
        return True


@client.on_callback_query()
def handle_callback_query(bot: Client, query: CallbackQuery):
    if query.data == 'start':
        bot.edit_inline_text(query.inline_message_id, 'بازی', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)]))
    elif query.data == '1':
        data[0][0][0] = 'X'
        bot.edit_inline_text(query.inline_message_id, 'بازی', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)]))
    elif query.data == '2':
        data[0][1][0] = 'X'
        bot.edit_inline_text(query.inline_message_id, 'بازی', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)]))
    elif query.data == '3':
        data[0][2][0] = 'X'
        bot.edit_inline_text(query.inline_message_id, 'بازی', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)]))
    elif query.data == '4':
        data[1][0][0] = 'X'
        bot.edit_inline_text(query.inline_message_id, 'بازی', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)]))
    elif query.data == '5':
        data[1][1][0] = 'X'
        bot.edit_inline_text(query.inline_message_id, 'بازی', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)]))
    elif query.data == '6':
        data[1][2][0] = 'X'
        bot.edit_inline_text(query.inline_message_id, 'بازی', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)]))
    elif query.data == '7':
        data[2][0][0] = 'X'
        bot.edit_inline_text(query.inline_message_id, 'بازی', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)]))
    elif query.data == '8':
        data[2][1][0] = 'X'
        bot.edit_inline_text(query.inline_message_id, 'بازی', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)]))
    elif query.data == '9':
        data[2][2][0] = 'X'
        bot.edit_inline_text(query.inline_message_id, 'بازی', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(data[i][0][0], data[i][0][1]) ,InlineKeyboardButton(data[i][1][0], data[i][1][1]) ,InlineKeyboardButton(data[i][2][0], data[i][2][1])]for i in range(3)]))
    elif query.data == 'end':
        bot.edit_inline_text(query.inline_message_id, 'بازی تمام شد!!')
    if chek(data) == True:
        bot.edit_inline_text(query.inline_message_id, 'بازی به اتمام رسید شخص X برنده شد', reply_markup=IKM([('خدا نگهدار', 'end')]))
    elif query.data == 'end':
        bot.edit_inline_text(query.inline_message_id, 'بازی تمام شد!!')
    elif query.data == 'wrong':
        bot.edit_inline_text(query.inline_message_id, 'حرکت اشتباه است', reply_markup=IKM([('بازگشت به بازی', 'start')]))



@client.on_inline_query()
def handle_inline_query(bot: Client, query: InlineQuery):
    if not query.query:
        return
    results = [InlineQueryResultArticle('شروع بازی جدید', InputTextMessageContent('بازی تیک تاک'),
                                        reply_markup=IKM([('قبول بازی!', 'start')]))]
    bot.answer_inline_query(query.id, results)


client.run()