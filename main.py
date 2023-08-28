import time
import os
import sys
import pyautogui

os.system("cls")

pyautogui.hotkey('f11')

time.sleep(1)
print("""                                                       
                                                                          
                                       .'.  
                                       .....                                    ███╗   ███╗███████╗ ██████╗  █████╗ ██╗      ██████╗ ██████╗ ████████╗███████╗██████╗  █████╗
                                      ...  ..                                   ████╗ ████║██╔════╝██╔════╝ ██╔══██╗██║     ██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
                                      ..   ..                                   ██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║██║     ██║   ██║██╔═══╝    ██║   ██╔══╝  ██╔══██╗██╔══██║
                                                                                ██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║███████╗╚██████╔╝██║        ██║   ███████╗██║  ██║██║  ██║
                                     ...   ..                                   ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝                    
                                     .'.   ..                                   
      ....',,,''....                  ',......                                  
    .,:c::::::;;;;::c:,'..          . 'lolcl,                   .....'''..      
     .,:ccc::;:;;,,;:ldxo:,'...      ..coooo' .          ...,:ccllcccloddol:'   
       .';llcc:c:;::ccclddc;;:;,...  ..'ldx:..     ...',;codxxddooollloxxxxdc.  
          .';:cllllllllclll:;;:c:;;,''.;ldkc.....,;:clcldkkkxddddddddddxdl:'    
              .',:clodddollccclccllloollodxl;:cccllloooxkOOOkOOkkxxdlc;'.       
         ..';;;;;:ccldxxxdoooolcclloddodxxxoddddxdodddxOOOOxoc;''...            
        .cddoc::cllllooddolllllloolloxxxxxxooodddxxkOO000Okdl:;,'.'..           
        .:lolcclllllooooc::::cloodddlllloolclddddxkkkOO00OOOOkxolccllc;.        
           .',:ccloooolc:;:::codoodxl;'.,;;,cdxkkxxxxkO0000OOkkkxolcoddo;.      
               ...''''''',:clodddxxoc,..,;. :xdxxxkkkxxkOOOOOOOkkxdoolc;'.      
                           ...',','... .:'  ...,,,;:cc::;,,;;::;;,'...          
                                    .. 'c.  ..                                  
                                    . .;o'  .                                   
                                      .;;.                                      
                                       .             
""")

time.sleep(0.5)
choice = input("Have you modified the api key (Y/N)?")
if choice == "Y":
  os.system("pyinstaller megaloptera.py")
else:
  print("go see this github")

