import abc
from abc import ABCMeta, abstractmethod
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView, QWidget


def create_table(table=None, data=None):
    table.setHorizontalHeaderLabels(data)
    # 균일한 간격으로 재배치
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    # row 단위 선택
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    # 수정 불가능
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    return table


class MyUi(QWidget):
    __metaclass__ = abc.ABCMeta

    @abstractmethod
    def delete_service(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def update_service(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def insert_service(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def select_service(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def create_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method. return item")

    @abstractmethod
    def set_text_form_table(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def load_data(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def init_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")