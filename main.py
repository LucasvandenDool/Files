__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os 
import shutil 
from zipfile import ZipFile 


cache = os.path.join(os.getcwd(), 'files', 'cache')


#Clean Cache \\\\\\\\
def clean_cache():
    if os.path.exists(cache):
        shutil.rmtree(cache)
    return os.mkdir(cache)

#Zip Cache \\\\\\\\
zip_path = os.getcwd()

def cache_zip(zip_path, cache_path):
    with ZipFile(zip_path, 'r') as zip:
        zip.extractall(cache_path)

#Cached Files \\\\\\\\
cached = os.path.abspath(cache)

def cached_files():
    lijst = []
    for file in os.listdir(cached):
        absolute_path = os.path.join(cached, file)
        lijst.append(absolute_path)
    return lijst

#Find Password \\\\\\\\
def find_password(lijst):
    for file in lijst:
        search = open(file, "r")
        for line in search:
            if ("password") in line:
                return line.replace("password: ", "").rstrip('\n')
