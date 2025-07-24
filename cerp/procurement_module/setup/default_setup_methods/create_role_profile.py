import frappe
from typing import List, Dict, Union, Any

def create_role_profile(role_profiles_data: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create role profiles with flexible configuration
    
    Example Data Structures:
    
    # Single Role Profile Configuration
    single_role_profile = {
        "role_profile_name": "Project Management Profile",  # Unique profile name
        "description": "Role profile for project managers", # Optional description
        "roles": [                                          # List of roles
            {"role": "Project Manager"},
            {"role": "Project Coordinator"}
        ]
    }
    
    # Multiple Role Profiles Configuration
    multiple_role_profiles = [
        {
            "role_profile_name": "Sales Management Profile",
            "roles": [
                {"role": "Sales Executive"},
                {"role": "Sales Manager"}
            ]
        },
        {
            "role_profile_name": "HR Management Profile",
            "roles": [
                {"role": "HR Manager"},
                {"role": "HR Coordinator"}
            ]
        }
    ]
    
    Args:
        role_profiles_data (List[Dict], optional): List of role profile configurations
    
    Returns:
        Dict containing creation details
    """
    try:
        # If no data provided, use default method
        if role_profiles_data is None:
            role_profiles_data = _get_default_role_profiles()
        
        created_role_profiles = []
        existing_role_profiles = []
        
        for profile_config in role_profiles_data:
            profile_name = profile_config.get('role_profile_name')
            
            if not profile_name:
                continue
            
            # Check if role profile exists
            if not frappe.db.exists("Role Profile", profile_name):
                try:
                    # Prepare roles for the profile
                    profile_roles = []
                    for role in profile_config.get('roles', []):
                        # Ensure role exists before adding to profile
                        if isinstance(role, str):
                            role = {"role": role}
                        
                        # Verify role exists
                        if frappe.db.exists("Role", role.get('role')):
                            profile_roles.append(role)
                    
                    new_profile = frappe.get_doc({
                        "doctype": "Role Profile",
                        "role_profile_name": profile_name,
                        "description": profile_config.get('description', ''),
                        "roles": profile_roles
                    }).insert(ignore_permissions=True)
                    
                    created_role_profiles.append(profile_name)
                except Exception as profile_error:
                    frappe.log_error(f"Error creating role profile {profile_name}: {str(profile_error)}")
            else:
                existing_role_profiles.append(profile_name)
        
        frappe.db.commit()
        
        return {
            "status": "success",
            "created_role_profiles": created_role_profiles,
            "existing_role_profiles": existing_role_profiles
        }
    
    except Exception as e:
        frappe.log_error(f"Role Profile Creation Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }
