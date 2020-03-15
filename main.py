import os
import glob
import json
from exlib import json2dir

if __name__ == "__main__":
    jsonfiles = glob.glob('./json/*')
    for jsonfile in jsonfiles:
        jsondict = {}
        with open(jsonfile, encoding='utf-8') as f:
            jsondict = json.loads(f.read())
        dirs = json2dir.dir_list_of(jsondict)
        for d in dirs:
            os.makedirs('api' + d, exist_ok=True)
