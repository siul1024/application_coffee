from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from dao.sale_dao import SaleDao
from ui import abs_ui
from ui.abs_ui import MyUi


class UiSale(MyUi):
    def __init__(self):
        super().__init__()
        self.TB = SaleDao()
        self.ui = uic.loadUi("ui/sale.ui")
        self.ui.setWindowTitle("Sale Management")
        self.ui.tbl_widget.setColumnCount(5)
        self.table = abs_ui.create_table(table=self.ui.tbl_widget, data=['no', 'code', 'price(￦)', 'saleCnt', 'marginRate(%)'])
        # self.ui.show()
        self.ui.rb_select.clicked.connect(self.select_service)
        self.ui.rb_delete.clicked.connect(self.delete_service)
        self.ui.rb_update.clicked.connect(self.update_service)
        self.ui.rb_insert.clicked.connect(self.insert_service)
        self.table.itemSelectionChanged.connect(self.set_text_form_table)
        self.ui.btn_init.clicked.connect(self.init_item)
        self.load_data()

    def delete_service(self):
        self.ui.le_no.setEnabled(True)
        self.ui.le_code.setEnabled(False)
        self.ui.le_price.setEnabled(False)
        self.ui.le_salecnt.setEnabled(False)
        self.ui.le_marginrate.setEnabled(False)
        self.ui.btn_apply.disconnect()
        self.ui.btn_apply.clicked.connect(self.__delete)
        self.load_data()

    def update_service(self):
        self.ui.le_no.setEnabled(True)
        self.ui.le_code.setEnabled(True)
        self.ui.le_price.setEnabled(True)
        self.ui.le_salecnt.setEnabled(True)
        self.ui.le_marginrate.setEnabled(True)
        self.ui.btn_apply.disconnect()
        self.ui.btn_apply.clicked.connect(self.__update)
        self.load_data()

    def insert_service(self):
        self.ui.le_no.setEnabled(False)
        self.ui.le_code.setEnabled(True)
        self.ui.le_price.setEnabled(True)
        self.ui.le_salecnt.setEnabled(True)
        self.ui.le_marginrate.setEnabled(True)
        self.ui.btn_apply.disconnect()
        self.ui.btn_apply.clicked.connect(self.__insert)
        self.load_data()

    def select_service(self):
        self.ui.le_no.setEnabled(True)
        self.ui.le_code.setEnabled(False)
        self.ui.le_price.setEnabled(False)
        self.ui.le_salecnt.setEnabled(False)
        self.ui.le_marginrate.setEnabled(False)
        self.ui.btn_apply.disconnect()
        self.ui.btn_apply.clicked.connect(lambda stat, le_no=self.ui.le_no: self.load_data(stat, le_no))

    def create_item(self, no, code, price, salecnt, marginrate):
        ino = QTableWidgetItem(no)
        ino.setTextAlignment(Qt.AlignCenter)
        ino.setData(Qt.DisplayRole, no)

        icode = QTableWidgetItem(code)
        icode.setTextAlignment(Qt.AlignCenter)
        icode.setData(Qt.DisplayRole, code)

        iprice = QTableWidgetItem(price)
        iprice.setTextAlignment(Qt.AlignRight)
        iprice.setData(Qt.DisplayRole, format(int(price), ',d'))

        isalecnt = QTableWidgetItem(salecnt)
        isalecnt.setTextAlignment(Qt.AlignRight)
        isalecnt.setData(Qt.DisplayRole, format(int(salecnt), ',d'))

        imarginrate = QTableWidgetItem(marginrate)
        imarginrate.setTextAlignment(Qt.AlignRight)
        imarginrate.setData(Qt.DisplayRole, format(int(marginrate), ',d'))
        return ino, icode, iprice, isalecnt, imarginrate

    def set_text_form_table(self):
        selectcheck = self.table.selectedRanges()
        if len(selectcheck) != 0:
            selectIdxs = self.table.selectedIndexes()[0]
            no = self.table.item(selectIdxs.row(), 0).text().replace(',', '')
            code = self.table.item(selectIdxs.row(), 1).text()
            price = self.table.item(selectIdxs.row(), 2).text().replace(',', '')
            salecnt = self.table.item(selectIdxs.row(), 3).text().replace(',', '')
            marginrate = self.table.item(selectIdxs.row(), 4).text().replace(',', '')
            self.ui.le_no.setText(no)
            self.ui.le_code.setText(code)
            self.ui.le_price.setText(price)
            self.ui.le_salecnt.setText(salecnt)
            self.ui.le_marginrate.setText(marginrate)

    def load_data(self, stat=None, le_no=None):
        if le_no is None:
            res = self.TB.select_table()
        else:
            if len(le_no.text()) == 0:
                res = self.TB.select_table()
            else:
                res = self.TB.select_table(le_no.text())
        self.table.setRowCount(0)
        for idx, (no, code, price, salecnt, marginrate) in enumerate(res):
            item_no, item_code, item_price, item_salecnt, item_marginrate \
                = self.create_item(no, code, price, salecnt, marginrate)
            nextIdx = self.table.rowCount()
            self.table.insertRow(nextIdx)
            self.table.setItem(nextIdx, 0, item_no)
            self.table.setItem(nextIdx, 1, item_code)
            self.table.setItem(nextIdx, 2, item_price)
            self.table.setItem(nextIdx, 3, item_salecnt)
            self.table.setItem(nextIdx, 4, item_marginrate)

    def init_item(self):
        self.ui.le_no.clear()
        self.ui.le_code.clear()
        self.ui.le_price.clear()
        self.ui.le_salecnt.clear()
        self.ui.le_marginrate.clear()
        self.table.clearSelection()

    def __insert(self):
        self.TB.insert_table(self.ui.le_code.text(), self.ui.le_price.text(), self.ui.le_salecnt.text(), self.ui.le_marginrate.text())
        self.load_data()

    def __update(self):
        self.TB.update_table(self.ui.le_code.text(), self.ui.le_price.text(), self.ui.le_salecnt.text(), self.ui.le_marginrate.text(), self.ui.le_no.text())
        self.load_data()

    def __delete(self):
        self.TB.delete_table(self.ui.le_no.text())
        self.load_data()


