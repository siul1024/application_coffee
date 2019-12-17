import inspect
from mysql.connector import Error
from dao.abs_dao import Dao

select_sql = "SELECT no, sale_price, addTax, supply_price, marginPrice FROM sale_detail"
order_by = "proc_saledetail_orderby"


class SaleDetailDao(Dao):
    def select_table(self):
        print("\n______ {}:{} ______".format(inspect.stack()[0][3], "sale_detail"))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(select_sql)
            res = []
            [res.append(row) for row in self.iter_row(cursor, 5)]
            return res
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def order_by_select(self, order):
        print("\n______ {}:{} ______".format(inspect.stack()[0][3], "sale_detail"))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            args = [order, ]
            cursor.callproc(order_by, args)
            res = []
            [res.append(row) for row in self.iter_row_join(cursor)]
            return res
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def delete_table(self, **kwargs):
        pass

    def update_table(self, **kwargs):
        pass

    def insert_table(self, **kwargs):
        pass