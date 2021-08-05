from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage

from file_io import file_io
from delivered_buffer import SendMess
from delivered_buffer import FindMess
from keyboard_dict import keyboard_dict
from msg_text import msg_text
from data_viber import user_amator




def ViberMessage(viber, viber_request):
    file_io("read")
    if viber_request.sender.id in user_amator or viber_request.user.id in user_amator:
        
        if (user_amator[viber_request.sender.id]["subscrib"]==False
        and user_amator[viber_request.sender.id]["registered"]==False 
        and user_amator[viber_request.sender.id]["phone_number"]==None):
            user_amator[viber_request.sender.id]["subscrib"]=True
            file_io("write")
            result=viber.send_messages(viber_request.sender.id, [TextMessage(text=msg_text[1].format(user_amator[viber_request.sender.id]["name"]))])
            if result[0]>0:
                SendMess(viber_request.sender.id, viber_request.sender.name, "ViberMessage:Subscribed", msg_text[1].format(viber_request.sender.name), result[0] )
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* УВЕДОМЛЕНИЕ О ПОДПИСКЕ ОТПРАВЛЕННО УСПЕШНО *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*", result)

        """ if (user_amator[viber_request.sender.id]["subscrib"]==True
        and user_amator[viber_request.sender.id]["registered"]==False 
        and user_amator[viber_request.sender.id]["phone_number"]==None
        and FindMess(viber_request.sender.id, "ViberMessage:SendPhone")==None):
            result=viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=3, keyboard=keyboard_dict["REG_KEYBOARD"], text=msg_text[2])])
            if result[0]>0:
                SendMess(viber_request.sender.id, viber_request.sender.name, "ViberMessage:SendPhone", msg_text[2].format(viber_request.sender.name), result[0] )
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ЗАПРОС ТЕЛЕФОННОГО НОМЕРА ОТПРАВЛЕННО УСПЕШНО *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*", result)

            #user_amator[viber_request.sender.id]["phone_number"]= viber_request.message.contact.phone_number
            print("--------------------------------TELEPHONE---------", user_amator[viber_request.sender.id]["phone_number"])
            file_io("write")"""
            
