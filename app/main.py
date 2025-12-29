from __future__ import annotations

import os
import sys
from pathlib import Path

from PySide6.QtCore import QThread, QSettings
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QStyleFactory

from .styles import LIGHT_QSS, DARK_QSS
from .gui_main import MainLayout
from .worker import SplitWorker, SplitResult

from PySide6.QtGui import QIcon
import ctypes



def open_in_explorer(folder: Path) -> None:
    os.startfile(str(folder))


class MainWindow(MainLayout):
    def __init__(self, app: QApplication, settings: QSettings) -> None:
        super().__init__()
        self._app = app
        self._settings = settings
        self.setWindowIcon(QIcon(resource_path("assets/icon.ico")))
        self.setWindowTitle("PDF Splitter")
        self.setMinimumSize(650, 480)

        self.selected_pdf: str | None = None
        self.last_out_dir: Path | None = None

        self.theme: str = str(self._settings.value("theme", "light"))
        self.apply_theme(self.theme)

        self.drop_zone.file_dropped.connect(self.on_pdf_selected)
        self.select_btn.clicked.connect(self.select_pdf)
        self.split_btn.clicked.connect(self.start_split)
        self.open_folder_btn.clicked.connect(self.open_output_folder)

        self.pages.valueChanged.connect(lambda _: self.update_split_button_text())
        self.update_split_button_text()

        self.theme_btn.clicked.connect(self.toggle_theme)

        self.thread: QThread | None = None
        self.worker: SplitWorker | None = None

    def apply_theme(self, theme: str) -> None:
        self.theme = "dark" if theme == "dark" else "light"
        self._settings.setValue("theme", self.theme)

        if self.theme == "dark":
            self._app.setStyleSheet(DARK_QSS)
            self.theme_btn.setText("☀")
        else:
            self._app.setStyleSheet(LIGHT_QSS)
            self.theme_btn.setText("☾")

    def toggle_theme(self) -> None:
        self.apply_theme("dark" if self.theme == "light" else "light")

    def update_split_button_text(self) -> None:
        pages = int(self.pages.value())
        self.split_btn.setText(f"Split ({pages} pages)")

    def set_busy(self, busy: bool) -> None:
        self.select_btn.setEnabled(not busy)
        self.drop_zone.setEnabled(not busy)
        self.pages.setEnabled(not busy)
        self.split_btn.setEnabled((not busy) and (self.selected_pdf is not None))
        self.open_folder_btn.setEnabled((not busy) and (self.last_out_dir is not None))
        self.theme_btn.setEnabled(not busy)

    def reset_ui_ready(self) -> None:
        self.selected_pdf = None
        self.file_name.setText("No file selected")
        self.file_path.setText("Drop a PDF above or click Select PDF.")
        self.status.setText("")
        self.progress.setVisible(False)
        self.progress.setValue(0)
        self.split_btn.setEnabled(False)

        self.drop_zone.text.setText("Drag & drop a PDF here")
        self.drop_zone.hint.setText("or click Select PDF below")

    def on_pdf_selected(self, path: str) -> None:
        self.selected_pdf = path
        p = Path(path)

        self.file_name.setText(p.name)
        self.file_path.setText(str(p.parent))

        self.drop_zone.text.setText("PDF selected ✓")
        self.drop_zone.hint.setText("Click Split to start")

        self.status.setText("Ready.")
        self.split_btn.setEnabled(True)

    def select_pdf(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "Select PDF", "", "PDF Files (*.pdf)")
        if path:
            self.on_pdf_selected(path)

    def start_split(self) -> None:
        if not self.selected_pdf:
            return

        pages = int(self.pages.value())

        self.set_busy(True)
        self.progress.setVisible(True)
        self.progress.setValue(0)
        self.status.setText(f"Splitting into {pages}-page parts…")

        self.thread = QThread()
        self.worker = SplitWorker(pdf_path=self.selected_pdf, pages_per_part=pages)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.on_progress)
        self.worker.finished.connect(self.on_finished)
        self.worker.failed.connect(self.on_failed)

        self.worker.finished.connect(self.thread.quit)
        self.worker.failed.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def on_progress(self, current_part: int, total_parts: int) -> None:
        if total_parts <= 0:
            return
        val = int((current_part / total_parts) * 100)
        self.progress.setValue(max(0, min(100, val)))

    def on_finished(self, result: SplitResult) -> None:
        self.last_out_dir = result.out_dir
        self.set_busy(False)
        self.progress.setValue(100)

        QMessageBox.information(
            self,
            "Done",
            f"Created {result.files_created} file(s) in:\n{result.out_dir}"
        )

        self.open_folder_btn.setEnabled(True)
        self.reset_ui_ready()

    def on_failed(self, message: str) -> None:
        self.set_busy(False)
        self.progress.setVisible(False)
        QMessageBox.critical(self, "Error", message)
        self.reset_ui_ready()

    def open_output_folder(self) -> None:
        if self.last_out_dir:
            open_in_explorer(self.last_out_dir)


def resource_path(relative: str) -> str:
    base = getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[1])
    return str(Path(base) / relative)



def main() -> int:
    app = QApplication(sys.argv)

    app.setStyle(QStyleFactory.create("Fusion"))

    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("MindaugasApps.PdfSplitter")
    except Exception:
        pass

    app.setWindowIcon(QIcon(resource_path("assets/icon.ico")))

    QApplication.setOrganizationName("MindaugasApps")
    QApplication.setApplicationName("PdfSplitter")
    settings = QSettings()

    win = MainWindow(app=app, settings=settings)
    win.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
