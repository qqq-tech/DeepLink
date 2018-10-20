import json

def listToDict(fromObj,key):
  res={}
  arr=[]
  preLInkName=""
  for once in fromObj:
    if(preLInkName!='' and preLInkName!=once[key]):
      res[once[key]] = arr
      arr.clear()
    arr.append(once)
    preLInkName=once[key]

  res[preLInkName]=arr
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