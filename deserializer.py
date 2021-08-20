import struct, json, pathlib
from tkinter import *
from tkinter import filedialog

findloc8=Tk()
findloc8.title('Find your loc8 file')

renderjson=Tk()
renderjson.title('Render your json file')

input_loc8=findloc8.filename=filedialog.askopenfilename(initialdir=str(pathlib.Path().absolute()), title="Find your loc8 file",filetypes=[("loc8 file","*.loc8")] )

output_json=filedialog.asksaveasfilename(title = "Render your json file",filetypes = (("JSON","*.json"),("all files","*.*")))

localisation={
"Strings": [],
"Audio": [],
"Paths": [],
"Unknown": []
}

f=open(input_loc8,"rb")

strings=struct.unpack('>I',f.read(4))[0]
string_total=strings
running=True
for x in range(strings):
    prekey=struct.unpack('>I',f.read(4))[0]

    prevalue={
      "Key": prekey,
      "Value": []
    }
    localisation["Strings"].append(prevalue)

    string_total=string_total-1

    values=struct.unpack('>I',f.read(4))[0]
    
    value_total=values
    print(value_total)
    for x in range(values):
        hexkey=f.read(4)
        key=struct.unpack('>I',hexkey)[0]
        len_valuename = struct.unpack('>I',f.read(4))[0]
        valuename = f.read(len_valuename).decode("utf-8")

        value={
        "Key": key,
        "Value": valuename
        }

        localisation["Strings"][0]["Value"].append(value)

        value_total=value_total-1
        if value_total==0:
            break

audio=struct.unpack('>I',f.read(4))[0]
paths=struct.unpack('>I',f.read(4))[0]

while running==True:
    unknown=f.read(4)
    if unknown==b'':
        break

    deserial_value=struct.unpack('>I',unknown)[0]
    localisation["Unknown"].append(deserial_value)

json.dump(localisation,open(output_json,"w"))