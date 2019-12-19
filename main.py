from PyQt5.QtWidgets import QApplication
from ui.mainwindow_ui import UiMainWindow


if __name__ == "__main__":
    app = QApplication([])
    ui = UiMainWindow()
    exit(app.exec_())