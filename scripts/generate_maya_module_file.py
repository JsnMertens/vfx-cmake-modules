# -*- coding: utf-8 -*-
"""
Script that generated a Maya module description file (.mod) for a given project.
"""

import argparse
import os


def main():
    """Generate Maya module description file for a given project."""

    parser = argparse.ArgumentParser(
        description="Generate Maya module description file for a given project."
    )
    parser.add_argument(
        "--module_name",
        help="Name of the module to create.",
        required=True,
    )
    parser.add_argument(
        "--module_version",
        help="Version of the module to create.",
        default="any",
        required=False
    )
    parser.add_argument(
        "--module_path",
        help="Path to the module folder.",
        default=".",
        required=False,
    )
    parser.add_argument(
        "--dst_dirpath",
        help="Path to the destination folder.",
        required=True,
    )
    parser.add_argument(
        "--arnold_plugin_path",
        help="Path to the Arnold plugin folder.",
        default=None,
        required=False,
    )
    parser.add_argument(
        "--mtoa_templates_path",
        help="Path to the MtoA templates folder.",
        default=None,
        required=False,
    )
    parser.add_argument(
        "--maya_custom_template_path",
        help="Path to the Maya custom template folder.",
        default=None,
        required=False,
    )
    args = parser.parse_args()

    print(f"Creating module description file for {args.arnold_plugin_path} in")

    # Create the module description file
    _generate_module(
        args.module_name,
        args.dst_dirpath,
        args.module_version,
        args.module_path,
        args.arnold_plugin_path,
        args.mtoa_templates_path,
        args.maya_custom_template_path
    )


def _generate_module(
        module_name,
        dst_dirpath,
        module_version="any",
        module_path=".",
        arnold_plugin_path=None,
        mtoa_templates_path=None,
        maya_custom_template_path=None
    ):
    """Generate Maya module description file for a given project.
    
    Args:
        module_name (str): Name of the module to create. The name should not contain extension.
        dst_dirpath (str): Path to the destination folder.
        module_version (str, optional): Version of the module to create. Defaults to "any".
        module_path (str, optional): Path to the module folder. Defaults to ".".
        arnold_plugin_path (str, optional): Path to the Arnold plugin folder.
            The path will be appended to the ARNOLD_PLUGIN_PATH environment variable.
        mtoa_templates_path (str, optional): Path to the MtoA templates folder.
            The path will be appended to the MTOA_TEMPLATES_PATH environment variable.
        maya_custom_template_path (str, optional): Path to the Maya custom template folder.
            The path will be appended to the MAYA_CUSTOM_TEMPLATE_PATH environment variable.
    """
    if not os.path.exists(dst_dirpath):
        os.makedirs(dst_dirpath)

    print(f"Creating module description file for {module_name} in {arnold_plugin_path}")

    # Create the module description file
    with open(os.path.join(dst_dirpath, f"{module_name}.mod"), "w") as f:
        f.write(f"+ {module_name} {module_version} {module_path}\n")
        if arnold_plugin_path:
            f.write(f"ARNOLD_PLUGIN_PATH +:= {arnold_plugin_path}\n")
        if mtoa_templates_path:
            f.write(f"MTOA_TEMPLATES_PATH +:= {mtoa_templates_path}\n")
        if maya_custom_template_path:
            f.write(f"MAYA_CUSTOM_TEMPLATE_PATH +:= {maya_custom_template_path}\n")


if __name__ == "__main__":
    main()
