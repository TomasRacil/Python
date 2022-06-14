from database import databasecreate
from instadownload import instadownloadstart
import getpass



 
    
if __name__ == "__main__":
    databasecreate()
    instadownloadstart()
    
hostid = input("Zadejte host:") #localhost
userid = input("Zadejte uživatelské jméno:") #root
passwdid = getpass.getpass("Zadejte heslo:") #admin
databaseid = "instagram"

