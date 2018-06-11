GET_INITIAL_LINK = "select link_name, running_seq, a.model_name,module_path,module_function,using_pre_result,pre_process_group,pre_process_name,pre_process_argument_json,post_process_group,post_process_name,post_process_argument_json \
from model_link_detail a join  model_master b on a.model_name=b.model_name order by running_seq asc"
