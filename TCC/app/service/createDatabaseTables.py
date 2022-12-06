
import sqlite3

def createTables():
    # Connecting to sqlite
    # connection object
    connection_obj = sqlite3.connect('../database/DBSR4001.db')
    
    # cursor object
    cursor_obj = connection_obj.cursor()
    
    # Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS trafficHover")
    
    # Creating table
    table = """ CREATE TABLE trafficHover (
                id INTEGER PRIMARY KEY,
                id_semaforo int,
                carro_esperando  text,
                date date
            ); """
    
    table2 = """ CREATE TABLE carTraffic (
                id INTEGER PRIMARY KEY,
                id_semaforo int,
                quantidade_total  text,
                dia_semana text,
                data text,
                hora text
            ); """
    
    table3 = = """ CREATE TABLE timeTable (
                id INTEGER PRIMARY KEY,
                id_semaforo text,
                diaDaSemana text,
                horaInicial int,
                tempoVerde  int,
                tempoVermelho int,
                numAtualizacao int
            );"""
            
    cursor_obj.execute(table)
    cursor_obj.execute(table2)
    cursor_obj.execute(table3)

    print("Tables is Ready")
    
    # Close the connection
    connection_obj.close()

if __name__ == '__main__':
    createTables()
