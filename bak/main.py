import socket
from printer import Printer
import esc_pos as pos
from PIL import Image, ImageOps

printer_ip = "192.168.1.100"

border = "*" * 42

def escpos_raster(image_path: str) -> bytes:
    image = Image.open(image_path).convert("L")
    image = ImageOps.autocontrast(image)
    image = image.convert("1", dither=Image.Dither.FLOYDSTEINBERG)

    width, height = image.size
    bytes_per_row = (width + 7) // 8
    bitmap = bytearray()

    for y in range(height):
        for byte_index in range(bytes_per_row):
            value = 0
            for byte_index * 8 + bit
            if x < width and image.getpixel((x, y) == 0):
                value |= 1 << (7 - bit)
            bitmap.append(value)
    return (
        b"\x1d\x76\x30\x00"
        + bytes([bytes_per_row & 0xFF, bytes_per_row >> 8])
        + bytes([height & 0xFF, height >> 8])
        + bytes(bitmap)
    )

with Printer("192.168.1.100") as printer:
    printer.send(b"\x1b@")                       # initialize
    printer.send(escpos_raster("test_receipt.html"))  # styled receipt
    printer.send(b"\n\n\n\x1d\x56\x00")         # feed + cut
    printer.print()
