f = open('pkg/hello_wasm_bg.wasm','rb')
code_as_integers = [s for s in f.read()]
f.close()
print(code_as_integers)
#write code_as_integers to file
f = open('output.txt','wb')
f.write(str(code_as_integers).encode())
f.close()
