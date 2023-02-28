const { Builder, By, Key } = require("selenium-webdriver");
const { DOMParser, XMLSerializer } = require('xmldom');

async function get_dom(url, browserName) {
    if (!browserName || typeof browserName !== 'string') {
      throw new Error('Invalid browser name');
    }
  
    let driver = await new Builder().forBrowser(browserName).build();
    try {
      await driver.get(url);
      const serializedDOM = await driver.executeScript(
        "return new XMLSerializer().serializeToString(document);"
      );
      return serializedDOM;
    } finally {
      await driver.quit();
    }
  }

async function get_dom_chrome(url) {
  return get_dom(url, 'chrome');
}

async function get_dom_firefox(url) {
  return get_dom(url, 'firefox');
}

async function main() {

    //Browser Comparison

    const dom1 = await get_dom_chrome('https://www.garantibbva.com.tr/');
    const parser1 = new DOMParser();
    const xmlDoc1 = parser1.parseFromString(dom1, "application/xml");

    /*const dom2 = await get_dom_firefox('https://www.garantibbva.com.tr/');

    const parser2 = new DOMParser();
    const xmlDoc2 = parser2.parseFromString(dom2, "application/xml");

    var compare = require('dom-compare').compare,
    reporter = require('dom-compare').GroupingReporter,
    expected = xmlDoc1,
    actual = xmlDoc2,
    result, diff, groupedDiff;
 
    // compare to DOM trees, get a result object
    result = compare(expected, actual);
    
    // get comparison result
    console.log(result.getResult()); // false cause' trees are different
    
    // get all differences
    diff = result.getDifferences(); // array of diff-objects

    // differences, grouped by node XPath
    groupedDiff = reporter.getDifferences(result); // object, key - node XPATH, value - array of differences (strings)
    
    // string representation
    console.log(reporter.report(result));*/

    //Same browser (instance) comparison
    const dom3 = await get_dom_chrome('https://www.garantibbva.com.tr/');
    
    const parser3 = new DOMParser();
    const xmlDoc3 = parser3.parseFromString(dom3, "application/xml");

    var compare = require('dom-compare').compare,
    reporter = require('dom-compare').GroupingReporter,
    expected = xmlDoc1,
    actual = xmlDoc3,
    result, diff, groupedDiff;
 
    // compare to DOM trees, get a result object
    result = compare(expected, actual);
    
    // get comparison result
    console.log(result.getResult()); // false cause' trees are different
    
    // get all differences
    diff = result.getDifferences(); // array of diff-objects

    // differences, grouped by node XPath
    groupedDiff = reporter.getDifferences(result); // object, key - node XPATH, value - array of differences (strings)
    
    // string representation
    console.log(reporter.report(result));
    //console.log(Object.keys(groupedDiff)); //prints node XPATH
    //console.log(Object.values(groupedDiff)); //prints array of differences
}

main();