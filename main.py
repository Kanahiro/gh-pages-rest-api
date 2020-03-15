import os
import glob
import json
from exlib import json2dir

def dir_list_of(jsondata, current_dir='')->list:
    dirs = []
    if isinstance(jsondata, int) or isinstance(jsondata, str):
        return dirs
    elif isinstance(jsondata, list):
        for i in range(len(jsondata)):
            cur_dir = current_dir + '/' + str(i)
            dirs.append(cur_dir)
            dirs += dir_list_of(jsondata[i], cur_dir)
    elif isinstance(jsondata, dict):
        for key in jsondata:
            cur_dir = current_dir + '/' + key
            dirs.append(cur_dir)
            dirs += dir_list_of(jsondata[key], cur_dir)

    return dirs

def seperate_jsons(jsondata, current_dir='')->list:
    dirs = []
    write_dict_as_json(jsondata, current_dir + '/index.html')
    if isinstance(jsondata, int) or isinstance(jsondata, str):
        write_text(jsondata, current_dir + '/index.html')
        return dirs
    elif isinstance(jsondata, list):
        for i in range(len(jsondata)):
            cur_dir = current_dir + '/' + str(i)
            dirs.append(cur_dir)
            dirs += seperate_jsons(jsondata[i], cur_dir)
    elif isinstance(jsondata, dict):
        for key in jsondata:
            cur_dir = current_dir + '/' + key
            dirs.append(cur_dir)
            dirs += seperate_jsons(jsondata[key], cur_dir)

    return dirs

def write_dict_as_json(jsondata:dict, output_filepath=''):
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(jsondata, f, indent=4)

def write_text(data, output_filepath=''):
    with open(output_filepath, mode='w') as f:
        f.write(str(data))

if __name__ == "__main__":
    jsonfiles = glob.glob('./json/*')
    for jsonfile in jsonfiles:
        jsondict = {}
        filename = os.path.splitext(os.path.basename(jsonfile))[0]
        with open(jsonfile, encoding='utf-8') as f:
            jsondict = json.loads(f.read())
        root_dir = 'api/' + filename
        os.makedirs(root_dir, exist_ok=True)
        dirs = dir_list_of(jsondict, root_dir)
        for d in dirs:
            os.makedirs(d, exist_ok=True)
        seperate_jsons(jsondict, root_dir)
