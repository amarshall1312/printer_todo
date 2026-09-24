from escpos.printer import Network

printer = Network(
    "192.168.1.100",
    port=9100
)

def print_receipt(path: str):
    print("hello")
    printer.image(path)
    printer.text("\n\n\n\n")
    printer.cut()

if __name__ == "__main__":
    printer.image("output/png/1bit_template.png")
    printer.text("\n\n\n\n")
    printer.cut()