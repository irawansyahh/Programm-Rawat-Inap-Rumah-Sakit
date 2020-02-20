def kamar(filetoread):
  f=open(filetoread,'r')
  content=f.read()
  filteredcontent=content.split(':')
  morefilteredcontent=[filteredcontent[x].split(',') for x in range(len(filteredcontent))]
  f.close()
  return morefilteredcontent