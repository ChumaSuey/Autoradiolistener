//Radiolistener
//const playwright = require('playwright');
//const chromium = playwright.chromium;
const { chromium } = require('playwright');
let browser;
//let page;

(async () => {
    const context = await chromium.launchPersistentContext('./user-data', {
        headless: false,
        slowMo: 100,
        ignoreDefaultBrowserChecks: true
      });
    const page = await context.newPage();

    await page.goto('https://www.google.com');
    page.on('dialog', dialog => {
        dialog.dismiss();
      });

    const searchInput = await page.$('//textarea[@id="APjFqb"]');
    console.log('Search input:', searchInput);
    const searchQuery = 'Circuito Lider';
    await searchInput.type(searchQuery);

    await page.keyboard.press('Enter');

    await page.waitForSelector('div.g');
    console.log('Waiting for 5 seconds...');
    await page.waitForTimeout(5000);
    console.log('5 seconds passed!');
    //const link = await page.$$('h3');
    //const targetLink = link.find((element) => element.textContent.indexOf('Circuito Líder - Fuerza Radial en Venezuela - stre'));
    //await targetLink.click();
    const link = await page.$('//div[@class="tF2Cxc"]//div[@class="yuRUbf"]//div//h3[@class="LC20lb MBeuO DKV0Md"]');
    const textContent = await page.evaluate(el => el.textContent, link);
    if (textContent.includes('Circuito Líder')) {
      await link.click();
    } else {
      console.error('Element not found');
    }
    console.log('Waiting for 5 seconds...');
    await page.waitForTimeout(5000);
    console.log('5 seconds passed!');
    const button = await page.$('//img[@id="boton-play-pause"]');
    console.log('Waiting for 5 seconds...');
    await page.waitForTimeout(5000);
    console.log('5 seconds passed!');
    await button.click();
    await page.waitForTimeout(10000);
    await browser.close();
})();