import frappe
from typing import List, Dict, Union, Any

def create_role(roles_data: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create roles with flexible configuration
    
    Example Data Structures:
    
    # Single Role Configuration
    single_role = {
        "role_name": "Project Manager",        # Required unique role name
        "desk_access": 1,                      # Desktop access (default: 1)
        "disabled": 0,                         # Role disabled status (default: 0)
        "description": "Manages project details" # Optional description
    }
    
    # Multiple Roles Configuration
    multiple_roles = [
        {
            "role_name": "Sales Executive",
            "desk_access": 1,
            "description": "Handles sales activities"
        },
        {
            "role_name": "HR Manager",
            "desk_access": 1,
            "description": "Manages human resources"
        }
    ]
    
    Args:
        roles_data (List[Dict], optional): List of role configurations
    
    Returns:
        Dict containing creation details
    """
    
    try:
        # If no data provided, use default method
        if roles_data is None:
            roles_data = _get_default_roles()
        
        created_roles = []
        existing_roles = []
        
        for role_config in roles_data:
            role_name = role_config.get('role_name')
            
            if not role_name:
                continue
            
            # Check if role exists
            if not frappe.db.exists("Role", role_name):
                try:
                    new_role = frappe.get_doc({
                        "doctype": "Role",
                        "role_name": role_name,
                        "desk_access": role_config.get('desk_access', 1),
                        "disabled": role_config.get('disabled', 0),
                        "description": role_config.get('description', '')
                    }).insert(ignore_permissions=True)
                    
                    created_roles.append(role_name)
                except Exception as role_error:
                    frappe.log_error(f"Error creating role {role_name}: {str(role_error)}")
            else:
                existing_roles.append(role_name)
        
        frappe.db.commit()
        
        return {
            "status": "success",
            "created_roles": created_roles,
            "existing_roles": existing_roles
        }
    
    except Exception as e:
        frappe.log_error(f"Role Creation Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }


    """
    Publicly accessible method to trigger workflow component setup
    """
    return comprehensive_workflow_setup(
        roles_data,
        role_profiles_data,
        workflow_states_data,
        workflow_actions_data,
        workflow_data
    )