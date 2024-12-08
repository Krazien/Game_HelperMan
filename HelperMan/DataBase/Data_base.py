import sqlite3


class DataBase:
    def __init__(self, file):  # init - конструктор
        self.con = sqlite3.connect(file)  # con - connection - соединение
        self.cur = self.con.cursor()  # cur - cursor - обратная связь
        self.create_table('score_players')

    def create_table(self, table_name):
        que_create = f'''
        CREATE TABLE IF NOT EXIST {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score INTEGER,
        )
        '''
        self.cur.execute(que_create)
        self.con.commit()

    def get(self, query='SELECT * FROM score_players'):
        return self.cur.execute(query).fetchall()

    def insert(self, name, score):
        que_insert = f'''INSERT INTO score_players (name, score)
                        VALUES ('{name}', '{score}')
                        '''
        self.cur.execute(que_insert)
        self.con.commit()

    def __del__(self):  # dell - диструктор
        self.con.close()
