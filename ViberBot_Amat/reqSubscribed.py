from file_io import file_io
from viberbot.api.messages.text_message import TextMessage
from delivered_buffer import SendMess
from msg_text import msg_text
from data_viber import user_amator

def Subscribed(viber, viber_request):
    file_io("read")
    if viber_request.user.id in user_amator:
        user_amator[viber_request.user.id]["subscrib"]=True
        file_io("write")
        result = viber.send_messages(viber_request.user.id, [TextMessage(text=msg_text[1].format(viber_request.user.name))])
        if result[0]>0:
            SendMess(viber_request.user.id, viber_request.user.name, "Subscribed", msg_text[1].format(viber_request.user.name), result[0] )
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* УВЕДОМЛЕНИЕ О ПОДПИСКЕ ОТПРАВЛЕННО УСПЕШНО *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*", result)