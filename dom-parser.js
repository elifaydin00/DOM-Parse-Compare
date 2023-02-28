const { DOMParser, XMLSerializer } = require('xmldom');

const dom1 = `
<document>
    <element attribute="10" attributeX="100">
        <text>  text content </text>
        <inner>
            <node />
        </inner>
    </element>
</document>
`;

const dom2=`
<document>
    <element attribute="100">
        <text>text content</text>
        <inner />
        <inner2 />
    </element>
</document>
`;

const parser1 = new DOMParser();
const xmlDoc1 = parser1.parseFromString(dom1, "application/xml");
const xmlString1 = new XMLSerializer().serializeToString(xmlDoc1.documentElement);

const parser2 = new DOMParser();
const xmlDoc2 = parser2.parseFromString(dom2, "application/xml");
const xmlString2 = new XMLSerializer().serializeToString(xmlDoc2.documentElement);

//console.log(xmlString1);
//console.log(xmlString2);



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
console.log(reporter.report(result));