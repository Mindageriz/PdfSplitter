from __future__ import annotations

from pathlib import Path
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QFont
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QProgressBar, QSizePolicy, QMessageBox,
    QSpinBox, QAbstractSpinBox
)


def is_pdf_file(path: str) -> bool:
    return Path(path).suffix.lower() == ".pdf"


class DropZone(QFrame):
    file_dropped = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("DropZone")
        self.setProperty("active", False)
        self.setAcceptDrops(True)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(8)

        self.icon = QLabel("📄")
        f = QFont()
        f.setPointSize(26)
        self.icon.setFont(f)
        self.icon.setAlignment(Qt.AlignCenter)

        self.text = QLabel("Drag & drop a PDF here")
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setObjectName("DropTitle")

        self.hint = QLabel("or click Select PDF below")
        self.hint.setObjectName("Hint")
        self.hint.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.icon)
        layout.addWidget(self.text)
        layout.addWidget(self.hint)

    def set_active(self, active: bool) -> None:
        self.setProperty("active", active)
        self.style().unpolish(self)
        self.style().polish(self)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            self.set_active(True)
            event.acceptProposedAction()

    def dragLeaveEvent(self, event) -> None:
        self.set_active(False)

    def dropEvent(self, event: QDropEvent) -> None:
        self.set_active(False)
        urls = event.mimeData().urls()
        if not urls:
            return
        path = urls[0].toLocalFile()
        if path and is_pdf_file(path):
            self.file_dropped.emit(path)
        else:
            QMessageBox.warning(self, "Not a PDF", "Please drop a .pdf file.")


class PagesStepper(QWidget):
    valueChanged = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("PagesStepper")

        row = QHBoxLayout(self)
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(10)

        self.spin = QSpinBox()
        self.spin.setObjectName("PagesSpin")
        self.spin.setRange(1, 5000)
        self.spin.setValue(20)
        self.spin.setButtonSymbols(QAbstractSpinBox.NoButtons)

        col = QVBoxLayout()
        col.setContentsMargins(0, 0, 0, 0)
        col.setSpacing(6)

        self.up = QPushButton("⌃")
        self.up.setObjectName("StepBtn")
        self.up.setAutoRepeat(True)

        self.down = QPushButton("⌄")
        self.down.setObjectName("StepBtn")
        self.down.setAutoRepeat(True)

        self.up.clicked.connect(lambda: self.spin.setValue(self.spin.value() + 1))
        self.down.clicked.connect(lambda: self.spin.setValue(self.spin.value() - 1))
        self.spin.valueChanged.connect(self.valueChanged.emit)

        col.addWidget(self.up)
        col.addWidget(self.down)

        row.addWidget(self.spin)
        row.addLayout(col)

    def value(self) -> int:
        return int(self.spin.value())

    def setEnabled(self, enabled: bool) -> None:
        super().setEnabled(enabled)
        self.spin.setEnabled(enabled)
        self.up.setEnabled(enabled)
        self.down.setEnabled(enabled)


class MainLayout(QWidget):
    def __init__(self) -> None:
        super().__init__()

        root = QVBoxLayout(self)
        root.setContentsMargins(18, 18, 18, 18)
        root.setSpacing(12)

        header = QHBoxLayout()
        header.setSpacing(10)

        self.title = QLabel("PDF Splitter")
        self.title.setObjectName("Title")
        header.addWidget(self.title)

        header.addStretch(1)

        self.theme_btn = QPushButton("☾")
        self.theme_btn.setObjectName("IconToggle")
        self.theme_btn.setToolTip("Toggle light/dark mode")
        header.addWidget(self.theme_btn)

        root.addLayout(header)

        self.subtitle = QLabel("Split PDFs into parts.")
        self.subtitle.setObjectName("Subtitle")
        root.addWidget(self.subtitle)

        self.drop_zone = DropZone()
        self.drop_zone.setFixedHeight(170)
        root.addWidget(self.drop_zone)

        self.card = QFrame()
        self.card.setObjectName("Card")
        card_lay = QVBoxLayout(self.card)
        card_lay.setContentsMargins(14, 12, 14, 12)
        card_lay.setSpacing(4)

        self.file_name = QLabel("No file selected")
        self.file_name.setObjectName("FileName")

        self.file_path = QLabel("Drop a PDF above or click Select PDF.")
        self.file_path.setObjectName("FilePath")
        self.file_path.setWordWrap(True)

        card_lay.addWidget(self.file_name)
        card_lay.addWidget(self.file_path)
        root.addWidget(self.card)

        pages_row = QHBoxLayout()
        pages_row.setSpacing(10)

        self.pages_label = QLabel("Pages per part:")
        self.pages_label.setObjectName("Subtitle")

        self.pages = PagesStepper()

        pages_row.addWidget(self.pages_label)
        pages_row.addWidget(self.pages)
        pages_row.addStretch(1)
        root.addLayout(pages_row)

        btns = QHBoxLayout()
        btns.setSpacing(12)

        self.select_btn = QPushButton("Select PDF")
        self.select_btn.setObjectName("Pill")

        self.split_btn = QPushButton("Split (20 pages)")
        self.split_btn.setObjectName("PrimaryPill")
        self.split_btn.setEnabled(False)

        self.open_folder_btn = QPushButton("Open output folder")
        self.open_folder_btn.setObjectName("Pill")
        self.open_folder_btn.setEnabled(False)

        btns.addWidget(self.select_btn)
        btns.addWidget(self.split_btn)
        btns.addWidget(self.open_folder_btn)
        root.addLayout(btns)

        self.progress = QProgressBar()
        self.progress.setVisible(False)
        self.progress.setValue(0)
        root.addWidget(self.progress)

        self.status = QLabel("")
        self.status.setObjectName("Subtitle")
        self.status.setWordWrap(True)
        root.addWidget(self.status)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        root.addWidget(spacer)
