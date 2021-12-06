dm = [199,200,208,210,200,207,240,269,260,263]
pocet_mereni = len (dm)
out = list()
count = 0
out.append ("N/A")
print ("pocet mereni je:", pocet_mereni)
for i in range (0,pocet_mereni-1):
    if dm [i+1] - dm [i] > 0:
        out.append ("increased")
        count += 1
    else:
        out.append ("decreased")
print (out)
print ("There are",count,"meaurements higher then the previous one." )