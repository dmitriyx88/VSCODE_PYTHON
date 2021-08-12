from viberbot.api.messages.text_message import TextMessage
from delivered_buffer import SendMess
from msg_text import msg_text


def ConversationStarted(viber, viber_request, user_amator):
    user_amator[viber_request.user.id]=dict(name=viber_request.user.name, avatar=viber_request.user.avatar, country=viber_request.user.country, subscrib=False, phone_number=None, registered=False, db_data=None, href=None)
    result = viber.send_messages(viber_request.user.id, [TextMessage(text=msg_text[0].format(viber_request.user.name))])
    if result[0]>0:
        SendMess(viber_request.user.id, viber_request.user.name, "ConversationStarted", msg_text[0].format(viber_request.user.name), result[0] )
    return user_amator
