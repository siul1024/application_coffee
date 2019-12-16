from PyQt5.QtWidgets import QApplication
from ui.product_ui import UiProduct

if __name__=="__main__":
    app = QApplication([])
    pui = UiProduct()
    exit(app.exec())