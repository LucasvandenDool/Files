__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile

os.chdir('C:\\Users\\lucas\\Winc\\files')

#Clean Cache \\\\\\\\
def clean_cache():
    path = 'C:\\Users\\lucas\\Winc\\files\\cache'
    if os.path.exists('cache'):
        shutil.rmtree(path)    
    os.makedirs('cache')
    
#Zip Cache \\\\\\\\
zip_path = 'C:\\Users\\lucas\\Winc\\files\\data.zip'

def cache_zip(zip_path, cache_path):
    with ZipFile(zip_path, 'r') as zip:
        zip.extractall(cache_path)

#Cached Files \\\\\\\\
cache = os.path.abspath("cache")

def cached_files():
    lijst = []
    for file in os.listdir(cache):
        absolute_path = os.path.join(cache, file)
        lijst.append(absolute_path)
    return lijst

#Find Password \\\\\\\\
def find_password(lijst):
    for file in lijst:
        search = open(file, "r")
        for line in search:
            if ("password") in line:
                return line.replace("password: ", "").rstrip('\n')
