from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from ui.product_ui import UiProduct
from ui.sale_detail_ui import UiSaleDetail
from ui.sale_ui import UiSale


class UiMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/mainwindow.ui")
        self.pui = UiProduct()
        self.sui = UiSale()
        self.dui = UiSaleDetail()
        self.ui.stk_widget.addWidget(self.pui.ui)
        self.ui.stk_widget.addWidget(self.sui.ui)
        self.ui.stk_widget.addWidget(self.dui.ui)
        self.ui.show()
        self.ui.btn_product.clicked.connect(self.display)
        self.ui.btn_sale.clicked.connect(lambda x: self.display(1))
        self.ui.btn_saledetail.clicked.connect(lambda x: self.display(2))
        self.ui.btn_product.setEnabled(False)

    def display(self, i):
        self.ui.stk_widget.setCurrentIndex(i)
        self.buttonslot(i)

    def buttonslot(self, i):
        if i == 0:
            self.ui.btn_product.setEnabled(False)
            self.ui.btn_sale.setEnabled(True)
            self.ui.btn_saledetail.setEnabled(True)
        elif i == 1:
            self.ui.btn_product.setEnabled(True)
            self.ui.btn_sale.setEnabled(False)
            self.ui.btn_saledetail.setEnabled(True)
        else:
            self.ui.btn_product.setEnabled(True)
            self.ui.btn_sale.setEnabled(True)
            self.ui.btn_saledetail.setEnabled(False)