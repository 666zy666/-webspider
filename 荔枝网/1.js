delete process
delete global
Window = function Window() {
};

window = new Window;

Location = function Location() {

}
Location.prototype = {
    "ancestorOrigins": {},
    "href": "https://www.gdtv.cn/channels/4#345",
    "origin": "https://www.gdtv.cn",
    "protocol": "https:",
    "host": "www.gdtv.cn",
    "hostname": "www.gdtv.cn",
    "port": "",
    "pathname": "/channels/4",
    "search": "",
    "hash": "#345"
};
location = new Location()
window.location = location
document = {
    location: window.location
}
window.document = document

self = window
self.self = window
globalThis = window
XMLHttpRequest = function XMLHttpRequest() {

}
fs =require('fs')
var wasm_code = fs.readFileSync('下载.wasm')

 var J = null;
function k() {
          return null !== J && 0 !== J.byteLength || (J = new Uint8Array(wasm_enc.memory.buffer)),
          J
}


function U(A) {
                                return null == A
                            }
function s() {
                                return null !== c && 0 !== c.byteLength || (c = new Int32Array(wasm_enc.memory.buffer)),
                                c
                            }
function Y(A) {
                                o === M.length && M.push(M.length + 1);
                                var g = o;
                                return o = M[g],
                                M[g] = A,
                                g
                            }
 function R(A, g) {
                                try {
                                    return A.apply(this, g)
                                } catch (A) {
                                    console.log('R',A)
                                    wasm_enc.__wbindgen_export_3(Y(A))
                                }
                            }
var N = new TextDecoder("utf-8",{
                                ignoreBOM: !0,
                                fatal: !0
                            })
 function K(A, g) {
                                return A >>>= 0,
                                N.decode(k().subarray(A, A + g))
                            }
 function E(A, g, I) {
    return E = function () {
        if ("undefined" == typeof Reflect || !Reflect.construct)
            return !1;
        if (Reflect.construct.sham)
            return !1;
        if ("function" == typeof Proxy)
            return !0;
        try {
            return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], (function () {
                }
            ))),
                !0
        } catch (A) {
            console.log(A)
            return !1
        }
    }() ? Reflect.construct.bind() : function (A, g, I) {
        var B = [null];
        B.push.apply(B, g);
        var Q = new (Function.bind.apply(A, B));
        return I && D(Q, I.prototype),
            Q
    }
        ,
        E.apply(null, arguments)
}
var P = Function
function S() {
                                for (var A = arguments.length, g = new Array(A), I = 0; I < A; I++)
                                    g[I] = arguments[I];
                                var B = function() {
                                    try {
                                        return E(P, g)
                                    } catch (A) {
                                        console.log('S',A)
                                        return function() {
                                            return null
                                        }
                                    }
                                }();
                                return B.toString = function() {
                                    return ""
                                }
                                ,
                                B
                            }

var c = null;

