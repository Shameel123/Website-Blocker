import time
from datetime import datetime as dt
#time.sleep(5) #-->Runs after 5 seconds


host_path = r"C:\Windows\System32\drivers\etc\hosts"
#remove above comment if you want to seriously run this :-)
#host_path = "hosts"
redirect="127.0.0.100"
website_list = ["www.facebook.com","facebook.com","gmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours")
        with open(host_path,"r+") as file: #r+ helps to read as well as write.
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
        time.sleep(5)
        file.close()

    else:
        print("Not working hours")
        with open(host_path,"r+") as file: #r+ helps to read as well as write.
            content = file.readlines()
            file.seek(0)#it is necessary to place pointer at the very first of the file.
            for line in content:
                if not any(website in line for website in website_list):
                    # if www.facebook.com is not in first line of hosts then write first line of host on host same to same.
                    file.write(line)
            file.truncate
        time.sleep(5)
        file.close()
