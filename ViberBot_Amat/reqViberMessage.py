from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
from viberbot.api.messages.contact_message import ContactMessage

from delivered_buffer import SendMess
from delivered_buffer import FindMess
from keyboard_dict import keyboard_reg
from keyboard_dict import keyboard_main
from msg_text import msg_text
from import_xls import find_user
from file_io import file_io



def ViberMessage(viber, viber_request, user_amator):
 
    if (viber_request.sender.id in user_amator
    and user_amator[viber_request.sender.id]):

        #print("\\\\\\\\\\\\\\ Request:", viber_request)
        
        if (user_amator[viber_request.sender.id]["subscrib"]==False
        and user_amator[viber_request.sender.id]["registered"]==False 
        and user_amator[viber_request.sender.id]["phone_number"]==None
        and user_amator[viber_request.sender.id]["href"]==None):
            user_amator[viber_request.sender.id]["subscrib"]=True
            user_amator[viber_request.sender.id]["href"]="REG_FORM_0"
            result=viber.send_messages(viber_request.sender.id, [TextMessage(text=msg_text[1].format(user_amator[viber_request.sender.id]["name"]))])
            if result[0]>0:
                SendMess(viber_request.sender.id, viber_request.sender.name, "ViberMessage:Subscribed", msg_text[1].format(viber_request.sender.name), result[0] )

        if (user_amator[viber_request.sender.id]["subscrib"]==True
        and user_amator[viber_request.sender.id]["registered"]==False 
        and user_amator[viber_request.sender.id]["phone_number"]==None
        and user_amator[viber_request.sender.id]["href"]=="REG_FORM_0"):
            result=viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=3, keyboard=keyboard_reg, text=msg_text[2])])
            user_amator[viber_request.sender.id]["href"]="REG_FORM_1"
            if result[0]>0:
                SendMess(viber_request.sender.id, viber_request.sender.name, "ViberMessage:SendPhoneKeyboard", msg_text[2].format(viber_request.sender.name), result[0] )
                user_amator[viber_request.sender.id]["phone_number"]= False
                user_amator[viber_request.sender.id]["href"]="REG_0"

        if (user_amator[viber_request.sender.id]["subscrib"]==True
        and user_amator[viber_request.sender.id]["registered"]==False 
        and user_amator[viber_request.sender.id]["phone_number"]==False
        and user_amator[viber_request.sender.id]["href"]=="REG_0"
        and hasattr(viber_request.message, "contact")):            
            user_amator[viber_request.sender.id]["phone_number"]= viber_request.message.contact.phone_number
            find_phone=find_user("tel1", user_amator[viber_request.sender.id]["phone_number"])
            if len(find_phone)>0:
                user_amator[viber_request.sender.id]["db_data"]=find_phone
                user_amator[viber_request.sender.id]["href"]="REG_1"
                result = viber.send_messages(viber_request.sender.id, [TextMessage(text=msg_text[3])])
                if result[0]>0:
                    SendMess(viber_request.sender.id, viber_request.sender.name, "ViberMessage:SuccesRegistration", msg_text[3], result[0] )
                    user_amator[viber_request.sender.id]["registered"]= True
                    user_amator[viber_request.sender.id]["href"]= "MAIN_0"
        
        if (user_amator[viber_request.sender.id]["registered"]==True
        and user_amator[viber_request.sender.id]["href"]=="MAIN_0"):
            #result = viber.send_messages(viber_request.sender.id, [TextMessage(text=msg_text[4].format(user_amator[viber_request.sender.id]["db_data"][0]["name2"], user_amator[viber_request.sender.id]["db_data"][0]["name3"]))])
            result=viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_main, text=msg_text[4].format(user_amator[viber_request.sender.id]["db_data"][0]["name2"], user_amator[viber_request.sender.id]["db_data"][0]["name3"]))])
            if result[0]>0:
                SendMess(viber_request.sender.id, viber_request.sender.name, "ViberMessage:MainMenu", msg_text[4], result[0] )
                user_amator[viber_request.sender.id]["href"]="MAIN_1"
                return user_amator
    
        
        if user_amator[viber_request.sender.id]["href"]=="MAIN_1":
            """print("++++++++++++++++++++++++++++Мы ЗДЕСЬ!!!!")
            print(dir(viber_request))
            print(dir(viber_request.sender))
            print(dir(viber_request.message))
            print(viber_request.message.text)"""

            if viber_request.message.text=="VznosInfo":
                user_amator[viber_request.sender.id]["href"]="VZNOS_INFO_0"
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++Получен запрос информации")
            if viber_request.message.text=="SendEnergy":
                user_amator[viber_request.sender.id]["href"]="SEND_ENERGY_0"
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++Получен запрос Отправить показание")        
            if viber_request.message.text=="AnketaInfo":
                user_amator[viber_request.sender.id]["href"]="ANKETA_INFO_0"
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++Получен запрос АНКЕТА")
        
        if user_amator[viber_request.sender.id]["href"]=="VZNOS_INFO_0":
            user_amator[viber_request.sender.id]["href"]="VZNOS_INFO_1"
            print("\n\n\n", user_amator[viber_request.sender.id]["db_data"], "\n\n\n")
            for i in user_amator[viber_request.sender.id]["db_data"]:
                res=msg_text[5].format(i["uchastok_id"], i["line_id"], i["s_uchastka"], i["vzn2021"], i["opl2021"], i["vzn2020"], i["opl2020"], i["vzn2019"], i["opl2019"] )
                result = viber.send_messages(viber_request.sender.id, [TextMessage(text=res)])


    return user_amator    

