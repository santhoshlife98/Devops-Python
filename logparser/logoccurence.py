import re

'''Author: Santhosh Bheeman'''
'''Python code to extract the number of Logs based on date and occurences'''

txtfile="alert.log"

logreg="\d{1,4}\:\d{1,2}\:\d{1,2}"
logreg2=".*\/\/(\d+)"

with open(txtfile) as txt:
    fread = txt.read()
    x=re.findall(logreg,fread)
    y=re.findall(logreg2,fread)
    dictu = {}
    for k,v in zip(x,y):
        if k in dictu.keys():
            dictu[k] += int(v)
        else:
            dictu[k] = int(v)
    print "date       no_of_alerts_triggered"
    for ke,ve in sorted(dictu.items()):
        print ke,ve
