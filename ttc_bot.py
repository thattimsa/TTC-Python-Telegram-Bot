import telebot
import requests

bot_token = 'YOUR_BOT_TOKEN'
api_key = 'c0a2f304-551a-4d08-b8df-2c53ecd57f9f'
lang = 'ka'

bot = telebot.TeleBot(bot_token)

def make_request(url, headers=None):
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "სალამი! ✨ მომწერე გაჩერების ნომერი და ავტობუსებისა და სამარშრუტო ტაქსების მოსვლის დროს გეტყვი. 🚀")

@bot.message_handler(func=lambda message: True)
def get_arrival_times(message):
    try:
        stop_no = message.text.strip()
        if not stop_no.isdigit():
            raise ValueError("გაჩერების არავალიდური ნომერი 🤔")
    except ValueError:
        bot.send_message(message.chat.id, "მომწერე გაჩერების ვალუდური ნომერი 🫡")
        return
    
    stop_info_url = f'https://transit.ttc.com.ge/pis-gateway/api/v2/stops/1:{stop_no}?locale={lang}'
    headers = {'X-Api-Key': api_key}
    stop_info = make_request(stop_info_url, headers)
    if stop_info:
        stop_name = stop_info['name']
        arrival_url = f'https://transit.ttc.com.ge/pis-gateway/api/v2/stops/1:{stop_no}/arrival-times?locale={lang}&ignoreScheduledArrivalTimes=false'
        arrival_data = make_request(arrival_url, headers)
        if arrival_data:
            response_text = f"გაჩერება #{stop_no} - {stop_name}\n\n"
            for arrival in arrival_data:
                emoji = "🟢" if arrival['color'] == '00B38B' else "🔵" if arrival['color'] == '0033B4' else "🌕"
                response_text += f"{emoji} {arrival['shortName']} - {arrival['headsign']}\n"
                response_text += f"🕐 {arrival['realtimeArrivalMinutes']} წუთი\n"
                response_text += "\n"
            bot.send_message(message.chat.id, response_text)
        else:
            bot.send_message(message.chat.id, "ინფორმაცია ვერ მოიძებნა")
    else:
        bot.send_message(message.chat.id, "გაჩერება ვერ მოიძებნა")

bot.polling()