import frappe
from typing import List, Dict, Union, Any

def create_workspace(
    workspace_config: Union[Dict[str, Any], List[Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """
    Create workspace(s) with flexible configuration
    
    Example Data Structures:
    
    # Single Workspace Configuration
    single_workspace = {
        "name": "Project Workspace",           # Unique identifier (optional)
        "label": "Project Dashboard",          # Display label (required)
        "title": "Project Management",         # Page title (optional)
        "module": "Projects",                  # Frappe module (default: 'Desk')
        "public": 1,                           # Public visibility (default: 1)
        "is_hidden": 0,                        # Hidden status (default: 0)
        "is_default": 0,                       # Default workspace (default: 0)
        "icon": "project",                     # Workspace icon
        "restrict_to_domain": "",              # Domain restriction
        "content": '''[                        # Workspace content (JSON)
            {
                "type": "header",
                "value": "Project Management Dashboard"
            },
            {
                "type": "paragraph",
                "value": "Overview of all project-related activities"
            }
        ]'''
    }
    
    # Multiple Workspace Configuration
    multiple_workspaces = [
        {
            "name": "Sales Workspace",
            "label": "Sales Dashboard",
            "title": "Sales Insights",
            "module": "Selling",
            "public": 1,
            "icon": "sales"
        },
        {
            "name": "HR Workspace",
            "label": "HR Dashboard",
            "title": "Human Resources",
            "module": "HR",
            "public": 1,
            "icon": "employee"
        }
    ]
    
    Args:
        workspace_config (Dict or List[Dict], optional): Workspace configuration(s)
    
    Returns:
        Dict containing creation details
    """
    
    try:
        # If no config provided, use default
        if workspace_config is None:
            workspace_config = _get_default_workspace_config()
        
        # Ensure workspace_config is a list
        if isinstance(workspace_config, dict):
            workspace_config = [workspace_config]
        
        created_workspaces = []
        existing_workspaces = []
        error_workspaces = []
        
        for workspace_data in workspace_config:
            # Validate required fields
            workspace_name = workspace_data.get('name') or workspace_data.get('label')
            
            if not workspace_name:
                error_workspaces.append({
                    "error": "Workspace name or label is required",
                    "data": workspace_data
                })
                continue
            
            # Check if workspace exists
            if frappe.db.exists("Workspace", workspace_name):
                existing_workspaces.append(workspace_name)
                continue
            
            try:
                # Prepare workspace configuration
                workspace_doc = frappe.get_doc({
                    "doctype": "Workspace",
                    "name": workspace_name,
                    "label": workspace_data.get('label', workspace_name),
                    "title": workspace_data.get('title', workspace_name),
                    "module": workspace_data.get('module', 'Desk'),
                    "public": workspace_data.get('public', 1),
                    "is_hidden": workspace_data.get('is_hidden', 0),
                    "is_default": workspace_data.get('is_default', 0),
                    "icon": workspace_data.get('icon', 'music'),
                    "restrict_to_domain": workspace_data.get('restrict_to_domain', ''),
                    "content": workspace_data.get('content', '[]')
                })
                
                # Add custom fields if provided
                for key, value in workspace_data.items():
                    if key not in [
                        'name', 'label', 'title', 'module', 'public', 
                        'is_hidden', 'is_default', 'icon', 
                        'restrict_to_domain', 'content'
                    ]:
                        setattr(workspace_doc, key, value)
                
                # Insert workspace
                workspace_doc.insert(ignore_permissions=True)
                created_workspaces.append(workspace_name)
            
            except Exception as workspace_error:
                error_workspaces.append({
                    "workspace": workspace_name,
                    "error": str(workspace_error),
                    "data": workspace_data
                })
        
        # Commit changes
        frappe.db.commit()
        
        # Clear cache to ensure immediate visibility
        frappe.clear_cache()
        
        return {
            "status": "success",
            "created_workspaces": created_workspaces,
            "existing_workspaces": existing_workspaces,
            "error_workspaces": error_workspaces
        }
    
    except Exception as e:
        frappe.log_error(f"Workspace Creation Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }

def _get_default_workspace_config() -> List[Dict[str, Any]]:
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
                }
            ]'''
        }
    ]

def create_multiple_workspaces(
    workspace_configs: List[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Create multiple workspaces
    
    Args:
        workspace_configs (List[Dict], optional): List of workspace configurations
    
    Returns:
        Dict containing creation details for multiple workspaces
    """
    return create_workspace(workspace_configs)

# Expose as whitelisted method
@frappe.whitelist()
def setup_workspaces(workspace_configs=None):
    """
    Publicly accessible method to create workspaces
    """
    return create_workspace(workspace_configs)

# Example usage function
def workspace_setup_example():
    """
    Example of creating multiple workspaces
    """
    workspace_configs = [
        {
            "name": "Project Workspace",
            "label": "Project Dashboard",
            "title": "Project Management",
            "module": "Projects",
            "public": 1,
            "icon": "music",
            "content": '''[
                {
                    "type": "header",
                    "value": "Project Management Dashboard"
                },
                {
                    "type": "paragraph",
                    "value": "Overview of all project-related activities"
                }
            ]'''
        },
        {
            "name": "Sales Workspace",
            "label": "Sales Dashboard",
            "title": "Sales Insights",
            "module": "Selling",
            "public": 1,
            "icon": "music",
            "content": '''[
                {
                    "type": "header",
                    "value": "Sales Performance Dashboard"
                },
                {
                    "type": "paragraph",
                    "value": "Comprehensive sales performance tracking"
                }
            ]'''
        }
    ]
    
    return create_multiple_workspaces(workspace_configs)