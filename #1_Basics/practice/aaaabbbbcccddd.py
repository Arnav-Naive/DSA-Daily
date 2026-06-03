f = open("C:\Arnav-Projects\DSA-Daily\#1_Basics\practice\demo.txt", "r") # if not , will have pass complete path of the file
data = f.read()
print(data)
print(type(data))  
f.close()