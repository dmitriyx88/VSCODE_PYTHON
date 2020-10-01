import threading, time

print("Начало программы")

def funk():
    time.sleep(10)
    print("Я проснулся")


th_obj= threading.Thread(target=funk)
th_obj1=threading.Thread(target=funk)
th_obj.start()
th_obj1.start()

print("Конец программы")