import os
import glob
import json

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