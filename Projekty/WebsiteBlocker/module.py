import time
import os
from datetime import datetime as dt

""" Arg: none, Return: blocked sites"""
def get_sites():
# websites That we want to block from txt 
    blokace = os.path.dirname(os.path.realpath(__file__))+"/blokace.txt"
    soubor = open(blokace,"r")
    for radek in soubor:
        website_list=[radek.strip() for radek in open(blokace,"r")]
    sites_to_block=[]
    for site in website_list:
        sites_to_block.append(site)
        sites_to_block.append(site[4:])
    return sites_to_block

""" Arg: sites to block and hosts path, Return: nothing just edit host file """
def blocks_sites(sites_to_block,hosts_path):
    while True:
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
        time.sleep(5)