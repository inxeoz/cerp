import frappe

def create_simple_workflow():
    if frappe.db.exists("Workflow", "Simple Bid Workflow"):
        return

    # Create Workflow States
    for state in ["Draft", "Review", "Approved"]:
        if not frappe.db.exists("Workflow State", state):
            frappe.get_doc({
                "doctype": "Workflow State",
                "workflow_state_name": state,
                "style": "Primary" if state == "Draft" else ("Success" if state == "Approved" else "Info")
            }).insert(ignore_permissions=True)
            print(f"Created Workflow State: {state}")

    # Create Workflow Actions
    actions = ["Send for Review", "Approve", "Reject"]
    for action in actions:
        if not frappe.db.exists("Workflow Action Master", action):
            frappe.get_doc({
                "doctype": "Workflow Action Master",
                "workflow_action_name": action
            }).insert(ignore_permissions=True)
            print(f"Created Workflow Action: {action}")

    # Create the Workflow
    if not frappe.db.exists("Workflow", "Simple Bid Workflow"):
        workflow = frappe.get_doc({
            "doctype": "Workflow",
            "workflow_name": "Simple Bid Workflow",
            "document_type": "Bid Document",
            "is_active": 1,
            "workflow_state_field": "workflow_state",
            "states": [
                {
                    "state": "Draft",
                    "doc_status": "0",
                    "allow_edit": "All"
                },
                {
                    "state": "Review", 
                    "doc_status": "0",
                    "allow_edit": "All"
                },
                {
                    "state": "Approved",
                    "doc_status": "1",
                    "allow_edit": "All"
                }
            ],
            "transitions": [
                {
                    "state": "Draft",
                    "action": "Send for Review",
                    "next_state": "Review",
                    "allowed": "All"
                },
                {
                    "state": "Review",
                    "action": "Approve",
                    "next_state": "Approved", 
                    "allowed": "All"
                },
                {
                    "state": "Review",
                    "action": "Reject",
                    "next_state": "Draft",
                    "allowed": "All"
                }
            ]
        })
        workflow.insert(ignore_permissions=True)
        print("Workflow created: Simple Bid Workflow")
        
        # Update the name to match workflow_name for UI visibility
        frappe.db.set_value("Workflow", workflow.name, "name", "Simple Bid Workflow")
        frappe.db.commit()
        print("Updated workflow name for UI visibility")
        
        # Clear cache to ensure it appears in the UI
        frappe.clear_cache()
        frappe.cache().delete_value("workflow_" + "Bid Document")
        frappe.clear_document_cache("Workflow", "Simple Bid Workflow")
        print("Cache cleared")




############## TO CREATE WORKFLOW USING THIS SCRIPT ####################
# bench --site yoursite console
# In [1]: from cerp.procurement_module.setup.create_workflows import
#    ...: create_simple_workflow
#
# In [2]: create_simple_workflow()
# Workflow created: Simple Bid Workflow
# Updated workflow name for UI visibility
# Cache cleared
#
# In [3]: