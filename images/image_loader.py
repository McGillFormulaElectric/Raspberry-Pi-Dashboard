from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QWidget


# This points to the folder that contains this script:
# .../Raspberry-Pi-Dashboard/images/
# So image_name should be just "file.png", not a full absolute path.
IMAGES_DIR = Path(__file__).resolve().parent


def load_image_to_label(
    label,
    image_name: str,
    keep_aspect_ratio: bool = True,
    smooth: bool = True,
) -> bool:
    """
    Load an image from the local images/ folder into a QLabel.

    Example:
        load_image_to_label(self.window.logoPlaceholder, "page_1.jpg")

    image_name:
        Use only the file name (or subpath inside images), e.g.:
        "logo.png" or "icons/car.png"
        Do NOT use a full path like "C:/.../logo.png"

    Returns True on success, False if the file is missing or invalid.
    """
    # Build the real file path from images/ + image_name.
    image_path = IMAGES_DIR / image_name
    if not image_path.exists():
        return False

    # Read image file into a pixmap Qt can display.
    pixmap = QPixmap(str(image_path))
    if pixmap.isNull():
        return False

    # Optionally resize image to fit label while keeping proportions.
    if keep_aspect_ratio:
        mode = Qt.SmoothTransformation if smooth else Qt.FastTransformation
        pixmap = pixmap.scaled(label.size(), Qt.KeepAspectRatio, mode)

    # Push the pixmap into the label widget.
    label.setPixmap(pixmap)
    label.setAlignment(Qt.AlignCenter)
    return True


def load_image_map(window, image_map: dict[str, str]) -> dict[str, bool]:
    """
    Batch-load many QLabel images by object name.

    image_map format:
    {
        "logoLabel": "logo.png",
        "carLabel": "car.png",
    }

    - Key = QLabel objectName from Qt Designer
    - Value = file name inside images/

    Returns:
        {"logoLabel": True, "carLabel": False, ...}
        so you can see what loaded and what failed.
    """
    results: dict[str, bool] = {}
    for label_name, image_name in image_map.items():
        # Find QLabel by objectName in the loaded UI tree.
        label = window.findChild(QLabel, label_name)
        if label is None:
            results[label_name] = False
            continue

        # Load the corresponding image file into that label.
        results[label_name] = load_image_to_label(label, image_name)
    return results


def load_page_image(
    window,
    page_number: int,
    label_name: str,
    image_name: str | None = None,
) -> bool:
    """
    Load a page image into a QLabel that lives on a specific stacked-widget page.

    Intended workflow:
    - In Qt Designer, place/size/crop your QLabel manually on page_X.
    - In code, call this function with the page number and label objectName.

    Examples:
        load_page_image(self.window, 1, "bgImageLabel")
        load_page_image(self.window, 3, "logoLabel", "my_custom_logo.png")

    Defaults:
    - If image_name is omitted, this loads "page_<page_number>.jpg"
      e.g. page_number=4 -> "page_4.jpg"
    """
    page = window.findChild(QWidget, f"page_{page_number}")
    if page is None:
        return False

    label = page.findChild(QLabel, label_name)
    if label is None:
        return False

    file_name = image_name if image_name else f"page_{page_number}.jpg"
    return load_image_to_label(label, file_name)
