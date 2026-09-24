from pathlib import Path
from playwright.sync_api import sync_playwright


def html_to_png(html_file: str, png_file: str):
    html_path = Path(html_file).resolve()

    with sync_playwright() as p:
        browser = p.chromium.launch()

        page = browser.new_page(
            viewport={
                "width": 576,
                "height": 1000,
            },
            device_scale_factor=1,
        )

        page.goto(html_path.as_uri())

        # Wait for fonts/images/etc.
        page.wait_for_load_state("networkidle")

        # Capture only the receipt element, excluding the page background.
        page.locator(".receipt").screenshot(
            path=png_file,
        )

        browser.close()


html_to_png("test_receipt.html", "receipt.png")