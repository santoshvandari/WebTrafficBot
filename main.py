import asyncio
from playwright.async_api import async_playwright
import random

# List of user agents to simulate different browsers
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
    'Version/14.1.2 Safari/605.1.15',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
]

# List of URLs to visit
URLS = [
    'https://sharehisab.com/',
]

async def simulate_user_interaction(page):
    for _ in range(random.randint(2, 5)):
        scroll_distance = random.randint(100, 1000)
        await page.mouse.wheel(0, scroll_distance)
        await asyncio.sleep(random.uniform(1, 3))

    try:
        selector = 'body *'
        await page.wait_for_selector(selector, timeout=10000)  # Increase timeout to 10 seconds
        elements = await page.query_selector_all(selector)
        if elements:
            print(f"Found {len(elements)} elements to potentially hover over.")
            element = random.choice(elements)
            if element:
                print("Hovering over an element.")
                await element.hover(timeout=10000)  # Increase timeout to 10 seconds
                await asyncio.sleep(random.uniform(0.5, 1.5))
        else:
            print("No elements found for hovering.")
    except Exception as e:
        print(f"An error occurred during hover: {e}")

    wait_time = random.randint(120, 180)
    print(f"Staying on the page for {wait_time} seconds.")
    await asyncio.sleep(wait_time)

async def visit_website(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Use headless mode
        
        context = await browser.new_context(
            viewport={'width': random.randint(800, 1920), 'height': random.randint(600, 1080)},
            user_agent=random.choice(USER_AGENTS),
            locale='en-US',
            timezone_id='America/New_York',
        )

        page = await context.new_page()
        await page.goto(url, wait_until='networkidle')  # Wait until the network is idle

        print(f"Visited {url} successfully!")

        await simulate_user_interaction(page)

        await browser.close()

if __name__ == "__main__":
    url = random.choice(URLS)
    asyncio.run(visit_website(url))