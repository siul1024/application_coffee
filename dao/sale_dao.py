import inspect
from mysql.connector import Error
from dao.abs_dao import Dao

insert_sql = "INSERT INTO sale VALUES(NULL, %s, %s, %s, %s)"
update_sql = "UPDATE sale SET code=%s, price=%s, saleCnt=%s, marginRate=%s WHERE no=%s"
delete_sql = "DELETE FROM sale WHERE no=%s"
select_sql = "SELECT no, code, price, saleCnt, marginRate FROM sale"
select_sql_where = select_sql + " WHERE no=%s"


class SaleDao(Dao):
    def delete_table(self, no=None):
        print("\n______ {}:{} ______".format(inspect.stack()[0][3], "sale"))
        args = (no, )
        try:
            super().do_query(query=delete_sql, kargs=args)
            return True
        except Error:
            return False

    def update_table(self, code=None, price=None, salecnt=None, marginrate=None, no=None):
        print("\n______ {}:{} ______".format(inspect.stack()[0][3], "sale"))
        args = (code, price, salecnt, marginrate, no)
        try:
            super().do_query(query=update_sql, kargs=args)
            return True
        except Error:
            return False

    def insert_table(self, code=None, price=None, salecnt=None, marginrate=None):
        print("\n______ {}:{} ______".format(inspect.stack()[0][3], "sale"))
        args = (code, price, salecnt, marginrate)
        try:
            super().do_query(query=insert_sql, kargs=args)
            return True
        except Error:
            return False

    def select_table(self, no=None):
        print("\n______ {}:{} ______".format(inspect.stack()[0][3], "sale"))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(select_sql) if no is None else cursor.execute(select_sql_where, (no,))
            res = []
            [res.append(row) for row in self.iter_row(cursor, 5)]
            return res
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()