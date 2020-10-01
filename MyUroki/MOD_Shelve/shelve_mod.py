import shelve

file= shelve.open("mydbfile")
file["car"]="Hunday"
file["model"]="Tucson"
file["Year"]=2004
file.close()

file1= shelve.open("mydbfile")
print(file1["car"])
file1.close()