from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:

        with conn:

            cur = conn.cursor()
            cur.execute("SELECT * FROM wp_users")

            rows = cur.fetchall()

            for row in rows:
                print("{0} {1} {2}".format(row[0], row[1], row[2]))







        #conn.close()
        print('Connection closed.')

if __name__ == '__main__':
    connect()
