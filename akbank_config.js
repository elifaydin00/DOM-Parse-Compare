//const inputString = '<script src="/WebApplication.UI/content/js/security/rsa.js?20230303190948"></script>';
const regex1 = /rsa\.js\?(\d+)"/; 
const regex2= /barrett\.js\?(\d+)"/; 
const regex3= /bigint\.js\?(\d+)"/; 
const regex4= /tea\.js\?(\d+)"/; 
const regex5 = /\|rpid=(-?\d+)\|/;
const regex6 = /Tea\.EncryptionKey\s*=\s*"([A-Z0-9]+)"/;
const regex7= /aspx\?T=([A-Z0-9]+)&/;
const regex8= /aspx\?T=([A-Z0-9]+)"/;
const regex9= /veribranch_windowid\s*=\s*'([\da-f-]+)'/;
const regex10=/RSAEncryptInMemory\('([A-Za-z0-9-]+)'\)/;

const inputString = "+ RSAEncryptInMemory('770ebdfe-8ad6-448a-a29c-2b7998f2ccb3')";

let match;
if ((match = regex10.exec(inputString)) !== null) {
  const capturedDigits = match[1]; // get the first capturing group
  console.log(capturedDigits);
}



