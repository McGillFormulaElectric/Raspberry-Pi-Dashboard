from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
import os
from PySide6.QtCore import Qt
from widgets.frontbrake import FrontBrakeBar


def main():
    app = QApplication(sys.argv)

    # Create loader and register custom widget
    loader = QUiLoader()
    loader.registerCustomWidget(FrontBrakeBar)

    # Absolute path to the .ui file
    ui_path = os.path.join(
        os.path.dirname(__file__),
        "untitled",
        "mainwindow.ui"
    )

    ui_file = QFile(ui_path)
    if not ui_file.open(QFile.ReadOnly):
        raise RuntimeError(f"Could not open UI file: {ui_path}")

    # Load the UI (this IS the main window)
    window = loader.load(ui_file)
    ui_file.close()

    if window is None:
        raise RuntimeError("Failed to load UI")

    # Get the promoted widget
    frontbrake = window.findChild(FrontBrakeBar, "frontbrake")
    if frontbrake is None:
        raise RuntimeError(
            "frontbrake not found — check objectName and promotion"
        )

    # Test value
    frontbrake.setValue(60)

    window.setWindowState(Qt.WindowNoState)
    window.setGeometry(100, 100, 1200, 800)
    window.show()
    window.raise_()
    window.activateWindow()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
