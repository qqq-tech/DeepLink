from Deeplink.database.sql.SqliteAdapter import SqliteAdapaterImpl

global deepLinkList
global deepLinkDict
global dynFuncDict
global db
db=SqliteAdapaterImpl("/Deeplink/database/DeepLink.db")


def getDynFunc(group,name):
  return dynFuncDict[group][name]