function t() {
                                var g = {
                                    wbg: {}
                                };
                                return g.wbg.__wbindgen_object_drop_ref = function(A) {
                                    G(A)
                                }
                                ,
                                g.wbg.__wbg_self_1ff1d729e9aae938 = function() {
                                    return R((function() {
                                        return Y(self.self)
                                    }
                                    ), arguments)
                                }
                                ,
                                g.wbg.__wbg_window_5f4faef6c12b79ec = function() {
                                    return R((function() {
                                        return Y(window.window)
                                    }
                                    ), arguments)
                                }
                                ,
                                g.wbg.__wbg_globalThis_1d39714405582d3c = function() {
                                    return R((function() {
                                        return Y(globalThis.globalThis)
                                    }
                                    ), arguments)
                                }
                                ,
                                g.wbg.__wbg_global_651f05c6a0944d1c = function() {
                                    return R((function() {
                                        return Y(A.global)
                                    }
                                    ), arguments)
                                }
                                ,
                                g.wbg.__wbindgen_is_undefined = function(A) {
                                    return void 0 === i(A)
                                }
                                ,
                                g.wbg.__wbg_newnoargs_581967eacc0e2604 = function(A, g) {
                                    return Y(S(K(A, g)))
                                }
                                ,
                                g.wbg.__wbg_call_cb65541d95d71282 = function() {
                                    return R((function(A, g) {
                                        return Y(i(A).call(i(g)))
                                    }
                                    ), arguments)
                                }
                                ,
                                g.wbg.__wbindgen_object_clone_ref = function(A) {
                                    return Y(i(A))
                                }
                                ,
                                g.wbg.__wbg_instanceof_Window_9029196b662bc42a = function(A) {
                                    var g;
                                    try {
                                        g = i(A)instanceof Window
                                    } catch (A) {
                                        console.log('9029196b662bc42a',A)
                                        g = !1
                                    }
                                    return g
                                }
                                ,
                                g.wbg.__wbg_document_f7ace2b956f30a4f = function(A) {
                                    var g = i(A).document;
                                    return U(g) ? 0 : Y(g)
                                }
                                ,
                                g.wbg.__wbg_location_56243dba507f472d = function(A) {
                                    return Y(i(A).location)
                                }
                                ,
                                g.wbg.__wbg_host_15090f3de0544fea = function() {
                                    return R((function(A, g) {
                                        var I = L(i(g).host, wasm_enc.__wbindgen_export_0, wasm_enc.__wbindgen_export_1)
                                          , B = h;
                                        s()[A / 4 + 1] = B,
                                        s()[A / 4 + 0] = I
                                    }
                                    ), arguments)
                                }
                                ,
                                g.wbg.__wbg_origin_50aa482fa6784a0a = function() {
                                    return R((function(A, g) {
                                        var I = L(i(g).origin, wasm_enc.__wbindgen_export_0, wasm_enc.__wbindgen_export_1)
                                          , B = h;
                                        s()[A / 4 + 1] = B,
                                        s()[A / 4 + 0] = I
                                    }
                                    ), arguments)
                                }
                                ,
                                g.wbg.__wbg_href_d62a28e4fc1ab948 = function() {
                                    return R((function(A, g) {
                                        var I = L(i(g).href, wasm_enc.__wbindgen_export_0, wasm_enc.__wbindgen_export_1)
                                          , B = h;
                                        s()[A / 4 + 1] = B,
                                        s()[A / 4 + 0] = I
                                    }
                                    ), arguments)
                                }
                                ,
                                g.wbg.__wbg_newwithargs_a0432b7780c1dfa1 = function(A, g, I, B) {
                                    return Y(S(K(A, g), K(I, B)))
                                }
                                ,
                                g.wbg.__wbindgen_string_new = function(A, g) {
                                    return Y(K(A, g))
                                }
                                ,
                                g.wbg.__wbg_call_01734de55d61e11d = function() {
                                    return R((function(A, g, I) {
                                        return Y(i(A).call(i(g), i(I)))
                                    }
                                    ), arguments)
                                }
                                ,
                                g.wbg.__wbindgen_string_get = function(A, g) {
                                    var I = i(g)
                                      , B = "string" == typeof I ? I : void 0
                                      , Q = U(B) ? 0 : L(B, wasm_enc.__wbindgen_export_0, wasm_enc.__wbindgen_export_1)
                                      , C = h;
                                    s()[A / 4 + 1] = C,
                                    s()[A / 4 + 0] = Q
                                }
                                ,
                                g.wbg.__wbg_eval_8c72ad5eafe427f2 = function() {
                                    return R((function(A, g) {
                                        return Y(x(K(A, g)))
                                    }
                                    ), arguments)
                                }
                                ,
                                g.wbg.__wbindgen_typeof = function(A) {
                                    return Y(I(i(A)))
                                }
                                ,
                                g.wbg.__wbindgen_boolean_get = function(A) {
                                    var g = i(A);
                                    return "boolean" == typeof g ? g ? 1 : 0 : 2
                                }
                                ,
                                g.wbg.__wbg_new_56693dbed0c32988 = function() {
                                    return Y(new Map)
                                }
                                ,
                                g.wbg.__wbg_set_bedc3d02d0f05eb0 = function(A, g, I) {
                                    return Y(i(A).set(i(g), i(I)))
                                }
                                ,
                                g.wbg.__wbindgen_number_new = function(A) {
                                    return Y(A)
                                }
                                ,
                                g.wbg.__wbg_new0_c0be7df4b6bd481f = function() {
                                    return Y(new Date)
                                }
                                ,
                                g.wbg.__wbg_getTime_5e2054f832d82ec9 = function(A) {
                                    return i(A).getTime()
                                }
                                ,
                                g.wbg.__wbg_new_cd59bfc8881f487b = function(A) {
                                    return Y(new Date(i(A)))
                                }
                                ,
                                g.wbg.__wbg_getTimezoneOffset_8aee3445f323973e = function(A) {
                                    return i(A).getTimezoneOffset()
                                }
                                ,
                                g.wbg.__wbindgen_throw = function(A, g) {
                                    throw new Error(K(A, g))
                                }
                                ,
                                g
                            }
