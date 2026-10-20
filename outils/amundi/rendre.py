import asyncio,sys
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if False else None)
    pg=await b.new_page()
    await pg.goto('file:///root/amundi/da/amundi.html'); await pg.wait_for_timeout(800)
    await pg.pdf(path='/root/amundi/da/Amundi-Etude-2.pdf',width='210mm',height='297mm',print_background=True)
    await b.close()
asyncio.run(main())
