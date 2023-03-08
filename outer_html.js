/*This code creates a virtual DOM from the original DOM using jsdom. 
It then compares the outerHTML property of the virtual DOM elements to check if they are equal.
This approach ignores any insignificant differences like
differences in whitespace or attributes that do not 
affect the appearance or functionality of the page. */

const { JSDOM } = require("jsdom");
const { Builder, By, Key } = require("selenium-webdriver");

async function get_dom(url, browserName) {
  if (!browserName || typeof browserName !== "string") {
    throw new Error("Invalid browser name");
  }

  let driver = await new Builder().forBrowser(browserName).build();
  try {
    await driver.get(url);
    const dom = await driver.executeScript(
      "return document.documentElement.outerHTML"
    );
    return dom;
  } finally {
    await driver.quit();
  }
}

async function get_dom_chrome(url) {
  return get_dom(url, "chrome");
}

async function get_dom_firefox(url) {
  return get_dom(url, "firefox");
}

async function main() {
  const dom1 = await get_dom_chrome("https://www.garantibbva.com.tr/");
  const dom2 = await get_dom_chrome("https://www.garantibbva.com.tr/");

  // Create a virtual DOM from the original DOM
  const virtualDom1 = new JSDOM(dom1).window.document;
  const virtualDom2 = new JSDOM(dom2).window.document;

  // Compare the outerHTML of the virtual DOM elements
  const isEqual = virtualDom1.documentElement.outerHTML === virtualDom2.documentElement.outerHTML;

  console.log(isEqual);
}

main();