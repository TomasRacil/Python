from sys import platform
from tkinter import *

#control the OS to determine the hostsFile
if platform=="linux":
    print("To je Linux OS") 
    hostsFile='/etc/hosts'  
elif platform=="win32":
    print("To je Windows OS")
    hostsFile='C:\Windows\System32\drivers\etc\hosts'


#ip local host
ip_local = "127.0.0.1" 


#Funkce Blokovani
def Blocker(Websites,rooot):
    """
    Function : takes the list of websites you want to block, combine with 127.0.0.1 and then write to file hosts.
               we open file hosts and read it. If that website not here, so program will add the website to file.
                                               else, program shows the Label "already block"
    args:
      Websites(type: tkinter.TEXT): list of websites you have put in
      rooot(type: tkinter.Tk): tkinter display
    """
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (hostsFile,'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
                if website in file_content:
                    Label(rooot, text = 'Already Blocked' ,bg = 'red', font = 'arial 12 bold').place(x=290,y=120)
                    Button(rooot,text="exit",command=rooot.quit).place(x=290,y =320)
                    
                else:
                    host_file.write(ip_local + " " + website + '\n')
                    Label(rooot, text = "Blocked",bg = 'red', font = 'arial 12 bold').place(x=290,y =120)
                    #Button(rooot,text="exit",command=rooot.quit).pack(side=BOTTOM)
                    Button(rooot,text="exit",command=rooot.quit).place(x=290,y =320)


#Funkce ODblokovani
def UnBlocker(WebsitesUn,rooot):
    """
    Function : takes the list of websites you want to Unblock, find them in file Hosts and delete them.
               At first, we open file hosts and read it.and then if the website is already in file, program will rewrite the file 
                 but not write the unblocked file. If the website is not in the hosts file, program will show "Not exit this file in blocked List"
                                               
    args:
      WebsitesUn(type: tkinter.TEXT): list of websites you have put in
      rooot(type: tkinter.Tk): tkinter display
    """
    websiteUn_lists = WebsitesUn.get(1.0,END)
    Removedwebsites=list(websiteUn_lists.split(","))
    with open ( hostsFile,'r+') as host_fileUn:
        file_content = host_fileUn.read() 
        for websiteUn in Removedwebsites:      
            if websiteUn in file_content:
                with open ( hostsFile,'r+') as host_fileUn:
                    lines = host_fileUn.readlines()
                    host_fileUn.seek(0)
                    for line in lines:
                        if not any(site in line for site in Removedwebsites):
                            host_fileUn.write(line)
                # removing hostnmes from host file
                    host_fileUn.truncate()
                    Label(rooot, text = 'Remove successfully' ,bg = 'red', font = 'arial 12 bold').place(x=280,y=250)
                   # Button(rooot,text="exit",command=rooot.quit).pack(side=BOTTOM)
                    Button(rooot,text="exit",command=rooot.quit).place(x=290,y =320)
               
                    
            else:
                Label(rooot, text = "Not exit this file in blocked List",bg = 'red', font = 'arial 12 bold').place(x=280,y =250)
                Button(rooot,text="exit",command=rooot.quit).place(x=290,y =320)

