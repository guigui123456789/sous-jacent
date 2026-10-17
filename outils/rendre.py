# -*- coding: utf-8 -*-
"""Rendu PDF maîtrisé : feuille A4 exacte, fonds imprimés, aucune marge.

Le rendu par --print-to-pdf de Chromium n'occupait que 86 % de la feuille,
ce qui laissait un liseré blanc à droite et en bas, très visible sur les
pages à fond marine.
"""
import sys, asyncio
from playwright.async_api import async_playwright

async def rendre(src, dest):
    async with async_playwright() as p:
        nav = await p.chromium.launch(args=['--no-sandbox', '--disable-gpu'])
        page = await nav.new_page()
        await page.goto('file://' + src, wait_until='networkidle')
        await page.emulate_media(media='print')
        await page.pdf(path=dest, prefer_css_page_size=True, print_background=True,
                       margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'})
        await nav.close()

src, dest = sys.argv[1], sys.argv[2]
asyncio.run(rendre(src, dest))
print('rendu', dest)
