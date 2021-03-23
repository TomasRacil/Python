import psycopg2

def Uloz(data):
    #přihlašovací údaje k PostgreSQL
    DB_NAME = "awojxbex"
    DB_USER = "awojxbex"
    DB_PASS = "vKrGWYMhWYCYJTbb8lGzM9vL-PX7V4xa"
    DB_HOST = "ziggy.db.elephantsql.com"
    DB_PORT = "5432"
    
    #připojení k databázi PostgreSql 
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print("Database connected successfully")

    database = data['data']
    cur = conn.cursor()

    #Zde začíná modifikovaný kód
    cur.execute("SELECT * FROM okresy ORDER BY id DESC LIMIT 1;")
    last_id_database =int(cur.fetchone()[0])
    last_id_api = len(database)
    
    if last_id_database == last_id_api:
        pass
    else:
        for i in range(last_id_database+1,last_id_api):
            info = database[i]  
            datum = info['datum']
            nakazeni = info['kumulovany_pocet_nakazenych']
            vyleceni = info['kumulovany_pocet_vylecenych']
            umrti = info['kumulovany_pocet_umrti']
            test = info['kumulovany_pocet_provedenych_testu']
            atest = info['kumulovany_pocet_provedenych_ag_testu']
            cur = conn.cursor()
        
            #uložení nových dat do databáze PostgreSQL
            postgres_insert_query = "INSERT INTO Okresy (ID, DATUM, POCET_NAKAZENYCH, POCET_VYLECENYCH, POCET_UMRTI, POCET_TESTU, POCET_ATESTU) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            record_to_insert = (i, datum, nakazeni, vyleceni, umrti, test, atest)
            cur.execute( postgres_insert_query, record_to_insert)
            conn.commit()
