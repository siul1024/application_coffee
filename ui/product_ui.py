from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from dao.product_dao import ProductDao
from ui import abs_ui
from ui.abs_ui import MyUi


class UiProduct(MyUi):
    def __init__(self):
        super().__init__()
        self.TB = ProductDao()
        self.ui = uic.loadUi("ui/product.ui")
        self.ui.setWindowTitle("Product Management")
        self.ui.tbl_widget.setColumnCount(2)
        self.table = abs_ui.create_table(table=self.ui.tbl_widget, data=['code', 'name'])
        # self.ui.show()
        self.ui.rb_select.clicked.connect(self.select_service)
        self.ui.rb_delete.clicked.connect(self.delete_service)
        self.ui.rb_update.clicked.connect(self.update_service)
        self.ui.rb_insert.clicked.connect(self.insert_service)
        self.table.itemSelectionChanged.connect(self.set_text_form_table)
        self.ui.btn_init.clicked.connect(self.init_item)
        self.load_data()

    def delete_service(self):
        self.ui.le_code.setEnabled(True)
        self.ui.le_name.setEnabled(False)
        self.ui.btn_apply.clicked.connect(self.__delete)
        self.load_data()

    def update_service(self):
        self.ui.le_code.setEnabled(True)
        self.ui.le_name.setEnabled(True)
        self.ui.btn_apply.clicked.connect(self.__update)
        self.load_data()

    def insert_service(self):
        self.ui.le_code.setEnabled(True)
        self.ui.le_name.setEnabled(True)

        self.ui.btn_apply.clicked.connect(self.__insert)
        self.load_data()

    def select_service(self):
        self.ui.le_code.setEnabled(True)
        self.ui.le_name.setEnabled(False)
        self.ui.btn_apply.clicked.connect(lambda stat, le_code=self.ui.le_code: self.load_data(stat, le_code))

    def create_item(self, code, name):
        icode = QTableWidgetItem(code)
        icode.setTextAlignment(Qt.AlignCenter)
        iname = QTableWidgetItem(name)
        iname.setTextAlignment(Qt.AlignCenter)
        return icode, iname

    def set_text_form_table(self):
        selectcheck = self.table.selectedRanges()
        if len(selectcheck) != 0:
            selectIdxs = self.table.selectedIndexes()[0]
            code = self.table.item(selectIdxs.row(), 0).text()
            name = self.table.item(selectIdxs.row(), 1).text()
            self.ui.le_code.setText(code)
            self.ui.le_name.setText(name)

    def load_data(self, stat=None, le_code=None):
        if le_code is None:
            res = self.TB.select_table()
        else:
            if len(le_code.text()) != 0:
                res = self.TB.select_table(le_code.text())
            else:
                res = self.TB.select_table()
        self.table.setRowCount(0)
        for idx, (code, name) in enumerate(res):
            item_code, item_name = self.create_item(code, name)
            nextIdx = self.table.rowCount()
            self.table.insertRow(nextIdx)
            self.table.setItem(nextIdx, 0, item_code)
            self.table.setItem(nextIdx, 1, item_name)

    def init_item(self):
        self.ui.le_code.clear()
        self.ui.le_name.clear()
        self.table.clearSelection()

    def __insert(self):
        self.TB.insert_table(self.ui.le_code.text(), self.ui.le_name.text())
        self.load_data()

    def __update(self):
        self.TB.update_table(self.ui.le_name.text(), self.ui.le_code.text())
        self.load_data()

    def __delete(self):
        self.TB.delete_table(self.ui.le_code.text())
        self.load_data()
