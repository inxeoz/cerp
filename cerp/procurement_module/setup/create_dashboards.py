import frappe

def create_simple_workspace():
    """Create a public and visible workspace"""
    
    workspace_name = "Simple Workspace"
    
    # Check if exists
    if frappe.db.exists("Workspace", workspace_name):
        print(f"Workspace already exists: {workspace_name}")
        return
    
    # Create workspace with public visibility
    workspace = frappe.get_doc({
        "doctype": "Workspace",
        "name": workspace_name,
        "label": "Simple Workspace",
        "title": "Simple Workspace",
        "module": "Desk",
        "public": 1,  # Make it public
        "is_hidden": 0,  # Make sure it's not hidden
        "icon": "view",  # Add an icon to make it more visible
        "restrict_to_domain": "",  # No domain restrictions
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
    })
    
    workspace.insert(ignore_permissions=True)
    frappe.db.commit()
    
    # Clear cache to ensure immediate visibility
    frappe.clear_cache()
    
    print(f"Created Public Workspace: {workspace_name}")
    print("The workspace should now be visible in the sidebar for all users")

# Run it
# create_simple_workspace()