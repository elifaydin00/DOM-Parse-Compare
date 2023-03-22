const { Builder, Options } = require("selenium-webdriver");
const { DOMParser, XMLSerializer } = require('xmldom');
const chrome = require("selenium-webdriver/chrome");

async function get_dom(url, browserName) {
  if (!browserName || typeof browserName !== 'string') {
    throw new Error('Invalid browser name');
  }

  let options = new chrome.Options();

  if (typeof options.setPageLoadStrategy === 'function') {
    options.setPageLoadStrategy('normal'); //normal or eager
  } else {
    console.warn('Page load strategy not supported for this driver');
  } //implement for other browsers like mozilla

  let driver = await new Builder()
    .forBrowser(browserName)
    .setChromeOptions(options)
    .build();

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

    const dom1 = await get_dom_chrome('https://hipmunk-com.com/');
    //console.log(dom1);
    const parser1 = new DOMParser();
    const xmlDoc1 = parser1.parseFromString(dom1, "application/xml");

    //Same browser (instance) comparison
    const dom3 = await get_dom_chrome('https://hipmunk-com.com/');
    
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

    console.log("*************\n");
    const extractedStrings = [];


    for (var i = 0; i < diff.length; i++){
      if(diff[i].message.includes("expected value") && diff[i].message.includes("instead of")){
        //console.log("Parse by regex and push: ", diff[i].message);
        const match = diff[i].message.match(/expected value '([^']*)' instead of '([^']*)'/);
        if (match) {
          extractedStrings.push(match[1], match[2]);
        }
      }
    }
    console.log(extractedStrings);

    extractedValues = [];

    for (let i = 0; i < extractedStrings.length; i++) {
      const string = extractedStrings[i];
      const regex = /(?<=\=|&)(\d+\.\d+|\d+)(?=\&|$)/g;
      let match;
      
      while ((match = regex.exec(string)) !== null) {
        extractedValues.push(match[0]);
      }
    }

    extractedValues = extractedValues.filter(val => val.length !== 1);
    console.log(extractedValues);

    /*Now, convert dom1 and dom2 to strings and mask if given strings exists */
    const serializer = new XMLSerializer();
    str1_doc = serializer.serializeToString(xmlDoc1);
    
    extractedValues.forEach((val) => {
      str1_doc = str1_doc.replaceAll(val, "MASKED");
    });

    console.log(str1_doc);

    const serializer2 = new XMLSerializer();
    str2_doc = serializer.serializeToString(xmlDoc3);
    
    extractedValues.forEach((val) => {
      str2_doc = str2_doc.replaceAll(val, "MASKED");
    });
  
    //comparison after masked

    parser_masked1 = new DOMParser();
    xmlDoc1_parsed = parser_masked1.parseFromString(str1_doc, "application/xml");

    parser_masked2 = new DOMParser();
    xmlDoc2_parsed = parser_masked2.parseFromString(str2_doc, "application/xml");

    var compare2 = require('dom-compare').compare,
    reporter = require('dom-compare').GroupingReporter,
    expected = xmlDoc1_parsed,
    actual = xmlDoc2_parsed,
    result, diff, groupedDiff;
 
    // compare to DOM trees, get a result object
    result = compare(expected, actual);
    
    // get comparison result
    console.log(result.getResult()); // false cause' trees are different

}

main();