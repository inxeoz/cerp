import frappe

def get_role_profiles():
    """Returns all role profile configurations"""
    
    role_profiles = [
        {
            "role_profile_name": "Marketing Team",
            "roles": [
                {"role": "Marketing Team"},
                {"role": "Employee"},
                {"role": "System User"}
            ],
            "description": "Role profile for marketing team members",
            "home_page": "/app/bid-document",
            "restrict_to_domain": "Marketing",
            "apply_to_all": 0,
            "creation_date": "2024-01-01"
        },
        {
            "role_profile_name": "Managing Director",
            "roles": [
                {"role": "Managing Director"},
                {"role": "Employee"},
                {"role": "System User"},
                {"role": "Approver"},
                {"role": "Report Manager"}
            ],
            "description": "Role profile for Managing Director with full approval rights",
            "home_page": "/app/dashboard/executive-dashboard",
            "restrict_to_domain": "",
            "apply_to_all": 0,
            "creation_date": "2024-01-01"
        },
        {
            "role_profile_name": "Chief General Manager",
            "roles": [
                {"role": "Chief General Manager"},
                {"role": "Employee"},
                {"role": "System User"},
                {"role": "Approver"},
                {"role": "Report Manager"},
                {"role": "Accounts Manager"}
            ],
            "description": "Role profile for Chief General Manager",
            "home_page": "/app/dashboard/operations-dashboard",
            "restrict_to_domain": "",
            "apply_to_all": 0,
            "creation_date": "2024-01-01"
        },
        {
            "role_profile_name": "Project Director",
            "roles": [
                {"role": "Project Director"},
                {"role": "Employee"},
                {"role": "System User"},
                {"role": "Projects User"},
                {"role": "Approver"}
            ],
            "description": "Role profile for Project Director",
            "home_page": "/app/project",
            "restrict_to_domain": "",
            "apply_to_all": 0,
            "creation_date": "2024-01-01"
        },
        {
            "role_profile_name": "Procurement Officer",
            "roles": [
                {"role": "Procurement Officer"},
                {"role": "Employee"},
                {"role": "System User"},
                {"role": "Purchase User"},
                {"role": "Stock User"}
            ],
            "description": "Role profile for Procurement Officer",
            "home_page": "/app/bid-document",
            "restrict_to_domain": "",
            "apply_to_all": 0,
            "creation_date": "2024-01-01"
        }
    ]
    
    return role_profiles

def create_all_role_profiles():
    """Create all role profiles in the system"""
    
    profiles = get_role_profiles()
    created_count = 0
    updated_count = 0
    
    print("Creating/Updating Role Profiles...\n")
    
    for profile_config in profiles:
        profile_name = profile_config["role_profile_name"]
        
        try:
            if not frappe.db.exists("Role Profile", profile_name):
                # Create new role profile
                role_profile = frappe.get_doc({
                    "doctype": "Role Profile",
                    "role_profile_name": profile_name,
                    "roles": profile_config["roles"]
                })
                role_profile.insert(ignore_permissions=True)
                created_count += 1
                print(f"✓ Created: {profile_name}")
            else:
                # Update existing role profile
                role_profile = frappe.get_doc("Role Profile", profile_name)
                role_profile.roles = []
                for role in profile_config["roles"]:
                    role_profile.append("roles", role)
                role_profile.save(ignore_permissions=True)
                updated_count += 1
                print(f"↻ Updated: {profile_name}")
                
        except Exception as e:
            print(f"❌ Error with profile {profile_name}: {str(e)}")
    
    frappe.db.commit()
    print(f"\n✅ Created: {created_count}, Updated: {updated_count}")
    
    return created_count, updated_count

