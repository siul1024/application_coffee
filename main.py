from PyQt5.QtWidgets import QApplication

from ui.mainwindow_ui import UiMainWindow
from ui.product_ui import UiProduct
from ui.sale_detail_ui import UiSaleDetail
from ui.sale_ui import UiSale

if __name__=="__main__":
    app = QApplication([])
    ui = UiMainWindow()
    exit(app.exec_())