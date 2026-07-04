names = "pran, alice, bob"
print(len(names)) #length dinxa
print(names[0]) #p is output
print(names[0:4]) #pran is output, 0 dekhi 4 indx vayeko samma
print(names[4:9]) #, ali is output, 4 dekhi 9 indx vayeko samma
print(names[0:-3]) #pran, alice is output, 0 dekhi -3 indx vayeko samma
a = "ApPle .."
print(a.upper())
print(a.lower())
print(a.rstrip("."))
print(a.replace("p", "l")) #p lai l le replace garxa

b = "pranisha"
print(b.count("a")) #b ma, "a" kati ota xa herna
print(b.isalpha())
 
c = "123Abc"
print(c.isalnum())
print(c.isalpha())