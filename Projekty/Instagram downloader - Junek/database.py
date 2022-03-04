#podprogram pro instalaci/import knihoven
def install_and_import(knihovna): 
    import importlib
    try:
        importlib.import_module(knihovna)
    except ImportError:
        import pip
        pip.main(['install', knihovna])
    finally:
        globals()[knihovna] = importlib.import_module(knihovna)
#spuštění podprogramu pro požadované knihovny       
install_and_import("mysql") 
install_and_import("mysql.connector")


#Vložení údajů pro přihlášení do MySQL
host = input("Zadejte host:") #localhost
user = input("Zadejte uživatelské jméno:") #root
passwd = input("Zadejte heslo:") #admin
#Přihlášení do MySQL
mydb = mysql.connector.connect(
  host = host,
  user= user,
  passwd = passwd,
  
  )


#Definování cursoru
my_cursor = mydb.cursor()
#Vytvoření databáze "instagram"
my_cursor.execute("CREATE DATABASE instagram")
#Přihlášení do databáze
mydb = mysql.connector.connect(
  host = host,
  user= user,
  passwd = passwd,
  database = "instagram"
  )
my_cursor = mydb.cursor()
#Vytvoření tabulek v databázi "instagram"
my_cursor.execute("CREATE TABLE users (ID INTEGER AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), numberofpost INTEGER,  followers INTEGER, followed INTEGER)")
my_cursor.execute("CREATE TABLE posts (ID INTEGER AUTO_INCREMENT PRIMARY KEY, id_post VARCHAR(255), posted_by VARCHAR(255), display_url VARCHAR(1024), accessibility_caption VARCHAR(255), edge_liked_by INTEGER, popisek VARCHAR(1024))")


print("Databáze vytvořena")
e= input("Pro ukončení stiskněte cokoliv")
