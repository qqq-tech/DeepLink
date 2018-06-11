
def listToDict(fromObj,key):
  res={}
  for once in fromObj:
    res[once[key]]=once
  return res

