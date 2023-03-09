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
    //console.log(reporter.report(result));

    console.log("*************\n");
    const extractedStrings = [];


    for (var i = 0; i < diff.length; i++){
      if(diff[i].message.includes("expected value") && diff[i].message.includes("instead of")){
        console.log("Parse by regex and push: ", diff[i].message);
        const match = diff[i].message.match(/expected value '([^']*)' instead of '([^']*)'/);
        if (match) {
          extractedStrings.push(match[1], match[2]);
        }
      }
    }
    console.log(extractedStrings);

    /*Now, convert dom1 and dom2 to strings and mask if given strings exists */
    const serializer = new XMLSerializer();
    const str1_doc = serializer.serializeToString(xmlDoc1);
    
    const words = str1_doc.split(' ');
    //change the word into MASKED if it exists in extractedStrings
    const maskedWords = words.map(word => extractedStrings.includes(word) ? 'MASKED' : word);

    const maskedStr1 = maskedWords.join(' ');

    //console.log(maskedStr1);

    const serializer2 = new XMLSerializer();
    const str2_doc = serializer.serializeToString(xmlDoc3);
    
    const words2 = str2_doc.split(' ');
    //change the word into MASKED if it exists in extractedStrings
    const maskedWords2 = words.map(word => extractedStrings.includes(word) ? 'MASKED' : word);

    const maskedStr2 = maskedWords.join(' ');

    //console.log(maskedStr2);

    //values change?? 
}

main();