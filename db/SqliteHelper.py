import sqlite3


class SqliteHelper:
    table_name = 'proxys'

    def __init__(self):
        self.database = sqlite3.connect('ip_pool.db')
        self.cursor = self.database.cursor()
        #创建表结构
        self.create_table()

    def create_table(self):
        self.cursor.execute("create TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, ip VARCHAR(16) NOT NULL,"
                            "port INTEGER NOT NULL, types INTEGER NOT NULL, protocol INTEGER NOT NULL DEFAULT 0,"
                            "country VARCHAR (20) NOT NULL, area VARCHAR (20) NOT NULL,"
                            "updatetime TimeStamp NOT NULL DEFAULT (datetime('now','localtime')),"
                            "speed DECIMAL(3,2) NOT NULL DEFAULT 100)" % self.table_name)

        self.database.commit()

    def select(self, condition, count):
        sql = 'select distinct ip, port from %s where %s order by speed asc %s' % (self.table_name, condition, count)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def select_all(self):
        sql = 'select distinct ip, port from %s order by speed asc' % self.table_name
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def select_one(self, condition):
        sql = 'select distinct ip, port from %s where %s order by speed asc' % (self.table_name, condition)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def select_count(self):
        sql = 'select count(distinct ip) from %s' % self.table_name
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def insert(self, value):
        proxy = [value['ip'], value['port', value['type'], value['protocol'], value['country'], value['area'], value['speed']]]
        sql = 'insert into %s (ip, port, types, protocol, country, area, speed) values (?,?,?,?,?,?,?)' % self.table_name
        self.cursor.execute(sql)

    def delete(self, condition):
        sql = 'delete from %s where %s' % (self.table_name, condition)

    def batch_insert(self,values):
        for value in values:
            if value is not None:
                self.insert(self.table_name, value)
        self.database.commit()

    def update(self, condition):
        sql = 'update %s %s' % (self.table_name, condition)
        self.cursor.execute(sql)
        self.database.commit()

    def commit(self):
        self.database.commit()

    def close(self):
        self.cursor.close()
        self.database.close()


if __name__ == '__main__':
    helper = SqliteHelper()
    print(helper.select_count()[0])