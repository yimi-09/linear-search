nlist = [2, 4, 6, 7, 9, 12, 15]
searchterm = 6
found = False

for x in range (len(nlist)):
    if searchterm == nlist[x]:
        found = True
        break
    
if (found = True):
    print("found number")
else:
    print("number not found")
    
