from Deeplink.core import GlobalVal
from Deeplink.util import ConvertUtil
import copy


def linkRun(linkName,data):
  globalRes={}
  inputData=copy.deepcopy(data)
  originalData=copy.deepcopy(data)
  oneLink = GlobalVal.deepLinkDict["linkName"]

  for o in oneLink:
    if not o["pre_process_group"]:
      preProcessArgument = {}
      if not o["using_pre_result"]:
        preProcessArgument=o["pre_process_argument_json"]
      else:
        preProcessArgument = ConvertUtil.setPreResultArg(o["pre_process_argument_json"],localRes)
      inputData=(GlobalVal.getDynFunc(o["pre_process_group"],o["pre_process_name"]))(inputData,preProcessArgument)
    #1. 이전 output bin 사용 or 원본 사용에 대한 처리 가 필요
    #2. prediction 결과에 대한 판단 후 처리 필요. why??? 원본에 수정을 가한 bin 리턴시 어떻게 하려고?

    localRes=(GlobalVal.getDynFunc("model",o["model_name"]))(inputData)

    # if not o["post_process_grouop"]:
    #   processData = (GlobalVal.getDynFunc(o["pre_process_group"], o["pre_process_name"]))()

    globalRes[o["model_name"]]=localRes

  return globalRes