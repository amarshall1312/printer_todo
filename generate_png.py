from pathlib import Path
from playwright.sync_api import sync_playwright


def html_file_to_png(
    html_path: str | Path,
    output_dir: str | Path,
) -> Path:
    html_path = Path(html_path)
    output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Read the HTML file
    html = html_path.read_text(encoding="utf-8")

    # Output has the same filename, but with .png
    output_path = output_dir / f"{html_path.stem}.png"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()

        try:
            page = browser.new_page(
                viewport={"width": 576, "height": 1200},
                device_scale_factor=2,
            )

            page.set_content(html, wait_until="load")

            receipt = page.locator(".receipt")

            if receipt.count() == 0:
                raise RuntimeError(
                    "No element matching '.receipt' found in the HTML"
                )

            receipt.screenshot(
                path=str(output_path),
                type="png",
            )

        finally:
            browser.close()

    return output_path