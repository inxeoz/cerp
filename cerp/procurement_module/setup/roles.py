import frappe

def get_roles_with_parameters():
    """Returns roles configuration with all available parameters"""
    
    roles_config = [
        {
            "role_name": "Procurement Officer",
            "home_page": "/app/bid-document",
            "route": "/app",
            "restrict_to_domain": "",
            "disabled": 0,
            "is_custom": 1,
            "desk_access": 1,
            "two_factor_auth": 0,
            "search_bar": 1,
            "notifications": 1,
            "list_sidebar": 1,
            "bulk_actions": 1,
            "view_switcher": 1,
            "form_sidebar": 1,
            "timeline": 1,
            "dashboard": 1,
            "kanban_boards": 1
        },
        {
            "role_name": "Managing Director",
            "home_page": "/app/dashboard/management-overview",
            "route": "/app",
            "restrict_to_domain": "",
            "disabled": 0,
            "is_custom": 1,
            "desk_access": 1,
            "two_factor_auth": 1,  # Enforce 2FA for sensitive roles
            "search_bar": 1,
            "notifications": 1,
            "list_sidebar": 1,
            "bulk_actions": 1,
            "view_switcher": 1,
            "form_sidebar": 1,
            "timeline": 1,
            "dashboard": 1,
            "kanban_boards": 1
        },
        {
            "role_name": "Chief General Manager",
            "home_page": "/app/dashboard/operations-dashboard",
            "route": "/app",
            "restrict_to_domain": "",
            "disabled": 0,
            "is_custom": 1,
            "desk_access": 1,
            "two_factor_auth": 1,
            "search_bar": 1,
            "notifications": 1,
            "list_sidebar": 1,
            "bulk_actions": 1,
            "view_switcher": 1,
            "form_sidebar": 1,
            "timeline": 1,
            "dashboard": 1,
            "kanban_boards": 1
        },
        {
            "role_name": "Project Director",
            "home_page": "/app/project",
            "route": "/app",
            "restrict_to_domain": "",
            "disabled": 0,
            "is_custom": 1,
            "desk_access": 1,
            "two_factor_auth": 0,
            "search_bar": 1,
            "notifications": 1,
            "list_sidebar": 1,
            "bulk_actions": 1,
            "view_switcher": 1,
            "form_sidebar": 1,
            "timeline": 1,
            "dashboard": 1,
            "kanban_boards": 1
        },
        {
            "role_name": "Marketing Team",
            "home_page": "/app/bid-document",
            "route": "/app",
            "restrict_to_domain": "Marketing",
            "disabled": 0,
            "is_custom": 1,
            "desk_access": 1,
            "two_factor_auth": 0,
            "search_bar": 1,
            "notifications": 1,
            "list_sidebar": 1,
            "bulk_actions": 0,  # Limited bulk actions
            "view_switcher": 1,
            "form_sidebar": 1,
            "timeline": 1,
            "dashboard": 0,
            "kanban_boards": 1
        },
        {
            "role_name": "Vendor",
            "home_page": "/app/vendor-portal",
            "route": "/app/vendor-portal",
            "restrict_to_domain": "Vendor Portal",
            "disabled": 0,
            "is_custom": 1,
            "desk_access": 0,  # No desk access for vendors
            "two_factor_auth": 0,
            "search_bar": 0,
            "notifications": 1,
            "list_sidebar": 0,
            "bulk_actions": 0,
            "view_switcher": 0,
            "form_sidebar": 0,
            "timeline": 0,
            "dashboard": 0,
            "kanban_boards": 0
        }
    ]
    
    return roles_config

def create_roles_with_parameters():
    """Create roles with all parameters in the system"""
    
    roles = get_roles_with_parameters()
    created_roles = []
    
    print("Creating roles with parameters...\n")
    
    for role_config in roles:
        role_name = role_config["role_name"]
        
        try:
            if not frappe.db.exists("Role", role_name):
                # Create new role
                role = frappe.get_doc({
                    "doctype": "Role",
                    "role_name": role_name,
                    "home_page": role_config.get("home_page"),
                    "restrict_to_domain": role_config.get("restrict_to_domain"),
                    "disabled": role_config.get("disabled", 0),
                    "is_custom": role_config.get("is_custom", 1),
                    "desk_access": role_config.get("desk_access", 1),
                    "two_factor_auth": role_config.get("two_factor_auth", 0),
                    "search_bar": role_config.get("search_bar", 1),
                    "notifications": role_config.get("notifications", 1),
                    "list_sidebar": role_config.get("list_sidebar", 1),
                    "bulk_actions": role_config.get("bulk_actions", 1),
                    "view_switcher": role_config.get("view_switcher", 1),
                    "form_sidebar": role_config.get("form_sidebar", 1),
                    "timeline": role_config.get("timeline", 1),
                    "dashboard": role_config.get("dashboard", 1)
                })
                
                role.insert(ignore_permissions=True)
                created_roles.append(role_name)
                print(f"✓ Created role: {role_name}")
            else:
                # Update existing role
                role = frappe.get_doc("Role", role_name)
                
                # Update parameters
                for key, value in role_config.items():
                    if key != "role_name" and hasattr(role, key):
                        setattr(role, key, value)
                
                role.save(ignore_permissions=True)
                print(f"↻ Updated role: {role_name}")
                
        except Exception as e:
            print(f"❌ Error with role {role_name}: {str(e)}")
    
    frappe.db.commit()
    return created_roles

