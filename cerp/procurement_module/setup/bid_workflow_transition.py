import frappe

def get_workflow_transitions_table():
    """Returns workflow transitions configuration as a list of dictionaries"""
    
    workflow_transitions = [
        {
            "no": 1,
            "state": "Draft",
            "action": "Submit for Approval",
            "next_state": "RQ Submitted For Approval",
            "allowed": "Procurement Officer"
        },
        {
            "no": 2,
            "state": "RQ Submitted For Approval",
            "action": "Approve",
            "next_state": "RQ Approved",
            "allowed": "Managing Director"
        },
        {
            "no": 3,
            "state": "RQ Approved",
            "action": "Submit for Approval",
            "next_state": "BCCM Submitted For Approval",
            "allowed": "Procurement Officer"
        },
        {
            "no": 4,
            "state": "BCCM Submitted For Approval",
            "action": "Verify",
            "next_state": "BCCM Verified By PD",
            "allowed": "Project Director"
        },
        {
            "no": 5,
            "state": "BCCM Verified By PD",
            "action": "Verify",
            "next_state": "BCCM Verified By CGM",
            "allowed": "Chief General Manager"
        },
        {
            "no": 6,
            "state": "BCCM Verified By CGM",
            "action": "Verify",
            "next_state": "BCCM Verified By MD",
            "allowed": "Managing Director"
        },
        {
            "no": 7,
            "state": "BCCM Verified By MD",
            "action": "Submit for Approval",
            "next_state": "UBO Submitted For Approval",
            "allowed": "Procurement Officer"
        },
        {
            "no": 8,
            "state": "UBO Submitted For Approval",
            "action": "Verify",
            "next_state": "UBO Verified By CGM",
            "allowed": "Chief General Manager"
        },
        {
            "no": 9,
            "state": "UBO Verified By CGM",
            "action": "Verify",
            "next_state": "UBO Verified By MD",
            "allowed": "Managing Director"
        },
        {
            "no": 10,
            "state": "UBO Verified By MD",
            "action": "Publish",
            "next_state": "Bid Published",
            "allowed": "Marketing Team"
        },
        {
            "no": 11,
            "state": "No Vendors Query",
            "action": "Submit for Approval",
            "next_state": "TEC MOM Uploaded",
            "allowed": "Procurement Officer"
        },
        {
            "no": 12,
            "state": "TEC MOM Uploaded",
            "action": "Verify",
            "next_state": "TEC MOM Verified By CGM",
            "allowed": "Chief General Manager"
        },
        {
            "no": 13,
            "state": "TEC MOM Verified By CGM",
            "action": "Verify",
            "next_state": "TEC MOM Verified By MD",
            "allowed": "Managing Director"
        },
        {
            "no": 14,
            "state": "TEC MOM Verified By MD",
            "action": "Submit for Approval",
            "next_state": "FEC MOM Uploaded",
            "allowed": "Procurement Officer"
        },
        {
            "no": 15,
            "state": "FEC MOM Uploaded",
            "action": "Verify",
            "next_state": "FEC MOM Verified By CGM",
            "allowed": "Chief General Manager"
        },
        {
            "no": 16,
            "state": "FEC MOM Verified By CGM",
            "action": "Verify",
            "next_state": "FEC MOM Verified By MD",
            "allowed": "Managing Director"
        },
        # Reject transitions
        {
            "no": 17,
            "state": "RQ Submitted For Approval",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Managing Director"
        },
        {
            "no": 18,
            "state": "BCCM Submitted For Approval",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Project Director"
        },
        {
            "no": 19,
            "state": "BCCM Verified By PD",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Chief General Manager"
        },
        {
            "no": 20,
            "state": "BCCM Verified By CGM",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Managing Director"
        },
        {
            "no": 21,
            "state": "UBO Submitted For Approval",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Chief General Manager"
        },
        {
            "no": 22,
            "state": "UBO Verified By CGM",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Managing Director"
        },
        {
            "no": 23,
            "state": "TEC MOM Uploaded",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Chief General Manager"
        },
        {
            "no": 24,
            "state": "TEC MOM Verified By CGM",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Managing Director"
        },
        {
            "no": 25,
            "state": "FEC MOM Uploaded",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Chief General Manager"
        },
        {
            "no": 26,
            "state": "FEC MOM Verified By CGM",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Managing Director"
        }
    ]
    
    return workflow_transitions

# def print_workflow_transitions_table():
#     """Print workflow transitions as a formatted table"""
    
#     transitions = get_workflow_transitions_table()
    
