import random
words = open("all-6lyokavica.txt","r")
donchovci = []
for word in words:
  if word.endswith('on\n'):
   donchovci.append(word.replace('\n','')+'cho')


random.shuffle(donchovci)
file=open("donchovci.txt","w")
for word in donchovci:
  file.write(word+'\n')



