"""Run this script as root"""
import time
import os
from datetime import datetime as dt

"""localhost's IP"""
redirect = "127.0.0.1"

def get_sites():
    """websites That we want to block from blokace.txt file"""
    blokace = os.path.dirname(os.path.realpath(__file__))+"/blokace.txt"
    soubor = open(blokace,"r")
    """Create "sites_to_blocks": the variable type "list" in which all the websites blocker will be save"""
    for radek in soubor:
        website_list=[radek.strip() for radek in open(blokace,"r")]
    sites_to_block=[]
    for site in website_list:
        sites_to_block.append(site)
        sites_to_block.append(site[4:])
    return sites_to_block

def blocks_sites(sites_to_block,hosts_path):
    while True:
        """Condition: Time of your work from 8-16h everyday""" 
        if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,13): 
            print("Working hours...") 
            """Change the file "hosts"""
            with open(hosts_path, 'r+') as hostsfile: 
                hosts_content = hostsfile.read() 
                for site in sites_to_block: 
                    if site not in hosts_content: 
                        """mapping hostnames to your localhost IP address"""
                        hostsfile.write(redirect + " " + site + "\n") 
        else:
            """Not in time of your work so change the file "hosts" by clearing websites that we blocked""" 
            print("unblock sites")
            with open(hosts_path, 'r+') as hostsfile:
                lines = hostsfile.readlines()
                hostsfile.seek(0)
                for line in lines:
                    if not any(site in line for site in sites_to_block):
                        hostsfile.write(line)
                """removing hostnmes from host file"""
                hostsfile.truncate()
        time.sleep(5)
        #if __name__== ten kontrektni soubor, pokud je prvni a neni importovany, tak bude mit jmeno main
     """sudo python script.py"""
if __name__ == '__main__':
    """change hosts path according to your OS"""
    if os.name=='posix':
        hosts_path = r"/etc/hosts"
    elif os.name=='nt':
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    blocks_sites(get_sites(),hosts_path)