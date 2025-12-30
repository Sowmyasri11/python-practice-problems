import pickle
fobj=open("file1.ser","wb")
pickle.dump(1.5,fobj)
pickle.dump(1+2j,fobj)
pickle.dump("NIT",fobj)
pickle.dump([10,20,30],fobj)
fobj.close()