# File: test.py
import frappe
import json

def create_system_workspace_complete():
    """Create a complete system workspace with all fields"""
    
    # First create custom block
    create_system_info_block()
    
    workspace_name = "system-demo"
    
    # Delete if exists
    if frappe.db.exists("Workspace", workspace_name):
        frappe.delete_doc("Workspace", workspace_name, force=True)
        frappe.db.commit()
    
    # Create workspace
    ws = frappe.new_doc("Workspace")
    
    # Required fields
    ws.name = workspace_name
    ws.label = "System Demo"
    ws.title = "System Demo"  # Required field
    ws.module = "Desk"
    
    # Optional fields
    ws.public = 1
    ws.is_hidden = 0
    ws.icon = "solid-success"
    ws.restrict_to_domain = ""
    
    # Content
    content = [
        {
            "type": "header",
            "value": "System Information Dashboard"
        },
        {
            "type": "paragraph",
            "value": """<div style='padding: 15px; background: #e3f2fd; border-radius: 8px;'>
                <p><strong>Welcome:</strong> {{ frappe.session.user_fullname }}</p>
                <p><strong>Email:</strong> {{ frappe.session.user }}</p>
                <p><strong>Site:</strong> {{ frappe.local.site }}</p>
            </div>"""
        },
        {
            "type": "spacer"
        },
        {
            "type": "header",
            "value": "Quick Links"
        },
        {
            "type": "shortcut",
            "label": "User List",
            "link_to": "User",
            "link_type": "DocType",
            "doc_view": "List"
        },
        {
            "type": "shortcut",
            "label": "Add User",
            "link_to": "User",
            "link_type": "DocType",
            "doc_view": "New"
        },
        {
            "type": "shortcut",
            "label": "System Settings",
            "link_to": "System Settings",
            "link_type": "DocType"
        },
        {
            "type": "shortcut",
            "label": "Error Log",
            "link_to": "Error Log",
            "link_type": "DocType",
            "doc_view": "List"
        },
        {
            "type": "spacer"
        },
        {
            "type": "custom_block",
            "value": "system_info_block"
        }
    ]
    
    ws.content = json.dumps(content)
    
    # Save
    ws.save(ignore_permissions=True)
    frappe.db.commit()
    
    print(f"✅ Workspace '{workspace_name}' created successfully!")
    print(f"📍 Access it at: /app/{workspace_name}")
    
    return ws

def create_system_info_block():
    """Create custom HTML block for system info"""
    block_name = "system_info_block"
    
    if frappe.db.exists("Custom HTML Block", block_name):
        print(f"Custom block '{block_name}' already exists")
        return
    
    doc = frappe.new_doc("Custom HTML Block")
    doc.name = block_name
    doc.html = """
    <div class="system-stats" style="padding: 20px; background: #f5f5f5; border-radius: 8px;">
        <h4 style="margin-bottom: 15px;">Live System Stats</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px;">
            <div style="text-align: center; padding: 15px; background: white; border-radius: 4px;">
                <div style="font-size: 2em; color: #1976d2;" id="user-count">0</div>
                <div style="color: #666;">Active Users</div>
            </div>
            <div style="text-align: center; padding: 15px; background: white; border-radius: 4px;">
                <div style="font-size: 2em; color: #388e3c;" id="doctype-count">0</div>
                <div style="color: #666;">DocTypes</div>
            </div>
            <div style="text-align: center; padding: 15px; background: white; border-radius: 4px;">
                <div style="font-size: 1.5em; color: #f57c00;" id="current-time">--:--</div>
                <div style="color: #666;">Server Time</div>
            </div>
        </div>
    </div>
    """
    
    doc.script = """
    frappe.ready(() => {
        // Get active users
        frappe.db.count('User', {enabled: 1}).then(count => {
            root_element.querySelector('#user-count').textContent = count;
        });
        
        // Get doctype count
        frappe.db.count('DocType', {istable: 0, issingle: 0}).then(count => {
            root_element.querySelector('#doctype-count').textContent = count;
        });
        
        // Update time
        function updateTime() {
            const now = new Date();
            root_element.querySelector('#current-time').textContent = now.toLocaleTimeString();
        }
        updateTime();
        setInterval(updateTime, 1000);
    });
    """
    
    doc.style = """
    .system-stats {
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    """
    
    doc.private = 0
    doc.save(ignore_permissions=True)
    frappe.db.commit()
    print(f"✅ Custom block '{block_name}' created")

def list_all_workspaces():
    """List all workspaces for debugging"""
    workspaces = frappe.get_all("Workspace", 
        fields=["name", "label", "title", "module", "public", "is_hidden"],
        order_by="name"
    )
    
    print("\n📋 All Workspaces:")
    print("-" * 70)
    print(f"{'Name':<25} {'Label':<20} {'Module':<10} {'Public':<8} {'Hidden':<8}")
    print("-" * 70)
    
    for ws in workspaces:
        public = "Yes" if ws.public else "No"
        hidden = "Yes" if ws.is_hidden else "No"
        print(f"{ws.name:<25} {ws.label:<20} {ws.module:<10} {public:<8} {hidden:<8}")
    
    return workspaces