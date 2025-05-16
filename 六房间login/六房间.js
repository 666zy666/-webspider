
const  Cryjs= require("crypto-js");

function ln(nonce,r){
    var servertime = parseInt((new Date).getTime()/1e3)
    password=Cryjs.SHA1(""+Cryjs.SHA1(Cryjs.SHA1(r)+servertime)+nonce).toString()
    return password
}
