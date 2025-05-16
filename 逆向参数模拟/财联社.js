e='app=CailianpressWeb&lastTime={D}&os=web&sv=8.4.6'
w="app=CailianpressWeb&category=&hasFirstVipArticle=1&lastTime=1746952789&os=web&rn=20&subscribedColumnIds=&sv=8.4.6"
const Cryjs= require("crypto-js");
var res=Cryjs.SHA1('app=CailianpressWeb&category=&hasFirstVipArticle=1&lastTime={D}&os=web&rn=20&subscribedColumnIds=&sv=8.4.6').toString()
sign=Cryjs.MD5(res).toString()
console.log(sign)
