from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from dao.sale_detail_dao import SaleDetailDao
from ui import abs_ui
from ui.abs_ui import MyUi


class UiSaleDetail(MyUi):
    def __init__(self):
        super().__init__()
        self.TB = SaleDetailDao()
        self.ui = uic.loadUi("ui/sale_detail.ui")
        self.ui.setWindowTitle("Sale Detail")
        # self.ui.show()
        self.ui.btn_default.clicked.connect(self.select_service)
        self.ui.btn_order_sp.clicked.connect(lambda stat, x=True: self.tablejoin_service(stat, order=x))
        self.ui.btn_order_mp.clicked.connect(lambda stat, x=False: self.tablejoin_service(stat, order=x))

    def select_service(self):
        self.ui.tbl_widget.setColumnCount(5)
        abs_ui.create_table(table=self.ui.tbl_widget,
                            data=['no', 'sale_price(￦)', 'addTax(￦)', 'supply_price(￦)', 'margin_price(￦)'])
        self.ui.btn_default.setEnabled(False)
        self.ui.btn_order_sp.setEnabled(True)
        self.ui.btn_order_mp.setEnabled(True)
        self.load_data()

    def tablejoin_service(self, stat, order):
        self.ui.tbl_widget.setColumnCount(10)
        abs_ui.create_table(table=self.ui.tbl_widget,
                            data=['rank', 'code', 'name', 'price(￦)', 'saleCnt',
                                  'supply_price(￦)', 'addTax(￦)', 'sale_price(￦)', 'marginRate(%)', 'marginPrice(￦)'])
        # 마진액순 mp
        if order==False:
            self.ui.btn_default.setEnabled(True)
            self.ui.btn_order_sp.setEnabled(True)
            self.ui.btn_order_mp.setEnabled(False)
            self.load_data2(False)
        # 판매액순 sp
        else:
            self.ui.btn_default.setEnabled(True)
            self.ui.btn_order_sp.setEnabled(False)
            self.ui.btn_order_mp.setEnabled(True)
            self.load_data2(True)

    def load_data(self):
        res = self.TB.select_table()
        self.ui.tbl_widget.setRowCount(0)
        for idx, (no, sale_price, addTax, supply_price, marginPrice) in enumerate(res):
            item_no, item_sale_price, item_addTax, item_supply_price, item_marginPrice = self.create_item(no, sale_price, addTax, supply_price, marginPrice)
            nextIdx = self.ui.tbl_widget.rowCount()
            self.ui.tbl_widget.insertRow(nextIdx)
            self.ui.tbl_widget.setItem(nextIdx, 0, item_no)
            self.ui.tbl_widget.setItem(nextIdx, 1, item_sale_price)
            self.ui.tbl_widget.setItem(nextIdx, 2, item_addTax)
            self.ui.tbl_widget.setItem(nextIdx, 3, item_supply_price)
            self.ui.tbl_widget.setItem(nextIdx, 4, item_marginPrice)

    def load_data2(self, order):
        res = self.TB.order_by_select(order)
        self.ui.tbl_widget.setRowCount(0)
        for idx, (rank, code, name, price, saleCnt, supply_price, addTax, sale_price, mR, mP)\
                in enumerate(res):
            irank, icode, iname, iprice, isc, isupp, iaddtax, isalep, imr, imp = \
                self.create_item2(rank, code, name, price, saleCnt, supply_price, addTax, sale_price, mR, mP)
            nextIdx = self.ui.tbl_widget.rowCount()
            self.ui.tbl_widget.insertRow(nextIdx)
            self.ui.tbl_widget.setItem(nextIdx, 0, irank)
            self.ui.tbl_widget.setItem(nextIdx, 1, icode)
            self.ui.tbl_widget.setItem(nextIdx, 2, iname)
            self.ui.tbl_widget.setItem(nextIdx, 3, iprice)
            self.ui.tbl_widget.setItem(nextIdx, 4, isc)
            self.ui.tbl_widget.setItem(nextIdx, 5, isupp)
            self.ui.tbl_widget.setItem(nextIdx, 6, iaddtax)
            self.ui.tbl_widget.setItem(nextIdx, 7, isalep)
            self.ui.tbl_widget.setItem(nextIdx, 8, imr)
            self.ui.tbl_widget.setItem(nextIdx, 9, imp)
            if order == False:
                self.ui.tbl_widget.item(nextIdx, 9).setBackground(Qt.lightGray)
            else:
                self.ui.tbl_widget.item(nextIdx, 5).setBackground(Qt.lightGray)

    def create_item(self, no, sale_price, addTax, supply_price, marginPrice):
        ino = QTableWidgetItem(no)
        ino.setTextAlignment(Qt.AlignCenter)
        ino.setData(Qt.DisplayRole, no)

        isale_price = QTableWidgetItem(sale_price)
        isale_price.setTextAlignment(Qt.AlignRight)
        isale_price.setData(Qt.DisplayRole, format(int(sale_price), ',d'))

        iaddTax = QTableWidgetItem(addTax)
        iaddTax.setTextAlignment(Qt.AlignRight)
        iaddTax.setData(Qt.DisplayRole, format(int(addTax), ',d'))

        isupply_price = QTableWidgetItem(supply_price)
        isupply_price.setTextAlignment(Qt.AlignRight)
        isupply_price.setData(Qt.DisplayRole, format(int(supply_price), ',d'))

        imarginPrice = QTableWidgetItem(marginPrice)
        imarginPrice.setTextAlignment(Qt.AlignRight)
        imarginPrice.setData(Qt.DisplayRole, format(int(marginPrice), ',d'))
        return ino, isale_price, iaddTax, isupply_price, imarginPrice

    def create_item2(self, rank, code, name, price, sc, supp, addtax, salep, mr, mp):
        i0 = QTableWidgetItem(rank)
        i0.setTextAlignment(Qt.AlignCenter)
        i0.setData(Qt.DisplayRole, rank)

        i1 = QTableWidgetItem(code)
        i1.setTextAlignment(Qt.AlignCenter)
        i1.setData(Qt.DisplayRole, code)

        i2 = QTableWidgetItem(name)
        i2.setTextAlignment(Qt.AlignCenter)
        i2.setData(Qt.DisplayRole, name)

        i3 = QTableWidgetItem(price)
        i3.setTextAlignment(Qt.AlignRight)
        i3.setData(Qt.DisplayRole, format(price, ','))

        i4 = QTableWidgetItem(sc)
        i4.setTextAlignment(Qt.AlignRight)
        i4.setData(Qt.DisplayRole, format(sc, ','))

        i5 = QTableWidgetItem(supp)
        i5.setTextAlignment(Qt.AlignRight)
        i5.setData(Qt.DisplayRole, format(supp, ','))

        i6 = QTableWidgetItem(addtax)
        i6.setTextAlignment(Qt.AlignRight)
        i6.setData(Qt.DisplayRole, format(addtax, ','))

        i7 = QTableWidgetItem(salep)
        i7.setTextAlignment(Qt.AlignRight)
        i7.setData(Qt.DisplayRole, format(salep, ','))

        i8 = QTableWidgetItem(mr)
        i8.setTextAlignment(Qt.AlignRight)
        i8.setData(Qt.DisplayRole, format(mr, ','))

        i9 = QTableWidgetItem(mp)
        i9.setTextAlignment(Qt.AlignRight)
        i9.setData(Qt.DisplayRole, format(mp, ','))
        return i0, i1, i2, i3, i4, i5, i6, i7, i8, i9
