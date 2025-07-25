import frappe

def create_role_profile():
    try:
        # Define the role profile name
        role_profile_name = "My Custom Role Profile"
        
        # Check if the role profile already exists
        if frappe.db.exists("Role Profile", role_profile_name):
            print(f"Role Profile '{role_profile_name}' already exists!")
            return
        
        # Create a new role profile document
        role_profile = frappe.new_doc("Role Profile")
        
        # Set the role profile name (this is the primary field)
        role_profile.role_profile = role_profile_name
        
        # Add roles to the role profile
        # The 'roles' field is a Table type that contains role assignments
        roles_to_add = [
            "System Manager",
            "Sales User",
            "Purchase User",
            "Stock User"
        ]
        
        for role_name in roles_to_add:
            # Check if the role exists before adding
            if frappe.db.exists("Role", role_name):
                role_profile.append("roles", {
                    "role": role_name
                })
                print(f"Added role: {role_name}")
            else:
                print(f"Role '{role_name}' does not exist, skipping...")
        
        # Insert the document
        role_profile.insert(ignore_permissions=True)
        
        # Commit the changes
        frappe.db.commit()
        
        print(f"\nRole Profile '{role_profile_name}' created successfully!")
        
    except Exception as e:
        frappe.log_error(f"Error creating role profile: {str(e)}")
        print(f"Error: {str(e)}")

# # To run the script
# if __name__ == "__main__":
#     # Make sure Frappe is initialized
#     # If running from bench console, this is already done
#     create_role_profile()