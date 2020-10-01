import csv, os

file = open(os.path.dirname(__file__)+"/"+"200.csv")
csv_file = csv.reader(file, delimiter=";")

csv_in_list= list(csv_file)

for i in csv_in_list:
    print(i)



file_save_csv= open(os.path.dirname(__file__)+"/"+"new_file.csv", 'w', newline="")
csv_writer_obj= csv.writer(file_save_csv, delimiter=";")

for i in csv_in_list:
    if i[0]="24":
        csv_writer_obj.writerow(i)


file.close()
file_save_csv.close()