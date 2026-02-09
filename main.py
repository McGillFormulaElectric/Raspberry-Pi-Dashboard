import sys
import os

# ---- HARD FIXES FOR WINDOWS / DPI / OFF-SCREEN ISSUES ----
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

from widgets.frontbrake import FrontBrakeBar


def main():
    app = QApplication(sys.argv)

    # ---- UI LOADER ----
    loader = QUiLoader()
    loader.registerCustomWidget(FrontBrakeBar)

    ui_path = os.path.join(
        os.path.dirname(__file__),
        "untitled",
        "mainwindow.ui"
    )

    ui_file = QFile(ui_path)
    if not ui_file.open(QFile.ReadOnly):
        raise RuntimeError(f"Could not open UI file: {ui_path}")

    window = loader.load(ui_file)
    ui_file.close()

    if window is None:
        raise RuntimeError("Failed to load UI")

    # ---- FORCE WINDOW STATE (CRITICAL ON WINDOWS) ----
    window.setWindowFlags(
        Qt.Window
        | Qt.WindowMinimizeButtonHint
        | Qt.WindowMaximizeButtonHint
        | Qt.WindowCloseButtonHint
    )

    window.setWindowState(Qt.WindowNoState)
    window.resize(1280, 800)
    window.move(100, 100)

    # ---- FIND WIDGETS ----
    frontbrake = window.findChild(FrontBrakeBar, "frontbrake")
    if frontbrake is None:
        raise RuntimeError("frontbrake widget not found")

    # ---- TEST VALUE ----
    frontbrake.setValue(60)

    # ---- SHOW WINDOW ----
    window.show()
    window.raise_()
    window.activateWindow()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
