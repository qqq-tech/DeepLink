from Deeplink.core import GlobalVal
from Deeplink.database.sql import UtilMgnt
from Deeplink.util.Impoter import *
def initialDynFuncDic():
  funcList = GlobalVal.db.select(UtilMgnt.GET_INITIAL_DYN_FUNC,{})
  for o in funcList:
    GlobalVal.dynFuncDict[o["group_name"]][o["module_name"]] = dynamic_import(o["module_path"],o["module_function"])