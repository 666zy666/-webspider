var CryptoJS = require('crypto-js')
var a={
    "username": "aa123456",
    "password": "aa123456",
    //验证码
    "captcha": "14"
}
function utilsrndString(){
        for (var e = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz", t = "", n = 0; n < 16; n++) {
            var a = Math.floor(Math.random() * e.length);
            t += e.substring(a, a + 1)
        }
        return t
    }



var i = utilsrndString();
 function desEncrypt(e, i) {
        var n = CryptoJS.enc.Utf8.parse(i);
        return CryptoJS.DES.encrypt(e ,n, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).toString()
    }

Encryption= desEncrypt(JSON.stringify(a), i)
console.log(Encryption)

