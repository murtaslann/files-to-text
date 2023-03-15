import os
import time

txt = list()
py = list()

for klasör_yolu,klasör_ismi,dosya_ismi in os.walk("C:\\Users\\Excalıbur\\Desktop"):
    for i in dosya_ismi:
        if(i.endswith(".txt")):
            txt.append(i)
        else:
            py.append(i)

with open("txt.txt","w+",encoding="utf-8") as txt_file:
    txt_file.write("Pc'deki txt uzantılı dosyalar;\n\n")
    for satır in txt:
        txt_file.write(satır + "\n")


with open("py.txt","w+",encoding="utf-8") as py_file:
    py_file.write("Pc'deki py uzantılı dosyalar;\n\n")
    for satır in py:
        py_file.write(satır+ "\n")
