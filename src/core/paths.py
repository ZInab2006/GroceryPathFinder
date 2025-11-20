from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = BASE_DIR / "src"
ASSETS_DIR = BASE_DIR / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
STYLES_DIR = ASSETS_DIR / "styles"
DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"
TOOLS_DIR = BASE_DIR / "tools"


def asset_path(*parts: str) -> Path:
    """Return the path to an asset file inside ``assets/``."""
    return ASSETS_DIR.joinpath(*parts)


def image_path(name: str) -> Path:
    """Return the path to an image stored in ``assets/images``."""
    return IMAGES_DIR / name


def style_path(name: str) -> Path:
    """Return the path to a QSS stylesheet stored in ``assets/styles``."""
    return STYLES_DIR / name


def data_path(name: str) -> Path:
    """Return the path to a data file stored in ``data/``."""
    return DATA_DIR / name


__all__ = [
    "BASE_DIR",
    "SRC_DIR",
    "ASSETS_DIR",
    "IMAGES_DIR",
    "STYLES_DIR",
    "DATA_DIR",
    "DOCS_DIR",
    "TOOLS_DIR",
    "asset_path",
    "image_path",
    "style_path",
    "data_path",
]

