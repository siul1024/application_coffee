from PyQt5.QtWidgets import QApplication
from ui.product_ui import UiProduct
from ui.sale_ui import UiSale

if __name__=="__main__":
    app = QApplication([])
    pui = UiProduct()
    sui = UiSale()
    exit(app.exec_())