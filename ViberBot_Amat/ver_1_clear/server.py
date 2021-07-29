from flask import Flask, request, Response
from viberbot import Api
from viberbot.api import messages, viber_requests
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

import time
import logging
import sched
import threading

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)

viber = Api(BotConfiguration(
  name='ST Amator',
  avatar='http://viber.com/avatar.jpg',
  auth_token='4daa90c76a27d2bd-da20e99cc428dc26-491a88d6cd292369'
))

@app.route('/', methods=['POST'])
def incoming():
    logger.debug("Получил запрос. Отправка данных: {0}".format(request.get_data()))
    
    viber_request = viber.parse_request(request.get_data())
    viber_request = viber.parse_request(request.get_data().decode('utf8'))
        

    if isinstance(viber_request, ViberMessageRequest):
        message_vmr = viber_request.message
        viber.send_messages(viber_request.sender.id, [message_vmr])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ТЕКСТОВОЕ СООБЩЕНИЕ *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        
    elif isinstance(viber_request, ViberConversationStartedRequest):
        message_vcsr='''Рады приветствовать Вас, {0}!
         Вы вошли на главную страницу бота СТ "АМАТОР". Созданного для обмена информацией между членами товарищества и правлением.  
         НАПИШИТЕ ЛЮБОЕ СООБЩЕНИЕ для того чтоб подписаться и получить доступ к основному функционалу нашего бота.'''.format(viber_request.user.name)
        viber.send_messages(viber_request.user.id, [TextMessage(text=message_vcsr)])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ПРИВЕТСТВЕННОЕ *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")


    elif isinstance(viber_request, ViberSubscribedRequest):
        message_vsubsc='''Отлично, {0}! Вы успешно подписались на наш публичный канал СТ "АМАТОР", 
         и теперь вам доступен весь функционал нашего чат бота.'''.format(viber_request.user.name)
        viber.send_messages(viber_request.user.id, [TextMessage(text=message_vsubsc)])
        logger.debug("Получил запрос: ПОДПИСАТЬСЯ")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ПОДПИСАТЬСЯ *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")


    elif isinstance(viber_request, ViberUnsubscribedRequest):
        #message_vunsubsc='''{0}, Вы успешно отписались от нашего публичного канала СТ "АМАТОР"'''.format(viber_request.user_id)
        #viber.send_messages(viber_request.user_id, [TextMessage(text=message_vunsubsc)])    
        logger.debug("Получил запрос. ОТПИСАТЬСЯ")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ОТПИСАТЬСЯ *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("Клиент не получил сообщение. Ошибка: {0}".format(viber_request))

    return Response(status=200)

def set_webhook(viber):
    viber.set_webhook('https://b78923c85329.ngrok.io/')
if __name__ == "__main__":
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(10, 1, set_webhook, (viber,))
    t = threading.Thread(target=scheduler.run)
    t.start()
    context = ('server.crt', 'server.key')
    app.run(host='0.0.0.0', port=8443, debug=True)
    #app.run(host='0.0.0.0', port=8443, debug=True, ssl_context=context)