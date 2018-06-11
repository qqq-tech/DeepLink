from Deeplink.database.sql.SqliteAdapter import  *
from Deeplink.database.sql.LinkDetail import *
from Deeplink.core import GlobalVal
from Deeplink.utl import ListUtil


def loadLinkData():
  sa = SqliteAdapaterImpl("/Deeplink/database/DeepLink.db")
  GlobalVal.deepLinkList= sa.select(GET_INITIAL_LINK)
  GlobalVal.deepLinkLDict=ListUtil.listToDict(GlobalVal.deepLinkList);