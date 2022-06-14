def databasecreate():
    """
    Vytvoří požadovanou databázi
    """
    import os

    def install_and_import(knihovna):
        """
        Nainstaluje a naimportuje požadované knihovny
        Args: knihovna = "nazev_knihovny" (kterou chcete naimportovat
        """
        import importlib

        try:
            importlib.import_module(knihovna)
        except ImportError:
            import pip

            pip.main(["install", knihovna])
        finally:
            globals()[knihovna] = importlib.import_module(knihovna)

    install_and_import("importlib")
    install_and_import("getpass")
    install_and_import("mysql")
    install_and_import("mysql.connector")

    from main import hostid
    from main import userid
    from main import passwdid
    from main import databaseid
    import mysql

    # Přihlášení do MySQL
    mydb = mysql.connector.connect(host=hostid, user=userid, passwd=passwdid)

    # Definování cursoru
    my_cursor = mydb.cursor()
    # Vytvoření databáze "instagram"
    try:
        my_cursor.execute("CREATE DATABASE instagram")
    except:
        print("Databáze už byla vytvořena byla vytvořena.")
    # Přihlášení do databáze
    mydb = mysql.connector.connect(
        host=hostid, user=userid, passwd=passwdid, database=databaseid
    )
    my_cursor = mydb.cursor()
    # Vytvoření tabulek v databázi "instagram"
    try:
        my_cursor.execute(
            "CREATE TABLE users (ID INTEGER AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), numberofpost INTEGER,  followers INTEGER, followed INTEGER)"
        )
        my_cursor.execute(
            "CREATE TABLE posts (ID INTEGER AUTO_INCREMENT PRIMARY KEY, id_post VARCHAR(255), posted_by VARCHAR(255), display_url VARCHAR(1024), edge_liked_by INTEGER, popisek VARCHAR(1024))"
        )
        e = input("Pro ukončení stiskněte cokoliv")
    except:
        e = input("Pro ukončení stiskněte cokoliv")
