'''import pickle
fobj=open("file1.ser","wb")
pickle.dump(1.5,fobj)
pickle.dump(1+2j,fobj)
pickle.dump("NIT",fobj)
pickle.dump([10,20,30],fobj)
fobj.close()'''


import pickle
data=['sowmya',98.2,21]
byte=pickle.dumps(data)
print(byte)      #pickled representation

#unpickling
data1=pickle.loads(byte)
print(data1)

