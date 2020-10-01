import os, re, openpyxl,pprint

phone_search= re.compile(r'''0[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]?\d''', re.VERBOSE|re.DOTALL)

while True:
    f_name= input("Введите название исходного файла с указанием раширения:")
    if os.path.exists(os.path.dirname(__file__) + "/" + f_name ):
        mybook= openpyxl.load_workbook(os.path.dirname(__file__) + "/" + f_name )
        break

sheet_list= mybook.sheetnames
print("\nИмпортированный файл имеет следующие вкладки:\n")
for i in range(len(sheet_list)):
    print("Вкладка №", i+1, sheet_list[i])

while True:
    sh_index= input("Выберите номер вкладки с которой желаете работать:")
    if sh_index.isnumeric:
        sh_index=int(sh_index)
        if sh_index>0 and sh_index<len(sheet_list)+1:
            break

act_sh=mybook[sheet_list[sh_index-1]]
print("\nВы выбрали вкладку:",act_sh.title, "\nКоторая имеет следующие размеры:\nКоличество строк-",act_sh.max_row,"\nКоличество столбцов-",act_sh.max_column)
col_max_name= openpyxl.utils.get_column_letter(act_sh.max_column)
print(col_max_name)

list_file= []
for i_stroki in act_sh["A1":col_max_name+str(act_sh.max_row)]:
    list_0=[]
    for y_column in i_stroki:
        list_0.append(y_column.value)
    list_file.append(list_0)

for i_str in range(len(list_file)):
    for y_col in range(len(list_file[i_str])):
        res= re.findall(phone_search, str(list_file[i_str][y_col]))
        if len(res)>0:
            
            for p in range(len(res)):
                res[p]="+38"+str(res[p])
            qq=0        
            for upd in range(0, len(res)):
                if qq==0:
                    qq=str(res[upd])
                else:
                    qq=qq +' '+ str(res[upd])
            list_file[i_str][y_col]=qq 
       
for w in range(len(list_file)):
    print(list_file[w])
        

xl_new= openpyxl.Workbook()
xl_new.active.title="Import data"
print(xl_new.active)
file_save=xl_new.active

for i in range(len(list_file)):
    for y in range(len(list_file[i])):
        file_save.cell(row=i+1, column=y+1).value = list_file[i][y]

xl_new.save(os.path.dirname(__file__)+'/'+"4400.xlsx")
