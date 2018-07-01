import json

def listToDict(fromObj,key):
  res={}
  for once in fromObj:
    res[once[key]]=once
  return res

def dicToJson(obj):
  return json.dumps(obj)

def jsonToDic(str):
  return json.loads(str)


def setPreResultArg(fromObj,toStr):
  result=jsonToDic(toStr)
  #{"fromKey":"toKey"}
  #return{"toKey"= toValue}
  for key in result.keys():
    fromKey,toKey=result.pop(key)
    result[toKey]=fromObj[fromKey]

  return result