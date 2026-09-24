"""PNG -> 1-bit bitmap sized for the print head."""

from __future__ import annotations

import io
from pathlib import Path

from PIL import Image


def prepare_for_thermal(
    png: bytes | str | Path,
    width: int = 576,
    threshold: int = 128,
    dither: bool = False,
) -> Image.Image:
    """Return a mode-"1" image exactly `width` dots wide.

    The supersampled capture is resized down with Lanczos first — that is what
    does the anti-aliasing — and only then flattened to black and white.
    """
    if isinstance(png, bytes):
        source = Image.open(io.BytesIO(png))
    else:
        source = Image.open(png)

    with source:
        # Flatten transparency onto white, or RGBA->L turns clear pixels black.
        if source.mode in ("RGBA", "LA", "P"):
            rgba = source.convert("RGBA")
            canvas = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
            canvas.alpha_composite(rgba)
            grey = canvas.convert("L")
        else:
            grey = source.convert("L")

    if grey.width != width:
        height = max(1, round(grey.height * width / grey.width))
        grey = grey.resize((width, height), Image.Resampling.LANCZOS)

    if dither:
        return grey.convert("1", dither=Image.Dither.FLOYDSTEINBERG)

    # point() then a dither-free convert keeps the hard edges we just decided on;
    # convert("1") alone would re-dither the greys.
    return grey.point(lambda value: 255 if value >= threshold else 0, mode="L").convert(
        "1", dither=Image.Dither.NONE
    )


def save(image: Image.Image, path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)
    return path


def convert_for_thermal(
    input_path: str | Path,
    output_path: str | Path,
    width: int = 576,
    threshold: int = 128,
    dither: bool = False,
) -> Path:
    """Convert an input image to a print-ready bitmap and save it to `output_path`."""
    image = prepare_for_thermal(
        input_path,
        width=width,
        threshold=threshold,
        dither=dither,
    )
    return save(image, output_path)
