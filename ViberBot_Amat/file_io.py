import os
import pickle
from data_viber import user_amator

cur_dir=f"{os.path.dirname(__file__)}"
user_file_name="data.file"

def file_io(method):
    global user_amator
    if os.path.isfile(f"{cur_dir}\{user_file_name}") and method=="read" and os.path.getsize(f"{os.path.dirname(__file__)}\{user_file_name}")>0:
        with open(f"{cur_dir}\{user_file_name}", "rb") as file_pickle:
            user_amator=pickle.load(file_pickle)
            print("\nPICKLE LOAD START!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n", user_amator, "\n\nPICKLE LOAD END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",)
    if method=="write":
        with open(f"{cur_dir}\{user_file_name}", "wb") as file_pickle:
            print("\nPICKLE DUMP START!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n", user_amator, "\n\nPICKLE DUMP END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            pickle.dump(user_amator, file_pickle)