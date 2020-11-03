# coding=utf-8
import pymysql
from Log import log

log = log.MyLog()


class MysqlCURD:
    def __init__(self, host, user, password, database, port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def connect(self):
        try:
            return pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                charset=self.charset
            )
        except Exception as e:
            log.error("failed to connect to database: %s" % e)
            return None

    def mysql_r(self, sql, column=None):
        rows = []
        conn = self.connect()
        cur = conn.cursor()
        try:
            if conn:
                cur.execute(sql)
                rows = cur.fetchall()
        except Exception as e:
            log.error("query failed: %s" % e)
        finally:
            conn.close()
        if not column:
            return rows
        else:
            value = rows[0][0]
            return value

    def mysql_cud(self, sql, have_semicolon=0):
        sign = False
        conn = self.connect()
        cur = conn.cursor()
        try:
            if conn:
                if have_semicolon == 0:
                    sql_list = sql.split(';')[:-1]
                    for i in sql_list:
                        cur.execute(i)
                        conn.commit()
                else:
                    cur.execute(sql)
                    conn.commit()
                sign = True
        except Exception as e:
            log.error("modify failed: %s" % e)
            conn.rollback()
        finally:
            conn.close()
        return sign

    def mysql_ep(self, procedure_name, parameters_list):
        sign = False
        conn = self.connect()
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            if conn:
                cur.callproc(
                    procedure_name,
                    args=parameters_list
                )
                conn.commit()
                sign = True
        except Exception as e:
            log.error("execute procedure failed: %s" % e)
        finally:
            conn.close()
        return sign
