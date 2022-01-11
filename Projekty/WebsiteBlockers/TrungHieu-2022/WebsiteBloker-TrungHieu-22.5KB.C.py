from tkinter import Tk, Label, Text, Button, CENTER, BOTTOM, WORD, END
from sys import platform

#zkontrolovat jaky je system
if platform=="linux": 
    print("To je Linux OS") 
    hostsFile='/etc/hosts'  
elif platform=="win32":
    print("To je Windows OS")
    hostsFile='C:\Windows\System32\drivers\etc\hosts'

#Vytvorim tkinter
root = Tk()
root.title("HIEU- Website Blocker")
root.geometry('600x400')  # dimension y*x
root.resizable(height=True, width=True)
root.minsize(height=300, width=300)

Label(root, text='WEBSITE BLOCKER', justify=CENTER,
      fg="red", font='arial 15 bold').pack()  #Hlavni Nazev


ip_local = "127.0.0.1"  # ip local host

Label(root, text='Enter Website :', font='arial 14 bold').place(x=5, y=65)
Websites = Text(root, font='arial 10', height='2',
                width='40', wrap=WORD, padx=5, pady=5) #Zadej nazev website, abyste blokoval 
Websites.place(x=150, y=60)


Label(root, text='Unblock Website :', font='arial 14 bold').place(x=5, y=195)
WebsitesUn = Text(root, font='arial 10', height='2',
                  width='40', wrap=WORD, padx=5, pady=5)  #Zadej nazev website, abyste unblokoval
WebsitesUn.place(x=180, y=190)

#Funkce , ktera pomuze blokovat
def Blocker():
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))
    with open(hostsFile, 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text='Already Blocked', bg='red',
                      font='arial 12 bold').place(x=290, y=120)
                Button(root, text="exit", command=root.quit).pack(side=BOTTOM)
                pass
            else:
                host_file.write(ip_local + " " + website + '\n')
                Label(root, text="Blocked", bg='red',
                      font='arial 12 bold').place(x=290, y=120)
                Button(root, text="exit", command=root.quit).pack(side=BOTTOM)

#Funkce , ktera unblokovat
def UnBlocker():
    websiteUn_lists = WebsitesUn.get(1.0, END)
    Removedwebsites = list(websiteUn_lists.split(","))
    with open(hostsFile, 'r+') as host_fileUn:
        file_content = host_fileUn.read()
        for websiteUn in Removedwebsites:
            if websiteUn in file_content:
                with open(hostsFile, 'r+') as host_fileUn:
                    lines = host_fileUn.readlines()
                    host_fileUn.seek(0)
                    for line in lines:
                        if not any(site in line for site in Removedwebsites):
                            host_fileUn.write(line)
                # removing hostnmes from host file
                    host_fileUn.truncate()

                    Label(root, text='Remove successfully', bg='red',
                          font='arial 12 bold').place(x=280, y=250)
                    Button(root, text="exit", command=root.quit).pack(
                        side=BOTTOM)
                pass

            else:
                Label(root, text="Not exit this file in blocked List",
                      bg='red', font='arial 12 bold').place(x=280, y=250)
                Button(root, text="exit", command=root.quit).pack(side=BOTTOM)


#click Blokovani
Button(root, text='Block', font='arial 12 bold', pady=5, command=Blocker,
       width=6, bg='royal blue1', activebackground='red').place(x=200, y=110)

#click Unblokovani
Button(root, text='UnBlock', font='arial 12 bold', pady=5, command=UnBlocker,
       width=6, bg='royal blue1', activebackground='red').place(x=200, y=240)


def MakeCenter(rooot):  # Move tkinter to center of screen
    rooot.update_idletasks()
    width = rooot.winfo_width()
    height = rooot.winfo_height()
    x = (rooot.winfo_screenwidth()//2)-(width//2)
    y = (rooot.winfo_screenheight()//2)-(height//2)
    rooot.geometry(f'{width}x{height}+{x}+{y}')


MakeCenter(root)
root.mainloop()
