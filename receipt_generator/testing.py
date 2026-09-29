import generate_png as gp
import bit_png as ipr

import generate_html as gh

from print_receipt import print_receipt


def run_pipeline(data: dict):
    gh.render_receipt(data, "output/html/pipeline_test.html")
    gp.html_file_to_png("output/html/pipeline_test.html", "output/png/")
    ipr.convert_for_thermal("output/png/pipeline_test.png", "output/png/pipeline_1bit.png")
    print_receipt("output/png/pipeline_1bit.png")

