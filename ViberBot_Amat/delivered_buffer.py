delivered_buffer={}

def SendMess(id, name, func, text_mes, msg_token):
    delivered_buffer[msg_token]= dict(user_id=id, user_name=name, function=func, text=text_mes, deliv=False, seen=False)
    print("/////////////////////СООБЩЕНИЕ:", msg_token, "ОТПРАВЛЕНО ПОЛЬЗОВАТЕЛЮ:", name, ", ФУНКЦИЯ:", func)


def FindMess(id, func):
    for key, val in delivered_buffer.items():
        if ( val["user_id"]==id and  val["function"]==func):
            token= key
            deliv= val["deliv"]
            seen=val["seen"]
            print("+++++Функция поиска сообщений: Сообщение найдено, ", token, deliv, seen)
            return token
        else: 
            print("+++++Функция поиска сообщений: Сообщение не найдено")
            return None   