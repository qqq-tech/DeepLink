from Deeplink.core import GlobalVal
import copy


def linkRun(linkName,data):
  globalRes={}
  inputData=cloneData=copy.deepcopy(data)
  oneLink = GlobalVal.deepLinkDict["linkName"]

  for o in oneLink:
    processData={}
    if not o["pre_process_group"]:
      if not o["using_pre_result"]:
        inputData={}
      processData=(GlobalVal.getDynFunc(o["pre_process_group"],o["pre_process_name"]))()

    localRes=(GlobalVal.getDynFunc("model",o["model_name"]))()

    if not o["post_process_grouop"]:
      inputData = {}
      processData = (GlobalVal.getDynFunc(o["pre_process_group"], o["pre_process_name"]))()
    globalRes[o["model_name"]]=localRes

  return globalRes