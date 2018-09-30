from Deeplink.database.sql.SqliteAdapter import SqliteAdapaterImpl

global deepLinkList
global deepLinkDict
global dynFuncDict
global db
#db=SqliteAdapaterImpl("/Deeplink/database/DeepLink.db")
db=SqliteAdapaterImpl("../db.sqlite3")


def getDynFunc(group,name):
  return dynFuncDict[group][name]