const CryptoJS = require('crypto-js')
var pwd = '1111'
var phone = '1111'
function encryptByAES(message, key) {
    let CBCOptions = {
        iv: CryptoJS.enc.Utf8.parse(key),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    };
    let aeskey = CryptoJS.enc.Utf8.parse(key);
    let secretData = CryptoJS.enc.Utf8.parse(message);
    let encrypted = CryptoJS.AES.encrypt(
        secretData,
        aeskey,
        CBCOptions
    );
    return CryptoJS.enc.Base64.stringify(encrypted.ciphertext);
}
var transferKey = "u2oh6Vu^HWe4_AES";
var pwd_enc = encryptByAES(pwd, transferKey).toString();
var phone_enc = encryptByAES(phone, transferKey).toString();
console.log(pwd_enc,phone_enc)