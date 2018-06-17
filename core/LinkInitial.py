from Deeplink.database.sql.SqliteAdapter import  *
from Deeplink.database.sql.LinkDetail import *
from Deeplink.core import GlobalVal
from Deeplink.util import ConvertUtil


def loadLinkData():
  GlobalVal.deepLinkList= GlobalVal.db.select(GET_INITIAL_LINK)
  GlobalVal.deepLinkLDict=ConvertUtil.listToDict(GlobalVal.deepLinkList, "link_name")