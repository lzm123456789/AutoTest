# coding=utf-8
import pymysql
from Log import log

log = log.MyLog


class MysqlCURD:
    """连接mysql进行增删改查操作"""

    def __init__(self, host, user, password, database, port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def connect(self):
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset=self.charset)
            return conn
        except Exception as e:
            log.error("failed to connect to database: %s" % e)
            return None

    def mysql_r(self, sql, column=None):
        """查询"""

        rows = value = []
        conn = self.connect()
        try:
            if conn:
                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
        except Exception as e:
            log.error("query failed: %s" % e)
        finally:
            conn.close()
        # 当sql没有指定具体查询字段的时候
        if not column:
            return rows
        # 当sql指定了具体查询字段的时候
        else:
            # 当查询不为空的时候
            if rows:
                value = rows[0][0]
            # 当查询为空的时候
            else:
                log.error("the query result is empty !")
            return value

    def mysql_cud(self, sql, have_semicolon=0):
        """插入、修改、删除"""

        sign = False
        conn = self.connect()
        try:
            if conn:
                cur = conn.cursor()
                # 当单条sql自身不包含分号的时候
                if have_semicolon == 0:
                    # 把多条sql语句分割开，然后逐条执行
                    sqllist = sql.split(';')[:-1]
                    for i in sqllist:
                        cur.execute(i)
                        conn.commit()
                # 当单条sql自身包含分号的时候
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
        """
        执行存储过程
        :param procedure_name: 存储过程名
        :param parameters_list: 参数列表
        :return:
        """

        sign = False
        conn = self.connect()
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            if conn:
                cur.callproc(procedure_name, args=parameters_list)
                conn.commit()
                sign = True
        except Exception as e:
            log.error("execute procedure failed: %s" % e)
        finally:
            cur.close()
            conn.close()
        return sign
