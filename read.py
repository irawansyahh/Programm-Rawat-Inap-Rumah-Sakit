def readfile(filetoread):
  f=open(filetoread,'r')
  content=f.read()
  f.close()
  
  return content