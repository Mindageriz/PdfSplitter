from __future__ import annotations
from pathlib import Path
from pypdf import PdfReader, PdfWriter

class PdfEncryptedError(Exception):
    pass

class PdfCorruptError(Exception):
    pass

def split_pdf_to_folder(input_pdf: str, pages_per_part: int = 20) -> tuple[Path, list[Path]]:
    in_path = Path(input_pdf)
    out_dir = in_path.parent / f"{in_path.stem}_split"
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        reader = PdfReader(str(in_path))
    except Exception as e:
        raise PdfCorruptError(str(e)) from e

    if getattr(reader, "is_encrypted", False):
        raise PdfEncryptedError("This PDF is encrypted and is not supported in v1.")

    total = len(reader.pages)
    out_files: list[Path] = []

    part = 1
    for start in range(0, total, pages_per_part):
        end = min(start + pages_per_part, total)

        writer = PdfWriter()
        for i in range(start, end):
            writer.add_page(reader.pages[i])

        out_path = out_dir / f"{in_path.stem}_part_{part:03d}.pdf"
        with open(out_path, "wb") as f:
            writer.write(f)

        out_files.append(out_path)
        part += 1

    return out_dir, out_files
