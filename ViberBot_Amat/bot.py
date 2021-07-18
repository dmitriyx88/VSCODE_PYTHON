from flask import Flask, request, Response
from viberbot import Api
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

bot_configuration = BotConfiguration(
	name='ST Amator',
	avatar='http://viber.com/avatar.jpg',
	auth_token='4daa90c76a27d2bd-da20e99cc428dc26-491a88d6cd292369')
viber = Api(bot_configuration)



@app.route('/', methods=['POST'])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        # lets echo back
        viber.send_messages(viber_request.sender.id, [
            message
        ])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)

app.run(host='0.0.0.0', port=443, debug=True)
viber.set_webhook('https://fdd4b599bc45.ngrok.io')
#viber.set_webhook('https://fdd4b599bc45.ngrok.io')

