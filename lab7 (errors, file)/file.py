
with open ("nonsense.txt", "w") as f:
    f.write("      test write")
    
with open("nonsense.txt", "a") as f:
    f.write(" \nnew text added")
with open ("nonsense.txt", "r") as f:
    #print(f.read()) #reads as it is
    print(f.readlines()) #reads as a list
    #for l in f:
        #print(l.strip()) #if any whitespaces or new lines, it removes them 
        # print(l) #reads as it is but line by line