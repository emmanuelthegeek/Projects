from datetime import datetime as time1
import time
host = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
sites = [input("Enter your website: ")]
print("Your website has been blocked for the specified time")
while True:
    start = time1(time1.now().year, time1.now().month, time1.now().day, 8)
    present_time = time1.now()
    end = time1(time1.now().year, time1.now().month, time1.now().day, 19)
    if start < present_time < end:
        with open(host, 'r+') as file:
            content = file.read()
            for websites in sites:
                if websites in content:
                    pass
            else:
                file.write(redirect + " " + websites + "\n")
        time.sleep(30)
    else:
        with open(host, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in sites):
                    file.write(line)
            file.truncate()
            time.sleep(30)