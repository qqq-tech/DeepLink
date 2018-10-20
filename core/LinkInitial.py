from Deeplink.database.sql.SqliteAdapter import  *
from Deeplink.database.sql.LinkDetail import *
from Deeplink.core import GlobalVal
from Deeplink.util import ConvertUtil
from Deeplink.util.Impoter import dynamic_import


def loadLinkData():
  GlobalVal.deepLinkLDict = GlobalVal.db.select(GET_INITIAL_LINK)
  GlobalVal.deepLinkLDict=ConvertUtil.listToDict(GlobalVal.deepLinkList, "link_name")

  for o in GlobalVal.deepLinkList:
    GlobalVal.dynFuncDict["model"] = {o["model_name"]: dynamic_import(o["module_path"],o["module_function"])}
