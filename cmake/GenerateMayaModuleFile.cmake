
# ------------------------------------------------
# generate_maya_module_file()
#
# Description:
#     Generate the module description file for Maya (.mod).
#
# Arguments:
#     MODULE_NAME: Name of the module to create. The name should not contain extension.
#     MODULE_VERSION: Version of the module to create. Defaults to "any".
#     MODULE_PATH: Path to the module folder. Defaults to ".".
#     DST_DIRPATH: Path to the destination folder.
#     ARNOLD_PLUGIN_PATH: Path to the Arnold plugin folder. The path will be appended to the ARNOLD_PLUGIN_PATH environment variable.
#     MTOA_TEMPLATES_PATH: Path to the MtoA templates folder. The path will be appended to the MTOA_TEMPLATES_PATH environment variable.
#     MAYA_CUSTOM_TEMPATE_PATH: Path to the Maya custom template folder. The path will be appended to the MAYA_CUSTOM_TEMPLATE_PATH environment variable.
#
# ------------------------------------------------
function(generate_maya_module_file)
  cmake_parse_arguments(
    _args
    ""
    "MODULE_NAME;MODULE_VERSION;MODULE_PATH;DST_DIRPATH;ARNOLD_PLUGIN_PATH;MTOA_TEMPLATES_PATH;MAYA_CUSTOM_TEMPATE_PATH"
    ""
    ${ARGN}
  )
  # Check if the required arguments are provided
  if(NOT _args_MODULE_NAME)
    message(FATAL_ERROR "[generate_maya_module_file] MODULE_NAME is required")
  endif()

  if(NOT _args_DST_DIRPATH)
    message(FATAL_ERROR "[generate_maya_module_file] DST_DIRPATH is required")
  endif()

  # Set default values for optional arguments
  if(NOT _args_MODULE_VERSION)
    set(_args_MODULE_VERSION "any")
  endif()

  if(NOT _args_MODULE_PATH)
    set(_args_MODULE_PATH ".")
  endif()

  get_filename_component(
    SCRIPT_PATH "${CMAKE_CURRENT_FUNCTION_LIST_DIR}/../scripts/generate_maya_module_file.py" ABSOLUTE
  )
  execute_process(
    COMMAND python3 "${SCRIPT_PATH}"
      --module_name "${_args_MODULE_NAME}"
      --module_version "${_args_MODULE_VERSION}"
      --module_path "${_args_MODULE_PATH}"
      --dst_dirpath "${_args_DST_DIRPATH}"
      --arnold_plugin_path "${_args_ARNOLD_PLUGIN_PATH}"
      --mtoa_templates_path "${_args_MTOA_TEMPLATES_PATH}"
      --maya_custom_template_path "${_args_MAYA_CUSTOM_TEMPATE_PATH}"
    RESULT_VARIABLE _result
  )
  if(NOT _result EQUAL 0)
    message(FATAL_ERROR "Error while executing the script generate_maya_module_file.py")
  endif()
endfunction()
