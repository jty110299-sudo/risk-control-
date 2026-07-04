from pathlib import Path
from typing import Iterable, List


DEFAULT_EXTENSIONS = (".csv", ".txt", ".tsv")


def ensure_directory(path: str | Path) -> Path:
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def find_candidate_input_files(
    sample_dir: str | Path, extensions: Iterable[str] | None = None
) -> List[Path]:
    directory = Path(sample_dir)
    if not directory.exists():
        return []
    allowed_extensions = tuple(extensions or DEFAULT_EXTENSIONS)
    return sorted(
        path for path in directory.iterdir()
        if path.is_file() and path.suffix.lower() in allowed_extensions
    )


def list_official_sample_files(sample_dir: str | Path) -> List[Path]:
    return find_candidate_input_files(sample_dir)


def read_csv_safely(file_path: str | Path, **kwargs):
    """Read a delimited file.

    Future phases should add an explicit file size check before reading large
    official files. This function never downloads files automatically.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    try:
        import pandas as pd
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "pandas is required to read input files. Install requirements.txt before ingestion."
        ) from exc
    suffix = path.suffix.lower()
    if suffix == ".tsv":
        kwargs.setdefault("sep", "\t")
    elif suffix == ".txt":
        kwargs.setdefault("sep", "|")
    return pd.read_csv(path, **kwargs)
