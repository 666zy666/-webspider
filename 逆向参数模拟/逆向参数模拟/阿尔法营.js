const  Cryjs= require("crypto-js");
var e='/WebApi/Users/Login?username=12345&password=12345DUE$DEHFYE(YRUEHD*&'
var t = ''


function a(e, t) {
        var n = (new Date).getTime() + 2592e6 + (t || 3e4)
          , r = (e || "") + "&t=" + n;
        return {
            t: n,
            s: Cryjs.SHA1(r).toString()
        }
    }


console.log(a(e,t))