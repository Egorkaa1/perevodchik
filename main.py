
import telebot
from config import token
# Задание 7 - испортируй команду defaultdict
from logic import quiz_questions
from collections import defaultdict

user_responses = {} 
# Задание 8 - создай словарь points для сохранения количества очков пользователя
points = defaultdict(int)
bot = telebot.TeleBot(token)

points['a'] += 1
print(points['a'])

points_list = defaultdict(list)


def send_question(chat_id):
    bot.send_message(chat_id, quiz_questions[user_responses[chat_id]].text, reply_markup=quiz_questions[user_responses[chat_id]].gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "correct":
        bot.answer_callback_query(call.id, "Answer is correct")
        # Задание 9 - добавь очки пользователю за правильный ответ
        points[chat_id] += 1
    elif call.data == "wrong":
        bot.answer_callback_query(call.id,  "Answer is wrong")
      
    # Задание 5 - реализуй счетчик вопросов
        user_responses[call.message.chat.id]+=1
    # Задание 6 - отправь пользователю сообщение с количеством его набранных очков, если он ответил на все вопросы, а иначе отправь следующий вопрос
    if user_responses[call.message.chat.id]>=len(quiz_questions):
        bot.send_message(call.message.chat.id, "The end")
    else:
        send_question(call.message.chat.id)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')
    global count
    global page
		#Обработка кнопки - скрыть
    if req[0] == 'unseen':
        bot.delete_message(call.message.chat.id, call.message.message_id)

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in user_responses.keys():
        user_responses[message.chat.id] = 0
        send_question(message.chat.id)


bot.infinity_polling()
