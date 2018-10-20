from Deeplink.core import GlobalVal
from Deeplink.util import ConvertUtil
import copy


def isNotBlank(myString):
  if myString and myString.strip():
    # myString is not None AND myString is not empty or blank
    return True
  # myString is None OR myString is empty or blank
  return False

def linkRun(linkName,data):
  globalRes={}
  localRes={}
  inputData=copy.deepcopy(data)
  originalData=copy.deepcopy(data)
  oneLink = GlobalVal.deepLinkDict[linkName]

  for o in oneLink:
    #1. 오리지널 이미지 사용에 체크 로직 추가할것
    #json 형태의 모델의 이름 {name:결과 name}
    if isNotBlank(o["select_pre_module_output"]):
      inputData=globalRes[o["select_pre_module_output"]]

    if isNotBlank(o["pre_process_group"]):
      preProcessArgument = {}
      if o["using_pre_prediction"]:
        # localRes 대체하여 globalRes에서 refrence_model_result 로 가져 올것.
        preProcessArgument = ConvertUtil.setPreResultArg(o["pre_process_argument_json"],localRes)
      inputData=(GlobalVal.getDynFunc(o["pre_process_group"],o["pre_process_name"]))(inputData,preProcessArgument)
    #1. 이전 output bin 사용 or 원본 사용에 대한 처리 가 필요
    #2. prediction 결과에 대한 판단 후 처리 필요. why??? 원본에 수정을 가한 bin 리턴시 어떻게 하려고?

    localRes=(GlobalVal.getDynFunc("model",o["model_name"]))(inputData)

#후처리는 result만...
    if isNotBlank(o["post_process_grouop"]):
      localRes = (GlobalVal.getDynFunc(o["pre_process_group"], o["pre_process_name"]))()

    globalRes[o["model_name"]]=localRes

  return globalRes