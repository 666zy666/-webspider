const cryptoJs = require('crypto-js')
// D = parseInt((new Date).getTime() / 1e3);
        l = {
            key: cryptoJs.enc.Utf8.parse("fX@VyCQVvpdj8RCa"),
            iv: cryptoJs.enc.Utf8.parse(function(t) {
                for (var e = "", i = 0; i < t.length - 1; i += 2) {
                    var n = parseInt(t[i] + "" + t[i + 1], 16);
                    e += String.fromCharCode(n)
                }
                return e
            }("00000000000000000000000000000000"))
        }
          , v = function(data) {
            return function(data) {
                return cryptoJs.AES.encrypt(data, l.key, {
                    iv: l.iv,
                    mode: cryptoJs.mode.CBC,
                    padding: cryptoJs.pad.Pkcs7
                }).toString()
            }(data)
        }
          , d = function(data) {
            return cryptoJs.MD5(data).toString()
        }
          , f = function(t) {
            var e = "";
            return Object.keys(t).sort().forEach((function(n) {
                e += n + ("object" === typeof (t[n]) ? JSON.stringify(t[n], (function(t, e) {
                    return "number" == typeof e && (e = String(e)),
                    e
                }
                )).replace(/\//g, "\\/") : t[n])
            }
            )),
            e
        }
          , h = function (t) {
            var data = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
              , e = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : "a75846eb4ac490420ac63db46d2a03bf"
              , n = e + f(data) + f(t) + e;
            return n = d(n),
            n = v(n)
        }

//         U={
//     "App-Ver": "",
//     "Os-Ver": "",
//     "Device-Ver": "",
//     "Imei": "",
//     "Access-Token": "",
//     "Timestemp": D,
//     "NonceStr": "1745921263fdww0",
//     "App-Id": "4ac490420ac63db4",
//     "Device-Os": "web",
//     "Signature": "GxVK4R5KanOTW7YdaOsI427JxkjLV4+7DEOJ39g3H6BmQydWxHF/de1ZIuzkgZEf"
// }
// M={
//     "username": "qwqw",
//     "password": "qwqw",
//     "code": "",
//     "hdn_refer": "https://www.epwk.com/"
// }
// C='a75846eb4ac490420ac63db46d2a03bf'
// // console.log(h(U,M,C))