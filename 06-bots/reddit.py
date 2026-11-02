import random
import time

from camoufox.sync_api import Camoufox

USERNAME = ""
PASS = ""


def human_pause(lo=2.0, hi=5.0):
    """Random delay between actions so request timing isn't robotic."""
    time.sleep(random.uniform(lo, hi))


def login():
    with Camoufox(
        headless=False,
        humanize=True,
        geoip=True,
        os="macos",
        persistent_context=True,
        user_data_dir="./camoufox_profile",
    ) as context:
        page = context.new_page()

        page.goto("https://old.reddit.com/login/", wait_until="domcontentloaded")
        human_pause()

        page.locator('input[name="username"]').fill(USERNAME)
        human_pause()

        # page.locator('input[name="password"]').press_sequentially(USERNAME, delay=random.randint(80, 160))

        page.locator('input[name="password"]').fill(PASS)
        human_pause()

        page.get_by_role("button", name="Log In").click()
        human_pause()


def browse():
    with Camoufox(
        headless=False,
        humanize=True,
        geoip=True,
        os="macos",
        persistent_context=True,
        user_data_dir="./camoufox_profile",
    ) as context:
        page = context.new_page()
        page.goto("https://old.reddit.com/r/all", wait_until="domcontentloaded")
        human_pause(lo=10, hi=20)


def random_post():
    with Camoufox(
        headless=False,
        humanize=True,
        geoip=True,
        os="macos",
        persistent_context=True,
        user_data_dir="./camoufox_profile",
    ) as context:
        page = context.new_page()
        page.goto("https://old.reddit.com/submit", wait_until="domcontentloaded")
        human_pause()

        page.get_by_role("link", name="text", exact=True).click()
        human_pause()

        page.locator('textarea[name="title"]').fill("Test Post")
        page.locator('textarea[name="text"]').fill("Test Post")
        page.locator('input[name="sr"]').fill("arttheory")
        # page.get_by_role("button", name="submit").click()


random_post()
