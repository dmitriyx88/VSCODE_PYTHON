from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
import pickle
import os
import msg_text
from keyboard_dict import keyboard_dict
cur_dir=f"{os.path.dirname(__file__)}"
user_file_name="data.file"

user_amator= {}




def file_io(method):
    global user_amator
    if os.path.isfile(f"{cur_dir}\{user_file_name}") and method=="read" and os.path.getsize(f"{os.path.dirname(__file__)}\{user_file_name}")>0:
        with open(f"{cur_dir}\{user_file_name}", "rb") as file_pickle:
            user_amator=pickle.load(file_pickle)
            print("\n\nPICKLE LOAD START!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n", user_amator, "\nPICKLE LOAD END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",)
    if method=="write":
        with open(f"{cur_dir}\{user_file_name}", "wb") as file_pickle:
            print("\n\nPICKLE DUMP START!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n", user_amator, "\n\nPICKLE DUMP END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            pickle.dump(user_amator, file_pickle)

def ConversationStarted(viber, viber_request):
    result= viber.send_messages(viber_request.user.id, [TextMessage(text=msg_text.msg_text[0].format(viber_request.user.name))])
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ПРИВЕТСТВЕННОЕ *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*", result, type(result))
    file_io("read")
    user_amator[viber_request.user.id]=dict(name=viber_request.user.name, avatar=viber_request.user.avatar, country=viber_request.user.country, subscrib=False, phone_number=None, registered=False)
    file_io("write")


def Subscribed(viber, viber_request):
    file_io("read")
    viber.send_messages(viber_request.user.id, [TextMessage(text=msg_text.msg_text[1].format(viber_request.user.name))])
    user_amator[viber_request.user.id]["subscrib"]=True
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ПОДПИСАТЬСЯ *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    #ViberMessage(viber, viber_request)

def ViberMessage(viber, viber_request):
    file_io("read")
    if viber_request.sender.id in user_amator or viber_request.user.id in user_amator:
        
        if (user_amator[viber_request.sender.id]["subscrib"]==False
        and user_amator[viber_request.sender.id]["registered"]==False 
        and user_amator[viber_request.sender.id]["phone_number"]==None):
            viber.send_messages(viber_request.sender.id, [TextMessage(text=msg_text.msg_text[1].format(user_amator[viber_request.sender.id]["name"]))])
            user_amator[viber_request.sender.id]["subscrib"]=True
            file_io("write")
            return

        if (user_amator[viber_request.sender.id]["subscrib"]==True
        and user_amator[viber_request.sender.id]["registered"]==False 
        and user_amator[viber_request.sender.id]["phone_number"]==None):
            #viber.send_messages(viber_request.sender.id, [TextMessage(text=msg_text.msg_text[2])])
            viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=3, keyboard=keyboard_dict["REG_KEYBOARD"], text=msg_text.msg_text[2])])
            user_amator[viber_request.sender.id]["phone_number"]= viber_request.message.contact.phone_number
            print("--------------------------------TELEPHONE---------", user_amator[viber_request.sender.id]["phone_number"])
            file_io("write")
            




