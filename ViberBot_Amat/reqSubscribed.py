from viberbot.api.messages.text_message import TextMessage
from delivered_buffer import SendMess
from msg_text import msg_text


def Subscribed(viber, viber_request, user_amator):
    if viber_request.user.id in user_amator:
        user_amator[viber_request.user.id]["subscrib"]=True
        result = viber.send_messages(viber_request.user.id, [TextMessage(text=msg_text[1].format(viber_request.user.name))])
        if result[0]>0:
            SendMess(viber_request.user.id, viber_request.user.name, "Subscribed", msg_text[1].format(viber_request.user.name), result[0] )
    return user_amator