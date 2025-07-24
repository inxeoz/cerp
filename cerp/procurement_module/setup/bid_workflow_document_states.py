import frappe

def get_workflow_states_table():
    """Returns workflow states configuration as a list of dictionaries"""
    
    workflow_states = [
        {
            "no": 1,
            "state": "Draft",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "draft",
            "only_allow_edit_for": "Procurement Officer"
        },
        {
            "no": 2,
            "state": "RQ Submitted For Approval",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for MD Appro...",
            "only_allow_edit_for": "Managing Director"
        },
        {
            "no": 3,
            "state": "RQ Approved",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending to creation of ...",
            "only_allow_edit_for": "Procurement Officer"
        },
        {
            "no": 4,
            "state": "BCCM Submitted For Approval",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for PD Approv...",
            "only_allow_edit_for": "Project Director"
        },
        {
            "no": 5,
            "state": "BCCM Verified By PD",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for CGM Appr...",
            "only_allow_edit_for": "Chief General Manager"
        },
        {
            "no": 6,
            "state": "BCCM Verified By CGM",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for MD Appro...",
            "only_allow_edit_for": "Managing Director"
        },
        {
            "no": 7,
            "state": "BCCM Verified By MD",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending to upload bcc...",
            "only_allow_edit_for": "Procurement Officer"
        },
        {
            "no": 8,
            "state": "UBO Submitted For Approval",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for CGM appr...",
            "only_allow_edit_for": "Chief General Manager"
        },
        {
            "no": 9,
            "state": "UBO Verified By CGM",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for MD appro...",
            "only_allow_edit_for": "Managing Director"
        },
        {
            "no": 10,
            "state": "UBO Verified By MD",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending to publish bid",
            "only_allow_edit_for": "Marketing Team"
        },
        {
            "no": 11,
            "state": "Bid Published",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "waiting for Vendors qu...",
            "only_allow_edit_for": "System Manager"
        },
        {
            "no": 12,
            "state": "No Vendors Query",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending to upload TE...",
            "only_allow_edit_for": "Procurement Officer"
        },
        {
            "no": 13,
            "state": "TEC MOM Uploaded",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for CGM appr...",
            "only_allow_edit_for": "Chief General Manager"
        },
        {
            "no": 14,
            "state": "TEC MOM Verified By CGM",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for MD appro...",
            "only_allow_edit_for": "Managing Director"
        },
        {
            "no": 15,
            "state": "TEC MOM Verified By MD",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending to upload FE...",
            "only_allow_edit_for": "Procurement Officer"
        },
        {
            "no": 16,
            "state": "FEC MOM Uploaded",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for CGM appr...",
            "only_allow_edit_for": "Chief General Manager"
        },
        {
            "no": 17,
            "state": "FEC MOM Verified By CGM",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for MD appro...",
            "only_allow_edit_for": "Managing Director"
        },
        {
            "no": 18,
            "state": "FEC MOM Verified By MD",
            "doc_status": 0,
            "update_field": "bid_document_status",
            "update_value": "Approved",
            "only_allow_edit_for": "System Manager"
        },
        {
            "no": 19,
            "state": "Rejected",
            "doc_status": 0,
            "update_field": "",
            "update_value": "",
            "only_allow_edit_for": "Procurement Officer"
        }
    ]
    
    return workflow_states

# def print_workflow_states_table():
#     """Print workflow states as a formatted table"""
    
#     states = get_workflow_states_table()
    
#     # Print header
#     print("\nAll possible Workflow States and roles of the workflow. Docstatus Options: 0 is 'Saved', 1 is 'Submitted' and 2 is 'Cancelled'\n")
#     print(f"{'No.':<5} {'State':<35} {'Doc Status':<12} {'Update Field':<25} {'Update Value':<25} {'Only Allow Edit For':<25}")
#     print("-" * 130)
    
#     # Print rows
#     for state in states:
#         print(f"{state['no']:<5} {state['state']:<35} {state['doc_status']:<12} {state['update_field']:<25} {state['update_value']:<25} {state['only_allow_edit_for']:<25}")

# def get_workflow_states_for_doctype(doctype="Bid Document"):
#     """Get workflow states formatted for use in workflow creation"""
    
#     states = get_workflow_states_table()
#     workflow_states = []
    
#     for state in states:
#         workflow_state = {
#             "state": state["state"],
#             "doc_status": str(state["doc_status"]),
#             "allow_edit": state["only_allow_edit_for"],
#             "is_optional_state": 0
#         }
        
#         # Add update field info if present
#         if state["update_field"]:
#             workflow_state["update_field"] = state["update_field"]
#             workflow_state["update_value"] = state["update_value"]
            
#         workflow_states.append(workflow_state)
    
#     return workflow_states

# def create_workflow_states_from_table():
#     """Create actual workflow states in the system from the table data"""
    
#     states = get_workflow_states_table()
#     created_states = []
    
#     print("Creating workflow states...")
    
#     for state in states:
#         state_name = state["state"]
        
#         if not frappe.db.exists("Workflow State", state_name):
#             # Determine style based on state name
#             if "Rejected" in state_name:
#                 style = "Danger"
#             elif "Approved" in state_name or "Verified" in state_name:
#                 style = "Success"
#             elif "Submitted" in state_name or "Uploaded" in state_name:
#                 style = "Warning"
#             elif "Draft" in state_name:
#                 style = "Primary"
#             else:
#                 style = "Info"
            
#             workflow_state = frappe.get_doc({
#                 "doctype": "Workflow State",
#                 "workflow_state_name": state_name,
#                 "style": style
#             })
#             workflow_state.insert(ignore_permissions=True)
#             created_states.append(state_name)
#             print(f"✓ Created state: {state_name}")
#         else:
#             print(f"→ State already exists: {state_name}")
    
#     return created_states

# def create_roles_from_table():
#     """Create roles mentioned in the workflow states table"""
    
#     states = get_workflow_states_table()
#     roles = set()
    
#     # Extract unique roles
#     for state in states:
#         if state["only_allow_edit_for"]:
#             roles.add(state["only_allow_edit_for"])
    
#     # Create roles
#     created_roles = []
#     print("\nCreating roles...")
    
#     for role in roles:
#         if not frappe.db.exists("Role", role):
#             role_doc = frappe.get_doc({
#                 "doctype": "Role",
#                 "role_name": role,
#                 "desk_access": 1
#             })
#             role_doc.insert(ignore_permissions=True)
#             created_roles.append(role)
#             print(f"✓ Created role: {role}")
#         else:
#             print(f"→ Role already exists: {role}")
    
#     return created_roles

# # Example usage:
# if __name__ == "__main__":
#     # Get the data
#     states = get_workflow_states_table()
#     print(f"Total states: {len(states)}")
    
#     # Print as table
#     print_workflow_states_table()
    
#     # Create states and roles in the system
#     # create_workflow_states_from_table()
#     # create_roles_from_table()