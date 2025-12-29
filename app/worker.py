from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from PySide6.QtCore import QObject, Signal, Slot

from .pdf_ops import split_pdf_to_folder, PdfEncryptedError, PdfCorruptError


@dataclass
class SplitResult:
    out_dir: Path
    files_created: int


class SplitWorker(QObject):
    progress = Signal(int, int)
    finished = Signal(object)
    failed = Signal(str)

    def __init__(self, pdf_path: str, pages_per_part: int = 20):
        super().__init__()
        self.pdf_path = pdf_path
        self.pages_per_part = pages_per_part

    @Slot()
    def run(self) -> None:
        try:
            from pypdf import PdfReader

            reader = PdfReader(self.pdf_path)
            if getattr(reader, "is_encrypted", False):
                raise PdfEncryptedError("This PDF is encrypted/password-protected and is not supported in v1.")

            total_pages = len(reader.pages)
            total_parts = max(1, (total_pages + self.pages_per_part - 1) // self.pages_per_part)

            out_dir, files = split_pdf_to_folder(self.pdf_path, self.pages_per_part)

            self.progress.emit(total_parts, total_parts)
            self.finished.emit(SplitResult(out_dir=out_dir, files_created=len(files)))

        except PdfEncryptedError as e:
            self.failed.emit(str(e))
        except PdfCorruptError as e:
            self.failed.emit(f"Could not read this PDF (it may be corrupted).\n\nDetails: {e}")
        except Exception as e:
            self.failed.emit(f"Unexpected error.\n\nDetails: {e}")
