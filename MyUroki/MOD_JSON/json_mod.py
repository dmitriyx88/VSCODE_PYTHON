import json,pprint

string_pars='["Dmitriy", {"Intelekt":"Umnui", "Vneshnost":"Krasiviy", "Kharater":["Dobrui","Pokladistui","Nastoichivui"]}]'

json_v= json.loads(string_pars)

v_json = json.dumps(json_v)

print(type(json_v), type(v_json)) 

print(json_v)
print(v_jso)