from Moduly import *
import psycopg2

def main(): 
    #přihlašovací údaje k PostgreSQL
    DB_NAME = "awojxbex"
    DB_USER = "awojxbex"
    DB_PASS = "vKrGWYMhWYCYJTbb8lGzM9vL-PX7V4xa"
    DB_HOST = "ziggy.db.elephantsql.com"
    DB_PORT = "5432"

    #připojení k databázi PostgreSql 
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print("Database connected successfully")

    
    data = jsonGetInfo()


    database = data['data']
    cur = conn.cursor()

    #nejprve vymažeme staré údaje
    postgres_delete_query = """DELETE FROM Okresy"""
    cur.execute( postgres_delete_query)
    conn.commit()
    for i in range(0, len(database)):
        
        info = database[i]  
        datum = info['datum']
        nakazeni = info['kumulovany_pocet_nakazenych']
        vyleceni = info['kumulovany_pocet_vylecenych']
        umrti = info['kumulovany_pocet_umrti']
        test = info['kumulovany_pocet_provedenych_testu']
        atest = info['kumulovany_pocet_provedenych_ag_testu']
        cur = conn.cursor()
        
        #uložení nových dat do databáze PostgreSQL
        postgres_insert_query = """INSERT INTO Okresy (ID, DATUM, POCET_NAKAZENYCH, POCET_VYLECENYCH, POCET_UMRTI, POCET_TESTU, POCET_ATESTU) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (i, datum, nakazeni, vyleceni, umrti, test, atest)
        cur.execute( postgres_insert_query, record_to_insert)
        conn.commit()

if __name__ == '__main__':
	main()
