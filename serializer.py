import struct, json, pathlib
from tkinter import *
from tkinter import filedialog

findjson=Tk()
findjson.title('Find your json file')

renderloc8=Tk()
renderloc8.title('Render your json file')

input_json=findjson.filename=filedialog.askopenfilename(initialdir=str(pathlib.Path().absolute()), title="Find your json file",filetypes=[("json file","*.json")] )

output_loc8=filedialog.asksaveasfilename(title = "Render your loc8 file",filetypes = (("LOC8","*.loc8"),("all files","*.*")))

a=open(input_json,'rb')
readjson=a.read().decode("utf-8")
locjson=json.loads(readjson)

loc8=open(output_loc8,'wb')
strings=locjson["Strings"]
audio=locjson["Audio"]
paths=locjson["Paths"]
unknown=locjson["Unknown"]

string_count=len(strings)
loc8.write(struct.pack('>I',string_count))

for string in strings:
    loc8.write(struct.pack('>I',string["Key"]))
    prevalue=string["Value"]
    value_count=len(prevalue)
    loc8.write(struct.pack('>I',value_count))
    for value_combine in prevalue:
        loc8.write(struct.pack('>I',value_combine["Key"]))
        value=value_combine["Value"]
        loc8.write(struct.pack('>I',len(value))+value.encode())

#audio and paths (ubi hardly used these)
loc8.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')

for unknown_value in unknown:
    loc8.write(struct.pack('>I',unknown_value))