wlist = [2, 3, 4, 5, 6, 7, 8]
searchterm = 5
found =False

for x in range (len(wlist)):
    if searchterm == wlist[x]:
        found = True
        break

if found == True:
    print('item found')
else:
    print("item no found")
