"""
Camoufox example: polite, persistent-profile scraping.

Setup (once):
    uv init --bare
    uv add "camoufox[geoip]"
    uv run camoufox fetch        # downloads the patched Firefox build
"""

import random
import time

from camoufox.sync_api import Camoufox

URLS = [
    "https://old.reddit.com/",
    "https://amazon.com",
    "https://x.com",
]


def human_pause(lo=2.0, hi=5.0):
    """Random delay between actions so request timing isn't robotic."""
    time.sleep(random.uniform(lo, hi))


def main():
    with Camoufox(
        headless=False,  # visible window leaks fewer signals than headless
        humanize=True,  # human-like cursor movement
        geoip=True,  # match timezone/locale to your IP
        os="macos",  # fingerprint OS (pick one consistent value)
        persistent_context=True,  # keep cookies/history between runs
        user_data_dir="./camoufox_profile",
    ) as context:
        page = context.new_page()

        for url in URLS:
            page.goto(url, wait_until="domcontentloaded")
            human_pause()

            # Scroll a bit like a real reader would
            page.mouse.wheel(0, random.randint(400, 1200))
            human_pause(1, 2)

            title = page.title()
            headings = page.locator("h1, h2").all_inner_texts()
            print(f"{url}\n  title: {title}\n  headings: {headings[:5]}\n")

            human_pause(3, 8)  # be gentle on the server between pages


if __name__ == "__main__":
    main()
