fs =require('fs')
function aa(page){
    n={
    "env": {},
    "wasi_snapshot_preview1": {}
}
var wasm_code = fs.readFileSync('Wasm.wasm')
var e= WebAssembly.instantiate(wasm_code,n )

e.then((result)=>{
    asm=result['instance'].exports

    console.log(asm.encrypt(20, parseInt(Math.round((new Date).getTime() / 1e3).toString())))
})
}
aa(process[2])
