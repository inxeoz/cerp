import frappe
from typing import List, Dict, Union, Any

def create_role_profile(role_profiles_data: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create role profiles with flexible configuration
    
    Example Data Structures:
    
    # Single Role Profile Configuration
    single_role_profile = {
        "role_profile": "Project Management Profile",      # Unique profile name (corrected field name)
        "description": "Role profile for project managers", # Optional description
        "roles": [                                          # List of roles
            {"role": "Project Manager"},
            {"role": "Project Coordinator"}
        ]
    }
    
    # Multiple Role Profiles Configuration
    multiple_role_profiles = [
        {
            "role_profile": "Sales Management Profile",
            "roles": [
                {"role": "Sales Executive"},
                {"role": "Sales Manager"}
            ]
        },
        {
            "role_profile": "HR Management Profile",
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
        
        # Ensure role_profiles_data is a list
        if isinstance(role_profiles_data, dict):
            role_profiles_data = [role_profiles_data]
        
        created_role_profiles = []
        existing_role_profiles = []
        errors = []
        
        for profile_config in role_profiles_data:
            # Support both 'role_profile' and 'role_profile_name' for backward compatibility
            profile_name = profile_config.get('role_profile') or profile_config.get('role_profile_name')
            
            if not profile_name:
                errors.append("Profile name is missing in configuration")
                continue
            
            # Check if role profile exists
            if not frappe.db.exists("Role Profile", profile_name):
                try:
                    # Create new Role Profile document
                    new_profile = frappe.new_doc("Role Profile")
                    new_profile.role_profile = profile_name
                    
                    # Add description if provided (custom field - may not exist)
                    if 'description' in profile_config and hasattr(new_profile, 'description'):
                        new_profile.description = profile_config.get('description', '')
                    
                    # Prepare roles for the profile
                    for role_data in profile_config.get('roles', []):
                        # Handle both string and dict formats
                        if isinstance(role_data, str):
                            role_name = role_data
                        else:
                            role_name = role_data.get('role')
                        
                        # Verify role exists before adding
                        if role_name and frappe.db.exists("Role", role_name):
                            new_profile.append("roles", {"role": role_name})
                        else:
                            errors.append(f"Role '{role_name}' does not exist")
                    
                    # Insert the role profile
                    new_profile.insert(ignore_permissions=True)
                    created_role_profiles.append(profile_name)
                    
                except Exception as profile_error:
                    error_msg = f"Error creating role profile '{profile_name}': {str(profile_error)}"
                    frappe.log_error(error_msg, "Role Profile Creation")
                    errors.append(error_msg)
            else:
                existing_role_profiles.append(profile_name)
        
        # Commit changes to database
        frappe.db.commit()
        
        return {
            "status": "success" if not errors else "partial",
            "created_role_profiles": created_role_profiles,
            "existing_role_profiles": existing_role_profiles,
            "errors": errors,
            "summary": {
                "created": len(created_role_profiles),
                "existing": len(existing_role_profiles),
                "errors": len(errors)
            }
        }
    
    except Exception as e:
        frappe.log_error(f"Role Profile Creation Error: {str(e)}", "Role Profile Creation")
        return {
            "status": "error",
            "message": str(e),
            "created_role_profiles": [],
            "existing_role_profiles": [],
            "errors": [str(e)]
        }


def _get_default_role_profiles() -> List[Dict[str, Any]]:
    """
    Returns default role profiles configuration
    """
    return [
        {
            "role_profile": "Administrator Profile",
            "roles": [
                {"role": "System Manager"},
                {"role": "Administrator"}
            ]
        },
        {
            "role_profile": "Sales Profile",
            "roles": [
                {"role": "Sales User"},
                {"role": "Sales Manager"}
            ]
        },
        {
            "role_profile": "Purchase Profile",
            "roles": [
                {"role": "Purchase User"},
                {"role": "Purchase Manager"}
            ]
        },
        {
            "role_profile": "Accounts Profile",
            "roles": [
                {"role": "Accounts User"},
                {"role": "Accounts Manager"}
            ]
        }
    ]


# Example usage functions
def create_single_role_profile():
    """Example: Create a single role profile"""
    single_profile = {
        "role_profile": "Project Management Profile",
        "roles": [
            {"role": "Projects User"},
            {"role": "Projects Manager"}
        ]
    }
    
    result = create_role_profile([single_profile])
    print(f"Result: {result}")
    return result


def create_multiple_role_profiles():
    """Example: Create multiple role profiles"""
    profiles = [
        {
            "role_profile": "Quality Control Profile",
            "roles": ["Quality Manager", "Stock User"]  # Can use strings directly
        },
        {
            "role_profile": "Support Team Profile",
            "roles": [
                {"role": "Support Team"},
                {"role": "Customer"}
            ]
        }
    ]
    
    result = create_role_profile(profiles)
    print(f"Result: {result}")
    return result


def list_existing_role_profiles():
    """Helper function to list existing role profiles"""
    role_profiles = frappe.get_all(
        "Role Profile",
        fields=["name", "role_profile"],
        order_by="creation desc"
    )
    
    print("\nExisting Role Profiles:")
    print("-" * 50)
    for profile in role_profiles:
        # Get roles for this profile
        roles = frappe.get_all(
            "Has Role",
            filters={"parent": profile.name, "parenttype": "Role Profile"},
            fields=["role"]
        )
        role_names = [r.role for r in roles]
        print(f"{profile.role_profile}: {', '.join(role_names)}")
    
    return role_profiles


# # Run examples
# if __name__ == "__main__":
#     # Create default role profiles
#     print("Creating default role profiles...")
#     result = create_role_profile()
#     print(f"Default profiles result: {result}")
    
#     # List existing profiles
#     list_existing_role_profiles()