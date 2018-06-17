GET_INITIAL_DYN_FUNC="select group_name,process_name,module_path,module_function,argument_json from util_mgmt \
union \
select 'model' as group_name, model_name as process_name, module_path,module_function, module_input as argument_json from model_master"