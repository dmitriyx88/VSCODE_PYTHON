import datetime
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
from viberbot.api.messages.contact_message import ContactMessage

from delivered_buffer import SendMess
from delivered_buffer import FindMess
from keyboard_dict import keyboard_reg
from keyboard_dict import keyboard_main
from keyboard_dict import keyboard_main_return

from keyboard_dict import keyboard_energy
from keyboard_dict import keyboard_energy_send
from msg_text import msg_text
from import_xls import find_user
from file_io import file_io
import datetime
import operator

def is_correct(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def ViberMessage(viber, viber_request, user_amator):
#    while True:

    if (viber_request.sender.id in user_amator
    and user_amator[viber_request.sender.id]):
        while True:
                
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
                result=viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_main, text=msg_text[4].format(user_amator[viber_request.sender.id]["db_data"][0]["name2"], user_amator[viber_request.sender.id]["db_data"][0]["name3"]))])
                user_amator[viber_request.sender.id]["href"]="MAIN_1"

        
            
            if (user_amator[viber_request.sender.id]["href"]=="MAIN_1"
            and hasattr(viber_request.message, "text")):
                if viber_request.message.text=="VznosInfo":
                    user_amator[viber_request.sender.id]["href"]="VZNOS_INFO_0"
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++Получен запрос информации")
                if viber_request.message.text=="SendEnergy":
                    user_amator[viber_request.sender.id]["href"]="SEND_ENERGY_0"
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++Получен запрос Отправить показание")        
                if viber_request.message.text=="AnketaInfo":
                    user_amator[viber_request.sender.id]["href"]="ANKETA_INFO_0"
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++Получен запрос АНКЕТА")
                if viber_request.message.text=="KontactInfo":
                    user_amator[viber_request.sender.id]["href"]="KONTACT_INFO_0"
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++Получен запрос АНКЕТА")


            if user_amator[viber_request.sender.id]["href"]=="VZNOS_INFO_0":
                user_amator[viber_request.sender.id]["href"]="VZNOS_INFO_1"
                print("\n\n\n", user_amator[viber_request.sender.id]["db_data"], "\n\n\n")
                for i in user_amator[viber_request.sender.id]["db_data"]:
                    res=msg_text[5].format(**i)
                    result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_main, text=res)])
                    user_amator[viber_request.sender.id]["href"]="MAIN_1"

            if user_amator[viber_request.sender.id]["href"]=="ANKETA_INFO_0":
                user_amator[viber_request.sender.id]["href"]="ANKETA_INFO_1"
                print("\n\n\n", user_amator[viber_request.sender.id]["db_data"], "\n\n\n")
                for i in user_amator[viber_request.sender.id]["db_data"]:
                    res=msg_text[6].format(**i)
                    result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_main, text=res)])
                    user_amator[viber_request.sender.id]["href"]="MAIN_1"
                res=msg_text[7]
                result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_main, text=res)])

            if user_amator[viber_request.sender.id]["href"]=="KONTACT_INFO_0":
                user_amator[viber_request.sender.id]["href"]="KONTACT_INFO_1"
                res=msg_text[8]
                result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_main, text=res)])
                user_amator[viber_request.sender.id]["href"]="MAIN_1"

            if user_amator[viber_request.sender.id]["href"]=="SEND_ENERGY_0":
                user_amator[viber_request.sender.id]["href"]="SEND_ENERGY_1"
                res=msg_text[4].format(user_amator[viber_request.sender.id]["db_data"][0]["name2"], user_amator[viber_request.sender.id]["db_data"][0]["name3"])
                result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_energy, text=res)])
                        
            if (user_amator[viber_request.sender.id]["href"]=="SEND_ENERGY_1"
            and hasattr(viber_request.message, "text")):

                if viber_request.message.text=="StoryEnergy":
                    user_amator[viber_request.sender.id]["href"]="STORY_ENERGY_0"
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++Получен запрос история показаний")
                if viber_request.message.text=="SendEnergyForm":
                    user_amator[viber_request.sender.id]["href"]="SEND_ENERGY_FORM_0"
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++Получен запрос Отправить показание")        
                if viber_request.message.text=="MainMenu":
                    user_amator[viber_request.sender.id]["href"]="MAIN_0"
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++Получен запрос выход в меню")
                    continue


            if user_amator[viber_request.sender.id]["href"]=="SEND_ENERGY_FORM_0":
                res=msg_text[9]
                result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_main_return, text=res)])
                user_amator[viber_request.sender.id]["href"]="SEND_ENERGY_FORM_1"

            if (user_amator[viber_request.sender.id]["href"]=="SEND_ENERGY_FORM_1"
            and hasattr(viber_request.message, "text")
            and not is_correct(viber_request.message.text)
            and viber_request.message.text!="SendEnergyForm"):    
                if viber_request.message.text=="MainMenu":
                    user_amator[viber_request.sender.id]["href"]="MAIN_0"
                    continue
                res=msg_text[11]
                result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_energy, text=res)])         


            if (user_amator[viber_request.sender.id]["href"]=="SEND_ENERGY_FORM_1"
            and hasattr(viber_request.message, "text")
            and is_correct(viber_request.message.text)
            and viber_request.message.text!="SendEnergyForm"):
                user_amator[viber_request.sender.id]["buffer1_energy"]=float(viber_request.message.text)
                res=msg_text[12].format(user_amator[viber_request.sender.id]["buffer1_energy"])
                result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_energy_send, text=res)])
                user_amator[viber_request.sender.id]["href"]="SEND_ENERGY_FORM_2"
                
            if (user_amator[viber_request.sender.id]["href"]=="SEND_ENERGY_FORM_2"
            and hasattr(viber_request.message, "text")
            and user_amator[viber_request.sender.id]["buffer1_energy"]):
                if viber_request.message.text=="Send_Energy_Pr":      
                    now= datetime.datetime.now()  
                    dict_energy=dict(uchastok_id=None, data=str(now.date()), energy_val_1=0, energy_val_0=user_amator[viber_request.sender.id]["buffer1_energy"], kvt=0, summ_kvt=0, oplacheno=0, avans=0, dolg=0, send_msg_upd=None )
                    user_amator[viber_request.sender.id]["energy"].append(dict_energy)
                    user_amator[viber_request.sender.id]["buffer1_energy"]=False
                    res=msg_text[13]
                    result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_main, text=res)])         
                    user_amator[viber_request.sender.id]["href"]="MAIN_1"
                    continue
                if viber_request.message.text=="MAIN_0":
                    user_amator[viber_request.sender.id]["href"]="MAIN_1"
                    continue





            if (user_amator[viber_request.sender.id]["href"]=="STORY_ENERGY_0"
            and len(user_amator[viber_request.sender.id]["energy"])==0):
                    res=msg_text[14]
                    result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_main, text=res)])   
                    user_amator[viber_request.sender.id]["href"]="MAIN_1"
                    continue

            if (user_amator[viber_request.sender.id]["href"]=="STORY_ENERGY_0"
            and len(user_amator[viber_request.sender.id]["energy"])>0):
                res=msg_text[15]
                res_din=""
                #result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, text=res)])   
                #user_amator[viber_request.sender.id]["energy"].sort(key=operator.itemgetter("data"))
                for m in user_amator[viber_request.sender.id]["energy"]:
                    res_din= res_din + "-->{data}: Показание-{energy_val_0}\r\nКол-во кВт:{kvt}.\r\nК ОПЛАТЕ:{dolg} \r\n\r\n".format(**m)
                concat=res+res_din
                result = viber.send_messages(viber_request.sender.id, [TextMessage(min_api_version=4, keyboard=keyboard_main, text=concat)])
                user_amator[viber_request.sender.id]["href"]="MAIN_1"
                continue                        
            
            break                    
                    

    return user_amator    
