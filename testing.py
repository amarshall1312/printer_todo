import generate_png as gp
import bit_png as ipr

import generate_html as gh

from print_receipt import print_receipt

#gp.html_file_to_png("/home/mojito/printer/output/html/receipt_template.html", "/home/mojito/printer/output/png/")

#ipr.convert_for_thermal("output/png/receipt_template.png", "output/png/1bit_template.png")

def run_pipeline(data: dict):
    gh.render_receipt(data, "output/html/pipeline_test.html")
    gp.html_file_to_png("output/html/pipeline_test.html", "output/png/")
    ipr.convert_for_thermal("output/png/pipeline_test.png", "output/png/pipeline_1bit.png")
    print_receipt("output/png/pipeline_1bit.png")

"""
Current capability

Params > Template > html > png > 1bitpng > print
generate_html > generate_png > bit_png > print

Need to host a service that can be passed this object and execute the pipeline

"""