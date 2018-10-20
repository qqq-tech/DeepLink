from Deeplink.database.sql.SqliteAdapter import SqliteAdapaterImpl

global deepLinkList
global deepLinkDict
global dynFuncDict
global db
deepLinkList=[]
deepLinkDict={}
dynFuncDict={}
#db=SqliteAdapaterImpl("/Deeplink/database/DeepLink.db")
db=SqliteAdapaterImpl("../db.sqlite3")
#sys.path.append("C:/doit/mymod")

def getDynFunc(group,name):
  return dynFuncDict[group][name]