var M = new Array(128).fill(void 0);
function i(A) {
                                return M[A]
                            }

var H =128
function L(A, g, I) {
                                if (void 0 === I) {
                                    var B = y.encode(A)
                                      , Q = g(B.length, 1) >>> 0;
                                    return k().subarray(Q, Q + B.length).set(B),
                                    h = B.length,
                                    Q
                                }
                                for (var C = A.length, E = g(C, 1) >>> 0, D = k(), w = 0; w < C; w++) {
                                    var M = A.charCodeAt(w);
                                    if (M > 127)
                                        break;
                                    D[E + w] = M
                                }
                                if (w !== C) {
                                    0 !== w && (A = A.slice(w)),
                                    E = I(E, C, C = w + 3 * A.length, 1) >>> 0;
                                    var i = k().subarray(E + w, E + C);
                                    E = I(E, C, w += F(A, i).written, 1) >>> 0
                                }
                                return h = w,
                                E
                            }

M.push(void 0, null, !0, !1);
var o = M.length;
function G(A) {
                                var g = i(A);
                                return function(A) {
                                    A < 132 || (M[A] = o,
                                    o = A)
                                }(A),
                                g
                            }
function ws(A, g, I, B, Q, C) {
    try {
        var E = L(A, wasm_enc.__wbindgen_export_0, wasm_enc.__wbindgen_export_1)
            , D = h
            , i = L(g, wasm_enc.__wbindgen_export_0, wasm_enc.__wbindgen_export_1)
            , o = h
            , Y = L(I, wasm_enc.__wbindgen_export_0, wasm_enc.__wbindgen_export_1)
            , N = h
            , J = L(B, wasm_enc.__wbindgen_export_0, wasm_enc.__wbindgen_export_1)
            , k = h
            , K = L(Q, wasm_enc.__wbindgen_export_0, wasm_enc.__wbindgen_export_1)
            , y = h;
        return G(wasm_enc.a(E, D, i, o, Y, N, J, k, K, y, function (A) {
            if (1 == H)
                throw new Error("out of js stack");
            return M[--H] = A,
                H
        }(C)))
    } catch (e) {
        console.log('ws wrong',e)
    }
    finally {
        M[H++] = void 0
    }
}
B123=t()
WebAssembly.instantiate(wasm_code,B123 ).then(result=>{
                          C = result.instance
                          var E = result.module
                          wasm_enc=C.exports
                          aaa=ws('GET','https://gdtv-api.gdtv.cn/api/channel/v1/news?beginScore=1758069586000&channelId=246&pageSize=11','WEB_d8e6e280-9087-11f0-bbd1-41ad82e4d631','WEB_PC','',undefined)
                          const obj = Object.fromEntries(aaa);
                          const json = JSON.stringify(obj);

                          console.log(json)


})

