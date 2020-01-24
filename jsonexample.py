import json
def JsonDumpData(filename, data):
    try: 
        with open(filename, "w", encoding="utf-8") as f_obj:
            json.dump(data, f_obj, ensure_ascii=False)
    except FileNotFoundError as ferr:
        print(ferr)

def JsonReadData(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f_obj:
            content = json.load(f_obj)
            return content
    except FileNotFoundError as ferr:
        print(ferr)

list = ['a', 'b', 'å', 'ä', 'ö']

JsonDumpData('./data_file/jsondata.json', list)
list2 = JsonReadData('./data_file/userinfo.json')
print(list2)