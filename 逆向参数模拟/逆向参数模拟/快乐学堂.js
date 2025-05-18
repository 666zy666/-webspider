var _key = 'k1fsa01v';
var _iv = 'k1fsa01v';
const CryptoJS = require('crypto-js')
function encryptByDES(message) {
    var keyHex = CryptoJS.enc.Utf8.parse(_key);
    var encrypted = CryptoJS.DES.encrypt(message, keyHex, {
        iv: CryptoJS.enc.Utf8.parse(_iv),
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}
 var r= Math.random()
//密码
var pass = '111'
var password=encryptByDES(pass)
console.log(password,r)