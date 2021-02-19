# Run this script as root 
import time 
from datetime import datetime as dt

  
# change hosts path according to your OS 
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# localhost's IP 
redirect = "127.0.0.1"
 

# websites That we want to block 
blokace = "C:\Users\servis\Python\Projekty\WebsiteBlocker\blokace.txt"
soubor = open(blokace,"r")
for radek in soubor:
    website_list=[radek.strip() for radek in open(blokace,"r")]
sites_to_block=[]
for site in website_list:
    sites_to_block.append(site)
    sites_to_block.append(site[4:])


#-----------------------------------

def blocks_sites():
    #while True:
        # time of your work 
        if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16): 
            print("Working hours...") 
            with open(hosts_path, 'r+') as hostsfile: 
                hosts_content = hostsfile.read() 
                for site in sites_to_block: 
                    if site not in hosts_content: 
                        # mapping hostnames to your localhost IP address 
                        hostsfile.write(redirect + " " + site + "\n") 
        else: 
            print("unblock sites")
            with open(hosts_path, 'r+') as hostsfile:
                lines = hostsfile.readlines()
                hostsfile.seek(0)
                for line in lines:
                    if not any(site in line for site in sites_to_block):
                        hostsfile.write(line)
                # removing hostnmes from host file
                hostsfile.truncate()
        time.sleep(5) #zabalit do funkce v argumentu website_list, konzultace
        #
        #if __name__== ten kontrektni soubor, pokud je prvni a neni importovany, tak bude mit jmeno main,

    # sudo python script.py
if __name__ == '__main__':
   blocks_sites()
    
    # 1. Trigger script manually every now and then
    # 2. Cron job
    # 3. scipt running in background with while True
    #while True:
    #    block_websites() 
    #    time.sleep(5)



#127.0.0.1 www.instagram.com
#127.0.0.1 instagram.com
#127.0.0.1 www.facebook.com
#127.0.0.1 facebook.com