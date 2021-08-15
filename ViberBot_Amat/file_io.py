import os
import pickle


cur_dir=f"{os.path.dirname(__file__)}"
user_file_name="data.file"

def file_io(method, user_amator, func):
    if os.path.isfile(f"{cur_dir}\\{user_file_name}") and method=="read" and os.path.getsize(f"{os.path.dirname(__file__)}\\{user_file_name}")>0:
        with open(f"{cur_dir}\\{user_file_name}", "rb") as file_pickle:
            user_amator=pickle.load(file_pickle)
            #print("\nPICKLE LOAD START", func, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n", user_amator, "\nPICKLE LOAD END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",)
    if method=="write":
        with open(f"{cur_dir}\\{user_file_name}", "wb") as file_pickle:
            #print("\nPICKLE DUMP START", func, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n", user_amator, "\nPICKLE DUMP END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            pickle.dump(user_amator, file_pickle)
    return user_amator