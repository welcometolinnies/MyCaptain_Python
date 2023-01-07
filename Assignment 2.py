fn=input("Input the Filename: ")
ext=fn.split(".")
D={"py":"python","java":"java","docx":"Microsoft Word file","pdf":"PDF file","txt":"Plain text file","cpp":"C++ source code file","jpeg":"JPEG image","png":"PNG image"}
ext1=ext[-1]
if ext1 in D:
    DictVal=D.get(ext1)
    print("The file extension is :",DictVal)
else:
    print("Unrecognizable file extension")