def get_all_role_parameters():
    """Get all available parameters for Role doctype"""
    
    # Get meta information
    meta = frappe.get_meta("Role")
    parameters = {}
    
    print("All available Role parameters:\n")
    
    for field in meta.fields:
        if field.fieldtype not in ["Section Break", "Column Break", "Tab Break"]:
            parameters[field.fieldname] = {
                "fieldname": field.fieldname,
                "label": field.label,
                "fieldtype": field.fieldtype,
                "default": field.default,
                "reqd": field.reqd,
                "description": field.description or "",
                "options": field.options or ""
            }
            
            print(f"- {field.fieldname} ({field.label})")
            print(f"  Type: {field.fieldtype}")
            if field.default:
                print(f"  Default: {field.default}")
            if field.description:
                print(f"  Description: {field.description}")
            print()
    
    return parameters

def export_roles_to_json(filename="roles_config.json"):
    """Export roles configuration to JSON file"""
    import json
    
    roles = get_roles_with_parameters()
    
    with open(filename, 'w') as f:
        json.dump(roles, f, indent=2)
    
    print(f"Exported roles to {filename}")

def print_roles_table():
    """Print roles in a formatted table"""
    
    roles = get_roles_with_parameters()
    
    print("\nRoles Configuration Table\n")
    print(f"{'Role Name':<25} {'Desk Access':<12} {'2FA':<5} {'Custom':<8} {'Home Page':<30}")
    print("-" * 80)
    
    for role in roles:
        print(f"{role['role_name']:<25} "
              f"{'Yes' if role['desk_access'] else 'No':<12} "
              f"{'Yes' if role['two_factor_auth'] else 'No':<5} "
              f"{'Yes' if role['is_custom'] else 'No':<8} "
              f"{role['home_page']:<30}")

def get_role_permissions_template():
    """Get a template for role permissions"""
    
    return {
        # Document permissions
        "read": 1,
        "write": 1,
        "create": 1,
        "delete": 1,
        "submit": 1,
        "cancel": 1,
        "amend": 1,
        "print": 1,
        "email": 1,
        "report": 1,
        "import": 0,
        "export": 1,
        "share": 1,
        
        # Field-level permissions
        "set_user_permissions": 0,
        "apply_user_permissions": 1,
        
        # Additional permissions
        "if_owner": 0,
        "select": 1
    }

def create_role_with_full_config(role_name, config):
    """Create a role with complete configuration including permissions"""
    
    # Create the role first
    if not frappe.db.exists("Role", role_name):
        role = frappe.get_doc({
            "doctype": "Role",
            "role_name": role_name,
            **config  # Unpack all config parameters
        })
        role.insert(ignore_permissions=True)
        print(f"✓ Created role: {role_name}")
        
        # Now set permissions for various doctypes if needed
        # This would be done separately using DocPerm
        
        return role
    else:
        print(f"→ Role already exists: {role_name}")
        return frappe.get_doc("Role", role_name)

# Example usage functions

def get_role_by_name(role_name):
    """Get a specific role configuration"""
    roles = get_roles_with_parameters()
    return next((role for role in roles if role["role_name"] == role_name), None)

def get_roles_with_2fa():
    """Get all roles that require two-factor authentication"""
    roles = get_roles_with_parameters()
    return [role for role in roles if role["two_factor_auth"]]

def get_roles_by_domain(domain):
    """Get all roles restricted to a specific domain"""
    roles = get_roles_with_parameters()
    return [role for role in roles if role["restrict_to_domain"] == domain]

# Main execution example
if __name__ == "__main__":
    # Get all roles
    roles = get_roles_with_parameters()
    print(f"Total roles configured: {len(roles)}")
    
    # Print roles table
    print_roles_table()
    
    # Get all available parameters
    # params = get_all_role_parameters()
    
    # Create roles in the system
    # created = create_roles_with_parameters()
    # print(f"\nCreated {len(created)} roles")