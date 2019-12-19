import inspect
from abc import ABCMeta, abstractmethod
from mysql.connector import Error
from db_connection.connection_pool import ConnectionPool


class Dao(metaclass=ABCMeta):
    def __init__(self):
        self.connection_pool = ConnectionPool.get_instance()

    @abstractmethod
    def delete_table(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def update_table(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def insert_table(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def select_table(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    def do_query(self, **kwargs):
        print("\n_______ {}() _______".format(inspect.stack()[0][3]))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            if kwargs['kargs'] is not None:
                cursor.execute(kwargs['query'], kwargs['kargs'])
            else:
                cursor.execute(kwargs['query'])
            conn.commit()
        except Error:
            raise
        finally:
            cursor.close()
            conn.close()

    def iter_row(self, cursor, size=5):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def iter_row_join(self, cursor):
        for result in cursor.stored_results():
            rows = result.fetchall()
            if not rows:
                break
            for row in rows:
                yield row