def get_comprehensive_role_profiles():
    """Get role profiles with comprehensive permission sets"""
    
    comprehensive_profiles = [
        {
            "role_profile_name": "Bid Document Manager",
            "roles": [
                {"role": "Procurement Officer"},
                {"role": "Purchase User"},
                {"role": "Purchase Manager"},
                {"role": "Item Manager"},
                {"role": "Stock User"},
                {"role": "Employee"},
                {"role": "System User"}
            ],
            "description": "Complete access to bid document management",
            "modules_access": [
                "Buying",
                "Stock", 
                "Accounts",
                "Projects"
            ]
        },
        {
            "role_profile_name": "Executive Management",
            "roles": [
                {"role": "Managing Director"},
                {"role": "Chief General Manager"},
                {"role": "CEO"},
                {"role": "Accounts Manager"},
                {"role": "HR Manager"},
                {"role": "Sales Manager"},
                {"role": "Purchase Manager"},
                {"role": "Report Manager"},
                {"role": "Dashboard Manager"},
                {"role": "System User"}
            ],
            "description": "Executive level access with full approval rights",
            "modules_access": [
                "All Modules"
            ]
        },
        {
            "role_profile_name": "Vendor Portal User",
            "roles": [
                {"role": "Vendor"},
                {"role": "Website User"},
                {"role": "Customer"}
            ],
            "description": "Limited access for vendors to submit bids",
            "modules_access": [
                "Portal",
                "Website"
            ]
        },
        {
            "role_profile_name": "Finance Team",
            "roles": [
                {"role": "Accounts User"},
                {"role": "Accounts Manager"},
                {"role": "Auditor"},
                {"role": "Employee"},
                {"role": "System User"}
            ],
            "description": "Finance and accounting team access",
            "modules_access": [
                "Accounts",
                "Assets",
                "Buying",
                "Selling"
            ]
        },
        {
            "role_profile_name": "HR Team",
            "roles": [
                {"role": "HR User"},
                {"role": "HR Manager"},
                {"role": "Employee Self Service"},
                {"role": "Employee"},
                {"role": "System User"}
            ],
            "description": "Human resources team access",
            "modules_access": [
                "HR",
                "Payroll",
                "Employee"
            ]
        }
    ]
    
    return comprehensive_profiles

def print_role_profiles_summary():
    """Print a summary of all role profiles"""
    
    profiles = get_role_profiles()
    
    print("\n👥 Role Profiles Summary\n")
    print(f"Total Profiles: {len(profiles)}")
    
    print("\n📋 Profile Details:")
    for i, profile in enumerate(profiles, 1):
        print(f"\n{i}. {profile['role_profile_name']}")
        print(f"   Description: {profile.get('description', 'N/A')}")
        print(f"   Number of Roles: {len(profile['roles'])}")
        print(f"   Roles:")
        for role in profile['roles']:
            print(f"     - {role['role']}")

def get_role_profile_by_name(profile_name):
    """Get a specific role profile configuration"""
    
    profiles = get_role_profiles()
    for profile in profiles:
        if profile["role_profile_name"] == profile_name:
            return profile
    return None

def assign_role_profile_to_user(user_email, role_profile_name):
    """Assign a role profile to a user"""
    
    try:
        if not frappe.db.exists("User", user_email):
            print(f"❌ User {user_email} not found")
            return False
            
        if not frappe.db.exists("Role Profile", role_profile_name):
            print(f"❌ Role Profile {role_profile_name} not found")
            return False
        
        user = frappe.get_doc("User", user_email)
        
        # Check if already assigned
        existing_profiles = [d.role_profile for d in user.role_profiles]
        if role_profile_name not in existing_profiles:
            user.append("role_profiles", {
                "role_profile": role_profile_name
            })
            user.save(ignore_permissions=True)
            frappe.db.commit()
            print(f"✓ Assigned {role_profile_name} to {user_email}")
        else:
            print(f"→ {user_email} already has {role_profile_name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error assigning role profile: {str(e)}")
        return False

def create_custom_role_profile(profile_name, roles_list, description=""):
    """Create a custom role profile with specified roles"""
    
    if frappe.db.exists("Role Profile", profile_name):
        print(f"Role Profile '{profile_name}' already exists")
        return frappe.get_doc("Role Profile", profile_name)
    
    try:
        # Prepare roles
        roles = []
        for role_name in roles_list:
            if frappe.db.exists("Role", role_name):
                roles.append({"role": role_name})
            else:
                print(f"⚠️  Warning: Role '{role_name}' not found, skipping")
        
        if not roles:
            print("❌ No valid roles provided")
            return None
        
        # Create role profile
        role_profile = frappe.get_doc({
            "doctype": "Role Profile",
            "role_profile_name": profile_name,
            "roles": roles
        })
        
        role_profile.insert(ignore_permissions=True)
        frappe.db.commit()
        
        print(f"✓ Created custom role profile: {profile_name}")
        return role_profile
        
    except Exception as e:
        print(f"❌ Error creating role profile: {str(e)}")
        return None

def get_users_with_role_profile(role_profile_name):
    """Get all users who have a specific role profile"""
    
    users = frappe.db.sql("""
        SELECT 
            u.name as user_email,
            u.full_name,
            u.enabled
        FROM 
            `tabUser` u
        INNER JOIN 
            `tabHas Role Profile` hrp ON hrp.parent = u.name
        WHERE 
            hrp.role_profile = %s
            AND u.name