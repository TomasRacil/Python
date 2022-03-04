#Podprogram pro instalaci/import potřebných knihoven
def install_and_import(knihovna):
    import importlib
    try:
        importlib.import_module(knihovna)
    except ImportError:
        import pip
        pip.main(['install', knihovna])
    finally:
        globals()[knihovna] = importlib.import_module(knihovna)
        
#Spuštění podprogramu pro požadované knihovny 
install_and_import("lzma")
install_and_import("glob")
install_and_import("os")
install_and_import("patoolib")
install_and_import("json")
install_and_import("sys")
install_and_import("mysql")
install_and_import("mysql.connector")
install_and_import("getpass")
install_and_import("instaloader")


#Definování cesta jako cesta do místa umístění scriptu
cesta=os.getcwd()

#Nastavení vstupu USER
print("Pokud je profil soukromý, zadejte své přihlašovací jméno, pokud je veřejný, stikněte ENTER.")
USER = input("Zadejte své uživatelské jméno:")

#Podmínka pro použití vlastního/defaultního IG profilu
if len(USER)==0:
    USER = "getimag"
    PASSWORD = "admin56789"
    Name = "{target}_{mediaid}" #Definování pojmenování stažených souborů target="jméno uživatele" mediaid= "id obrázku"
    
else:
    PASSWORD = getpass.getpass("Zadejte své heslo:") #Použití getpass pro skrytí hesla v konzoli
    Name = "{target}_{mediaid}"

#Začátek podprogramu pro stahování a zadávání do databáze(běží ve smyčce)  
def function():
    #Zadání uživatelského profilu, který chceme stáhnout
    PROFILE = input("Zadejte uživatelské jméno profilu, který chcete stáhnout:")
    #Definování proměné DIR jako cestu do složky kde je script/data/"složka se jménem uživatele". DIR následné požijeme k definování cesty pro stažené soubory 
    DIR = cesta+"/data/"+PROFILE
    #Definování instaloderu a jeho parametrů
    L = instaloader.Instaloader(dirname_pattern=DIR, filename_pattern=Name)
    #Přihlášení do instagramu pomocí zadaných/defaultních údajů
    L.login(USER, PASSWORD)
    #Přihlášení do databáze
    mydb = mysql.connector.connect(
      host = "localhost",
      user= "root",
      passwd = "admin",
      database = "instagram"
  )

    #Definování cursoru
    my_cursor = mydb.cursor()


    #Stažení jednotlivých postů pomocí cyklu a knihovny instaloader 
    profile = instaloader.Profile.from_username(L.context, PROFILE)
    for post in profile.get_posts():
        L.download_post(post, target=profile.username)
        filename = profile.username + '/' + L.format_filename(post, target=profile.username)

    #Definování pomocných proměných
    i=0
    s=len(PROFILE)+1
    e=len(PROFILE)+20
    
    #Otevření cesty k datům
    os.chdir(cesta+"/data/"+PROFILE)

    #Cyklus pro vyhledání, extrahování ".xz" souborů do ".json" a zadání dat do tabulky post
    for file_xz in glob.glob("*.xz"):
        i=i+1 #Pomocná proměná pořítající počet postů
        patoolib.extract_archive(cesta+"/data/"+PROFILE+"/"+PROFILE+"_"+file_xz[s:e]+".json.xz", outdir=cesta+"/data/"+PROFILE+"/") #extrahování .xz souborů pomocí knihovny patoolib
        #Otevření a načtení json dat
        f = open(cesta+"/data/"+PROFILE+"/"+PROFILE+"_"+file_xz[s:e]+".json.")
        data = json.load(f)
        #Výběr a zápis požadovaných dat do tabulky post
        popisek = (cesta+"/data/"+PROFILE+"/"+PROFILE+"_"+file_xz[s:e]+".txt.") #popisek je vložen pouze jako cesta k .txt souboru, protože když jsem chtěl vložit přímo text, tak byl problém s různými emotikony a znaky, kterých je na instagramu poměrně hodně
        id_post = (data["node"]["id"])
        display_url= (data["node"]["display_url"])
        accessibility_caption= (data["node"]["accessibility_caption"])
        edge_liked_by= (data["node"]["iphone_struct"]["like_count"])
        followers= (data["node"]["owner"]["edge_followed_by"]["count"])
        followed= (data["node"]["owner"]["edge_follow"]["count"])
        zapis1 = "INSERT INTO posts(ID, id_post, posted_by, display_url, accessibility_caption, edge_liked_by, popisek) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        record1 = (0, id_post, PROFILE ,display_url,accessibility_caption, edge_liked_by, popisek)
        my_cursor.execute(zapis1, record1)
        mydb.commit()
    



    #Zápis požadovaných dat do tabulky users
    zapis2 = "INSERT INTO users(ID, username, numberofpost, followers, followed) VALUES(%s, %s, %s, %s, %s)"
    record2 = (0 ,PROFILE, i, followers, followed)
    my_cursor.execute(zapis2, record2)
    mydb.commit()

    
    var = "_"
    if var == "_":
        
        print ("Stahování dokončeno")
while True:
    function()    



