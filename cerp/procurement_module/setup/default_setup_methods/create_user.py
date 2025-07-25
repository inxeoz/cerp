import frappe
from typing import List, Dict, Union, Any

def create_user(user_data: Union[Dict[str, Any], List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """
    Create user with flexible configuration
    
    Example Data Structures:
    
    # Single user Configuration
    single_user = {
        "user_first_name": "Ravi",                         # Required 
        "user_email": "inxeoz@inxeoz.com",                # Required
        "role_profile_name": "Procurement Officer Profile"  # Role Profile not Role,
        "new_password" : "asd@123"
    }
    
    # Multiple user Configuration
    multiple_user = [
        {
            "user_first_name": "Ravi",                         # Required 
            "user_email": "inxeoz@inxeoz.com",                # Required
            "role_profile_name": "Procurement Officer Profile"  # Role Profile not Role,
            "new_password" : "asd@123"
        },
        {
            "user_first_name": "Kishan",                       # Required 
            "user_email": "kishan@inxeoz.com",                # Required
            "role_profile_name": "Procurement Officer Profile"  # Role Profile not Role,
            "new_password" : "asd@123"
        }
    ]
    
    Args:
        user_data (Dict or List[Dict], optional): Single user dict or list of user configurations
    
    Returns:
        Dict containing creation details
    """
    
    try:
        # If no data provided, use default method
        if user_data is None:
            user_data = _get_default_user()
        
        # Ensure user_data is a list
        if isinstance(user_data, dict):
            user_data = [user_data]
        
        created_users = []
        existing_users = []
        errors = []
        
        for user_config in user_data:
            user_email = user_config.get('user_email')
            user_first_name = user_config.get('user_first_name')
            role_profile_name = user_config.get('role_profile_name')
            
            # Validate required fields
            if not user_email:
                errors.append("User email is required")
                continue
            
            if not user_first_name:
                errors.append(f"First name is required for user {user_email}")
                continue
            
            # Check if user exists
            if not frappe.db.exists("User", user_email):
                try:
                    # Create new user document
                    new_user = frappe.new_doc("User")
                    new_user.email = user_email
                    new_user.first_name = user_first_name
                    new_user.enabled = 1
                    new_user.send_welcome_email = 0  # Disable welcome email for bulk creation
                    
                    # Set additional fields if provided
                    if user_config.get('user_last_name'):
                        new_user.last_name = user_config.get('user_last_name')
                    
                    if user_config.get('user_mobile'):
                        new_user.mobile_no = user_config.get('user_mobile')

                                        # Set additional fields if provided
                    if user_config.get('new_password'):
                        new_user.new_password = user_config.get('new_password')
                    
                    # Insert the user
                    new_user.insert(ignore_permissions=True)
                    
                    # Assign role profile if provided and exists
                    if role_profile_name and frappe.db.exists("Role Profile", role_profile_name):
                        new_user.role_profile_name = role_profile_name
                        new_user.save(ignore_permissions=True)
                        
                        # Apply roles from role profile
                        apply_role_profile_to_user(new_user.name, role_profile_name)
                    elif role_profile_name:
                        errors.append(f"Role Profile '{role_profile_name}' does not exist for user {user_email}")
                    
                    created_users.append(user_email)
                    
                except Exception as user_error:
                    error_msg = f"Error creating user {user_email}: {str(user_error)}"
                    frappe.log_error(error_msg, "User Creation Error")
                    errors.append(error_msg)
            else:
                existing_users.append(user_email)
        
        # Commit changes
        frappe.db.commit()
        
        return {
            "status": "success" if not errors else "partial",
            "created_users": created_users,
            "existing_users": existing_users,
            "errors": errors,
            "summary": {
                "created": len(created_users),
                "existing": len(existing_users),
                "errors": len(errors)
            }
        }
    
    except Exception as e:
        frappe.log_error(f"User Creation Error: {str(e)}", "User Creation Error")
        return {
            "status": "error",
            "message": str(e),
            "created_users": [],
            "existing_users": [],
            "errors": [str(e)]
        }


def apply_role_profile_to_user(user_email: str, role_profile_name: str) -> bool:
    """
    Apply roles from a role profile to a user
    """
    try:
        # Get the role profile
        role_profile = frappe.get_doc("Role Profile", role_profile_name)
        
        # Get the user
        user = frappe.get_doc("User", user_email)
        
        # Clear existing roles (optional, remove if you want to keep existing roles)
        # user.roles = []
        
        # Apply roles from role profile
        for role in role_profile.roles:
            if not any(r.role == role.role for r in user.roles):
                user.append("roles", {
                    "role": role.role
                })
        
        user.save(ignore_permissions=True)
        return True
        
    except Exception as e:
        frappe.log_error(f"Error applying role profile: {str(e)}", "Role Profile Application")
        return False


def _get_default_user() -> List[Dict[str, Any]]:
    """
    Returns default user configuration
    """
    return [
        {
            "user_first_name": "Test",
            "user_last_name": "User",
            "user_email": "testuser@example.com",
            "role_profile_name": "Employee"
        }
    ]


# Enhanced version with more features
def create_user_advanced(user_data: Union[Dict[str, Any], List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """
    Create user with advanced configuration options
    
    Example:
    user_data = {
        "user_first_name": "John",
        "user_last_name": "Doe",
        "user_email": "john.doe@example.com",
        "user_mobile": "+1234567890",
        "role_profile_name": "Sales Manager Profile",
        "user_type": "System User",  # or "Website User"
        "language": "en",
        "time_zone": "America/New_York",
        "additional_roles": ["Sales User", "Stock User"],  # Additional individual roles
        "user_groups": ["Sales Team", "Management"],  # User groups to assign
        "module_profile": "Sales",  # Module profile to assign
        "send_welcome_email": False,
        "password": "SecurePassword123!"  # Optional, will generate if not provided
    }
    """
    
    try:
        if user_data is None:
            user_data = _get_default_user()
        
        if isinstance(user_data, dict):
            user_data = [user_data]
        
        created_users = []
        existing_users = []
        errors = []
        
        for user_config in user_data:
            user_email = user_config.get('user_email')
            
            if not user_email:
                errors.append("User email is required")
                continue
            
            if frappe.db.exists("User", user_email):
                existing_users.append(user_email)
                continue
            
            try:
                # Create user with all available fields
                new_user = frappe.new_doc("User")
                
                # Required fields
                new_user.email = user_email
                new_user.first_name = user_config.get('user_first_name', 'User')
                
                # Optional fields
                optional_fields = [
                    ('last_name', 'user_last_name'),
                    ('mobile_no', 'user_mobile'),
                    ('user_type', 'user_type'),
                    ('language', 'language'),
                    ('time_zone', 'time_zone'),
                    ('module_profile', 'module_profile'),
                    ('home_page_link', 'home_page_link'),
                    ('gender', 'gender'),
                    ('birth_date', 'birth_date')
                ]
                
                for field_name, config_key in optional_fields:
                    if config_key in user_config:
                        setattr(new_user, field_name, user_config[config_key])
                
                # Set password if provided, otherwise it will be auto-generated
                if user_config.get('password'):
                    new_user.new_password = user_config['password']
                
                # Control welcome email
                new_user.send_welcome_email = user_config.get('send_welcome_email', 0)
                
                # Set enabled status
                new_user.enabled = user_config.get('enabled', 1)
                
                # Insert user
                new_user.insert(ignore_permissions=True)
                
                # Apply role profile
                if user_config.get('role_profile_name'):
                    if frappe.db.exists("Role Profile", user_config['role_profile_name']):
                        new_user.role_profile_name = user_config['role_profile_name']
                        new_user.save(ignore_permissions=True)
                        apply_role_profile_to_user(new_user.name, user_config['role_profile_name'])
                
                # Apply additional individual roles
                if user_config.get('additional_roles'):
                    for role in user_config['additional_roles']:
                        if frappe.db.exists("Role", role):
                            new_user.append("roles", {"role": role})
                    new_user.save(ignore_permissions=True)
                
                # Add to user groups
                if user_config.get('user_groups'):
                    for group in user_config['user_groups']:
                        if frappe.db.exists("User Group", group):
                            frappe.get_doc("User Group", group).append_users(new_user.name)
                
                created_users.append({
                    "email": user_email,
                    "name": new_user.name,
                    "full_name": new_user.full_name
                })
                
            except Exception as e:
                error_msg = f"Error creating user {user_email}: {str(e)}"
                errors.append(error_msg)
                frappe.log_error(error_msg, "User Creation Error")
        
        frappe.db.commit()
        
        return {
            "status": "success" if not errors else "partial",
            "created_users": created_users,
            "existing_users": existing_users,
            "errors": errors,
            "summary": {
                "created": len(created_users),
                "existing": len(existing_users),
                "errors": len(errors)
            }
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "created_users": [],
            "existing_users": [],
            "errors": [str(e)]
        }


# # Usage examples
# if __name__ == "__main__":
#     # Example 1: Create single user
#     single_user = {
#         "user_first_name": "Ravi",
#         "user_email": "ravi@inxeoz.com",
#         "role_profile_name": "Procurement Officer Profile"
#     }
#     result = create_user(single_user)
#     print(f"Single user result: {result}")
    
#     # Example 2: Create multiple users
#     multiple_users = [
#         {
#             "user_first_name": "Ravi",
#             "user_email": "ravi@inxeoz.com",
#             "role_profile_name": "Procurement Officer Profile"
#         },
#         {
#             "user_first_name": "Kishan",
#             "user_email": "kishan@inxeoz.com",
#             "role_profile_name": "Procurement Officer Profile"
#         }
#     ]
#     result = create_user(multiple_users)
#     print(f"Multiple users result: {result}")