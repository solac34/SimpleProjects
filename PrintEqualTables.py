import math
namelist = ['Ata','Mehmet','Krankwrgensen','Johannsenatrulabus']
indexlist = [*range(0,4)]
maxlen = max([len(n) for n in namelist])*2

print('-'*(maxlen+4))
for i in range(len(namelist)):
    print(f"|{indexlist[i]}|{' '*int((maxlen-len(namelist[i]))/2)}{namelist[i]}{' '*math.ceil((maxlen-len(namelist[i]))/2)}|")
print('-'*(maxlen+4))



