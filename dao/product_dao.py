import inspect
from mysql.connector import Error
from dao.abs_dao import Dao

insert_sql = "INSERT INTO product VALUES(%s, %s)"
update_sql = "UPDATE product SET name=%s WHERE code=%s"
delete_sql = "DELETE FROM product WHERE code=%s"
select_sql = "SELECT code, name FROM product"
select_sql_where = select_sql + " WHERE code=%s"


class ProductDao(Dao):
    def delete_table(self, code=None):
        print("\n______ {}:{} ______".format(inspect.stack()[0][3], "product"))
        args = (code, )
        try:
            super().do_query(query=delete_sql, kargs=args)
            return True
        except Error:
            return False

    def update_table(self, name=None, code=None):
        print("\n______ {}:{} ______".format(inspect.stack()[0][3], "product"))
        args = (name, code)
        try:
            super().do_query(query=update_sql, kargs=args)
            return True
        except Error:
            return False

    def insert_table(self, code=None, name=None):
        print("\n______ {}:{} ______".format(inspect.stack()[0][3], "product"))
        args = (code, name)
        try:
            super().do_query(query=insert_sql, kargs=args)
            return True
        except Error:
            return False

    def select_table(self, code=None):
        print("\n______ {}:{} ______".format(inspect.stack()[0][3], "product"))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(select_sql) if code is None else cursor.execute(select_sql_where, (code,))
            res = []
            [res.append(row) for row in self.iter_row(cursor, 5)]
            return res
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()