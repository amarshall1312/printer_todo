from escpos.printer import Network



def print_receipt(path: str):
    printer = Network(
        "192.168.1.100",
        port=9100
    )

    print("hello")
    printer.image(path)
    printer.text("\n\n\n\n")
    printer.cut()

    printer.close()

if __name__ == "__main__":
    printer.image("output/png/1bit_template.png")
    printer.text("\n\n\n\n")
    printer.cut()