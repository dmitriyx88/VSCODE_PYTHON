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
from viberbot.api.viber_requests import ViberDeliveredRequest
from viberbot.api.viber_requests import ViberSeenRequest

import time
import logging
import sched
import threading

import reqConversationStarted
import reqSubscribed
import reqViberMessage
from file_io import file_io

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

user_amator= {}


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
    
    global user_amator
    if len(user_amator)==0:
        user_amator=file_io("read", user_amator, "StartBot")    

    if isinstance(viber_request, ViberMessageRequest):
        file_io("read", user_amator, "FuncMessageRequest")
        user_amator=reqViberMessage.ViberMessage(viber, viber_request, user_amator)
        file_io("write", user_amator, "FuncMessageRequest")
    
    
        
    elif isinstance(viber_request, ViberConversationStartedRequest):
        file_io("read", user_amator, "FuncConversationRequest")
        user_amator=reqConversationStarted.ConversationStarted(viber, viber_request, user_amator)
        file_io("write", user_amator, "FuncConversationRequest")
        

    elif isinstance(viber_request, ViberSubscribedRequest):
        file_io("read", user_amator, "FuncSubscribedRequest")
        user_amator=reqSubscribed.Subscribed(viber, viber_request, user_amator)
        file_io("write", user_amator, "FuncSubscribedRequest")


    elif isinstance(viber_request, ViberDeliveredRequest):
        pass

    elif isinstance(viber_request, ViberSeenRequest):
        pass

    elif isinstance(viber_request, ViberUnsubscribedRequest):
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ОТПИСАТЬСЯ *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    elif isinstance(viber_request, ViberFailedRequest):
        pass

    return Response(status=200)

def set_webhook(viber):
    viber.set_webhook('https://c822eb52fefe.ngrok.io/')
if __name__ == "__main__":
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(6, 1, set_webhook, (viber,))
    t = threading.Thread(target=scheduler.run)
    t.start()
    context = ('server.crt', 'server.key')
    app.run(host='0.0.0.0', port=8443, debug=True)
    #app.run(host='0.0.0.0', port=8443, debug=True, ssl_context=context)