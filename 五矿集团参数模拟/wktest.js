//参数a的生成
 function v(A, e) {
            var t = Object.keys(A);
            if (Object.getOwnPropertySymbols) {
                var n = Object.getOwnPropertySymbols(A);
                e && (n = n.filter((function(e) {
                    return Object.getOwnPropertyDescriptor(A, e).enumerable
                }
                ))),
                t.push.apply(t, n)
            }
            return t
        }
        function m(A) {
            for (var e = 1; e < arguments.length; e++) {
                var t = null != arguments[e] ? arguments[e] : {};
                e % 2 ? v(Object(t), !0).forEach((function(e) {
                    b(A, e, t[e])
                }
                )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(A, Object.getOwnPropertyDescriptors(t)) : v(Object(t)).forEach((function(e) {
                    Object.defineProperty(A, e, Object.getOwnPropertyDescriptor(t, e))
                }
                ))
            }
            return A
        }
        function b(A, e, t) {
            return e in A ? Object.defineProperty(A, e, {
                value: t,
                enumerable: !0,
                configurable: !0,
                writable: !0
            }) : A[e] = t,
            A
        }
e={
    "inviteMethod": "",
    "businessClassfication": "",
    "mc": "",
    "lx": "ZBGG",
    "dwmc": "",
    "pageIndex": 4
}
var  Cryjs= require("crypto-js");
a = m(m({}, e), {}, {
                                sign: Cryjs.MD5(JSON.stringify(e)).toString(),
                                timeStamp: +new Date
                            })
console.log(a)
