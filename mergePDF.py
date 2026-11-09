"""
merge.py - Ek folder ki saari PDF files ko ek single PDF me merge karta hai.

Usage:
    python merge.py                      # current folder ki PDFs merge hongi
    python merge.py -i pdfs -o out.pdf   # custom input folder aur output name

Requirements:
    pip install pypdf
"""

import argparse
import logging
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.errors import PdfReadError

# ---------- Logging setup ----------
# print ki jagah logging use karte hain, taaki time + level (INFO/ERROR) dikhe
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """Command line arguments padhta hai."""
    parser = argparse.ArgumentParser(description="Merge multiple PDFs into one.")
    parser.add_argument("-i", "--input", default=".", help="PDFs wala folder (default: current folder)")
    parser.add_argument("-o", "--output", default="merged.pdf", help="Output file ka naam (default: merged.pdf)")
    return parser.parse_args()


def collect_pdfs(folder: Path, output_name: str) -> list[Path]:
    """Folder se saari PDFs ki list deta hai (output file ko chhod kar)."""
    # sorted() se order hamesha same rahega
    return sorted(
        p for p in folder.glob("*.pdf")
        if p.name.lower() != output_name.lower()
    )


def merge_pdfs(pdf_files: list[Path], output_path: Path) -> tuple[int, list[tuple[Path, str]]]:
    """
    PDFs ko merge karta hai.

    Returns:
        (success_count, failed_list)
        failed_list me (file, error reason) hota hai.
    """
    writer = PdfWriter()
    success = 0
    failed: list[tuple[Path, str]] = []

    for pdf in pdf_files:
        try:
            # Pehle check karo ki file password-protected to nahi
            reader = PdfReader(pdf)
            if reader.is_encrypted:
                raise ValueError("password-protected PDF")

            writer.append(reader)
            success += 1
            log.info("Added: %s (%d pages)", pdf.name, len(reader.pages))

        except (PdfReadError, ValueError) as e:
            # Corrupt ya encrypted file - skip karo, baaki chalne do
            log.error("Skipped: %s -> %s", pdf.name, e)
            failed.append((pdf, str(e)))
        except Exception as e:  # koi unexpected error
            log.error("Unexpected error in %s -> %s", pdf.name, e)
            failed.append((pdf, str(e)))

    # Agar ek bhi file add nahi hui toh output banane ka matlab nahi
    if success == 0:
        return 0, failed

    try:
        with open(output_path, "wb") as f:
            writer.write(f)
    except PermissionError:
        # Aksar tab hota hai jab merged.pdf kisi viewer me khuli ho
        log.error("Output file likh nahi sakte. Kya '%s' khuli hui hai?", output_path.name)
        raise
    finally:
        writer.close()

    return success, failed


def main() -> int:
    """Main function. Exit code: 0 = success, 1 = kuch fail hua."""
    args = parse_args()
    folder = Path(args.input).resolve()
    output_path = folder / args.output

    # Input folder check
    if not folder.is_dir():
        log.error("Folder nahi mila: %s", folder)
        return 1

    pdf_files = collect_pdfs(folder, args.output)
    if not pdf_files:
        log.error("Is folder me koi PDF nahi mili: %s", folder)
        return 1

    log.info("%d PDF files mili. Merge shuru...", len(pdf_files))

    try:
        success, failed = merge_pdfs(pdf_files, output_path)
    except PermissionError:
        return 1
    except Exception as e:
        log.exception("Merge fail ho gaya: %s", e)
        return 1

    # ---------- Summary ----------
    if success == 0:
        log.error("Koi bhi PDF merge nahi hui.")
        return 1

    log.info("Done! %d/%d PDFs merge hui -> %s", success, len(pdf_files), output_path)

    if failed:
        log.warning("%d file(s) fail hui:", len(failed))
        for pdf, reason in failed:
            log.warning("  - %s (%s)", pdf.name, reason)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