#     # Print header
#     print("\nWorkflow Transitions Table\n")
#     print(f"{'No.':<5} {'State':<35} {'Action':<20} {'Next State':<35} {'Allowed':<25}")
#     print("-" * 120)
    
#     # Print rows
#     for trans in transitions:
#         print(f"{trans['no']:<5} {trans['state']:<35} {trans['action']:<20} {trans['next_state']:<35} {trans['allowed']:<25}")

# def get_workflow_transitions_for_creation():
#     """Get workflow transitions formatted for use in workflow creation"""
    
#     transitions = get_workflow_transitions_table()
#     workflow_transitions = []
    
#     for trans in transitions:
#         workflow_transition = {
#             "state": trans["state"],
#             "action": trans["action"],
#             "next_state": trans["next_state"],
#             "allowed": trans["allowed"],
#             "allow_self_approval": 1
#         }
#         workflow_transitions.append(workflow_transition)
    
#     return workflow_transitions

# def create_workflow_actions_from_transitions():
#     """Create workflow actions based on the transitions table"""
    
#     transitions = get_workflow_transitions_table()
#     actions = set()
    
#     # Extract unique actions
#     for trans in transitions:
#         actions.add(trans["action"])
    
#     # Create actions
#     created_actions = []
#     print("Creating workflow actions...")
    
#     for action in actions:
#         if not frappe.db.exists("Workflow Action Master", action):
#             action_doc = frappe.get_doc({
#                 "doctype": "Workflow Action Master",
#                 "workflow_action_name": action
#             })
#             action_doc.insert(ignore_permissions=True)
#             created_actions.append(action)
#             print(f"✓ Created action: {action}")
#         else:
#             print(f"→ Action already exists: {action}")
    
#     return created_actions

# def get_transition_graph():
#     """Generate a visual representation of the workflow transitions"""
    
#     transitions = get_workflow_transitions_table()
    
#     print("\nWorkflow Transition Graph:\n")
#     print("Draft")
#     print("  └─[Submit for Approval]→ RQ Submitted For Approval")
#     print("                            ├─[Approve]→ RQ Approved")
#     print("                            │            └─[Submit for Approval]→ BCCM Submitted For Approval")
#     print("                            │                                      ├─[Verify]→ BCCM Verified By PD")
#     print("                            │                                      │           └─[Verify]→ BCCM Verified By CGM")
#     print("                            │                                      │                       └─[Verify]→ BCCM Verified By MD")
#     print("                            │                                      │                                   └─[Submit for Approval]→ UBO Submitted For Approval")
#     print("                            │                                      │                                                             ├─[Verify]→ UBO Verified By CGM")
#     print("                            │                                      │                                                             │           └─[Verify]→ UBO Verified By MD")
#     print("                            │                                      │                                                             │                       └─[Publish]→ Bid Published")
#     print("                            │                                      │                                                             └─[Reject]→ Rejected")
#     print("                            │                                      └─[Reject]→ Rejected")
#     print("                            └─[Reject]→ Rejected")
#     print("\n... (Additional transitions for TEC MOM and FEC MOM flows)")

# def get_transitions_by_state(state_name):
#     """Get all transitions from a specific state"""
    
#     transitions = get_workflow_transitions_table()
#     state_transitions = [t for t in transitions if t["state"] == state_name]
    
#     return state_transitions

# def get_transitions_by_role(role_name):
#     """Get all transitions allowed for a specific role"""
    
#     transitions = get_workflow_transitions_table()
#     role_transitions = [t for t in transitions if t["allowed"] == role_name]
    
#     return role_transitions

# def export_transitions_to_csv(filename="workflow_transitions.csv"):
#     """Export workflow transitions to CSV file"""
#     import csv
    
#     transitions = get_workflow_transitions_table()
    
#     with open(filename, 'w', newline='') as csvfile:
#         fieldnames = ['no', 'state', 'action', 'next_state', 'allowed']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
#         writer.writeheader()
#         writer.writerows(transitions)
    
#     print(f"Exported transitions to {filename}")

# # Example usage:
# if __name__ == "__main__":
#     # Get all transitions
#     transitions = get_workflow_transitions_table()
#     print(f"Total transitions: {len(transitions)}")
    
#     # Print as table
#     print_workflow_transitions_table()
    
#     # Get transitions for a specific state
#     draft_transitions = get_transitions_by_state("Draft")
#     print(f"\nTransitions from Draft: {draft_transitions}")
    
#     # Get transitions for a specific role
#     po_transitions = get_transitions_by_role("Procurement Officer")
#     print(f"\nTransitions for Procurement Officer: {len(po_transitions)}")