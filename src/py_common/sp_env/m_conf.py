"""Environmental configuration module."""

# Imports
import os
import yaml
from py_common.sp_file import m_file
from py_common.sp_file import m_dir


def get_env_config_base():
    """Get environmental configruration.

    Returns:
        dict: dictionary with following project environmental parematers: project_name, env_log_dir, env_conf_dir, env_dcv_dir log_level
    """
    with open(os.path.join("config", "env.yml"), "r") as file:
        f = yaml.safe_load(file)

    return {
        "project_name": f["PROJECT_NAME"],
        "env_log_dir": os.path.expanduser(f["ENV_LOG_DIR"]),
        "env_conf_dir": os.path.expanduser(f["ENV_CONF_DIR"]),
        "env_dcv_dir": os.path.expanduser(f["ENV_DCV_DIR"]),
        "log_level": f["LOG_LEVEL"],
    }


def generate_env_config_paths():
    """Generate and write to file paths based on general config.

    Returns:
        int: Error number
    """
    cfg = get_env_config_base()

    # Create base repository directories

    repo_dir = os.getcwd()
    repo_tls_dir = os.path.join(repo_dir, "tools")
    repo_bld_dir = os.path.join(repo_dir, "build")
    repo_src_dir = os.path.join(repo_dir, "src")
    repo_conf_dir = os.path.join(repo_dir, "config")
    repo_docs_dir = os.path.join(repo_dir, "docs")

    conf_dir = os.path.join(cfg["env_conf_dir"], cfg["project_name"])
    dcv_dir = os.path.join(cfg["env_dcv_dir"], cfg["project_name"])

    path_to_paths_file = os.path.join(conf_dir, "paths.yml")
    m_dir.create_dir_if_not_exist(conf_dir)
    m_file.create_new_file(path_to_paths_file)

    m_file.overwrite_line_with_matching_prefix_to_file(path_to_paths_file, "REPO_DIR: ", repo_dir)
    m_file.overwrite_line_with_matching_prefix_to_file(path_to_paths_file, "REPO_TLS_DIR: ", repo_tls_dir)
    m_file.overwrite_line_with_matching_prefix_to_file(path_to_paths_file, "REPO_BLD_DIR: ", repo_bld_dir)
    m_file.overwrite_line_with_matching_prefix_to_file(path_to_paths_file, "REPO_SRC_DIR: ", repo_src_dir)
    m_file.overwrite_line_with_matching_prefix_to_file(path_to_paths_file, "REPO_CONF_DIR: ", repo_conf_dir)
    m_file.overwrite_line_with_matching_prefix_to_file(path_to_paths_file, "REPO_DOCS_DIR: ", repo_docs_dir)
    m_file.overwrite_line_with_matching_prefix_to_file(path_to_paths_file, "CONF_DIR: ", conf_dir)
    m_file.overwrite_line_with_matching_prefix_to_file(path_to_paths_file, "DCV_DIR: ", dcv_dir)

    return 0


def get_env_config_paths():
    """Get environmental paths configruration from generated environmental config paths.

    Returns:
        dict: dictionary with following project environmental parematers:
            repo_dir,
            repo_tls_dir,
            repo_bld_dir,
            repo_src_dir,
            repo_conf_dir,
            repo_docs_dir,
            conf_dir,
            dcv_dir
    """
    cfg = get_env_config_base()
    path_to_paths_file = os.path.join(cfg["env_conf_dir"], cfg["project_name"], "paths.yml")
    with open(path_to_paths_file, "r") as file:
        f = yaml.safe_load(file)
    return {
        "repo_dir": os.path.expanduser(f["REPO_DIR"]),
        "repo_tls_dir": os.path.expanduser(f["REPO_TLS_DIR"]),
        "repo_bld_dir": os.path.expanduser(f["REPO_BLD_DIR"]),
        "repo_src_dir": os.path.expanduser(f["REPO_SRC_DIR"]),
        "repo_conf_dir": os.path.expanduser(f["REPO_CONF_DIR"]),
        "repo_docs_dir": os.path.expanduser(f["REPO_DOCS_DIR"]),
        "conf_dir": os.path.expanduser(f["CONF_DIR"]),
        "dcv_dir": os.path.expanduser(f["DCV_DIR"]),
    }


def get_env_conf_all():
    """Get general config and paths environemental config.

    Returns:
        dict: dictionary consisting of general and paths environmetal configs
    """
    cfg = get_env_config_base()
    paths = get_env_config_paths()
    return cfg.update(paths)
