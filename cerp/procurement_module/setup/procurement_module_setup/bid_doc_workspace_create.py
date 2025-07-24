import frappe
from typing import List, Dict, Any
from cerp.procurement_module.setup.default_setup_methods.create_workspace import create_workspace

def example_workspace_config() -> List[Dict[str, Any]]:
    """
    Retrieve default workspace configurations
    
    Returns:
        List of default workspace configurations
    """
    return [
        {
            "name": "Simple Workspace",
            "label": "Simple Workspace",
            "title": "Simple Workspace",
            "module": "Desk",
            "public": 1,
            "is_hidden": 0,
            "is_default": 1,
            "icon": "music",
            "restrict_to_domain": "",
            "content": '''[
                {
                    "type": "header",
                    "value": "Welcome to Simple Workspace"
                },
                {
                    "type": "paragraph",
                    "value": "This is a public workspace visible to all users."
                },
                {
                    "type" : "custom_block",
                    "value" : "info_about_user"
                }
               
            ]'''
        }
    ]

def create_bid_workspace():

    return create_workspace(example_workspace_config())

