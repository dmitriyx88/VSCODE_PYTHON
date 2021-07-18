from flask import Flask, request, Response
from viberbot import Api
from viberbot.api import viber_requests
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
		message = viber_request.message
		viber.send_messages(viber_request.sender.id, [
			message
		])
        
	elif isinstance(viber_request, ViberConversationStartedRequest) \
			or isinstance(viber_request, ViberSubscribedRequest) \
			or isinstance(viber_request, ViberUnsubscribedRequest):
		viber.send_messages(viber_request.sender.id, [
			TextMessage(None, None, viber_request.get_event_type())
		])

	elif isinstance(viber_request, ViberFailedRequest):
		logger.warn("Клиент не получил сообщение. Ошибка: {0}".format(viber_request))

	return Response(status=200)


def set_webhook(viber):
	viber.set_webhook('https://2f9990a5c08a.ngrok.io')
if __name__ == "__main__":
	scheduler = sched.scheduler(time.time, time.sleep)
	scheduler.enter(10, 1, set_webhook, (viber,))
	t = threading.Thread(target=scheduler.run)
	t.start()
	context = ('server.crt', 'server.key')
	app.run(host='0.0.0.0', port=8443, debug=True)
    #app.run(host='0.0.0.0', port=8443, debug=True, ssl_context=context)