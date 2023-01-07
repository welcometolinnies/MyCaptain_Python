fn=input("Input the Filename: ")
ext=fn.split(".")
if ext[-1]=="py":
    ext1="python"
else:
    ext1=ext[-1]
print("The extension of the file is :",ext1)
