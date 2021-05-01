import mysql.connector
from mysql.connector import errorcode


class Dao:
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'dico_fr_kb',
        'raise_on_warnings': True
    }
    connection = None
    source = 'dico_fr_chaoui'
    insert_sql = 'INSERT INTO dico_fr_chaoui(Mot, Definition) VALUES(%s, %s)'

    def __init__(self):
        if Dao.connection is None:
            self.connect_to_db()

    @staticmethod
    def connect_to_db():
        try:
            Dao.connection = mysql.connector.connect(**Dao.config)
            print('connection success!')
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('connection error (ER_ACCESS_DENIED_ERROR) : {}'.format(error.msg))
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print('connection error (ER_BAD_DB_ERROR) : {}'.format(error.msg))
            else:
                print(error.msg)

    def insert(self, mot, definition):
        cursor = Dao.connection.cursor()
        insert_data = (mot, definition)

        try:
            cursor.execute(Dao.insert_sql, insert_data)
            Dao.connection.commit()
        except:
            print('{} not inserted'.format(mot))
        cursor.close()

    def select(self):
        cursor = Dao.connection.cursor()
        cursor.execute('SELECT * FROM {}'.format(Dao.source), [])
        items = cursor.fetchall()
        cursor.close()
        return items

    @staticmethod
    def close():
        Dao.connection.close()
        Dao.connection = None
