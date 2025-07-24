import frappe

def get_all_workflow_states():
    """Returns all workflow states configuration"""
    
    workflow_states = [
        {
            "id": "Draft",
            "state": "Draft",
            "workflow_state_name": "Draft",
            "style": "Primary",
            "icon": "file",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "RQ Submitted For Approval",
            "state": "RQ Submitted For Approval", 
            "workflow_state_name": "RQ Submitted For Approval",
            "style": "Warning",
            "icon": "send",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "RQ Approved",
            "state": "RQ Approved",
            "workflow_state_name": "RQ Approved",
            "style": "Success",
            "icon": "check",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "BCCM Submitted For Approval",
            "state": "BCCM Submitted For Approval",
            "workflow_state_name": "BCCM Submitted For Approval",
            "style": "Warning",
            "icon": "send",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "BCCM Verified By PD",
            "state": "BCCM Verified By PD",
            "workflow_state_name": "BCCM Verified By PD",
            "style": "Info",
            "icon": "user-check",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "BCCM Verified By CGM",
            "state": "BCCM Verified By CGM",
            "workflow_state_name": "BCCM Verified By CGM",
            "style": "Info",
            "icon": "user-check",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "BCCM Verified By MD",
            "state": "BCCM Verified By MD",
            "workflow_state_name": "BCCM Verified By MD",
            "style": "Success",
            "icon": "crown",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "UBO Submitted For Approval",
            "state": "UBO Submitted For Approval",
            "workflow_state_name": "UBO Submitted For Approval",
            "style": "Warning",
            "icon": "send",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "UBO Verified By CGM",
            "state": "UBO Verified By CGM",
            "workflow_state_name": "UBO Verified By CGM",
            "style": "Info",
            "icon": "user-check",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "UBO Verified By MD",
            "state": "UBO Verified By MD",
            "workflow_state_name": "UBO Verified By MD",
            "style": "Success",
            "icon": "crown",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "Bid Published",
            "state": "Bid Published",
            "workflow_state_name": "Bid Published",
            "style": "Success",
            "icon": "globe",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "No Vendors Query",
            "state": "No Vendors Query",
            "workflow_state_name": "No Vendors Query",
            "style": "Info",
            "icon": "question-circle",
            "doc_status": 0,
            "is_optional_state": 1,
            "creation_date": "2024-01-01"
        },
        {
            "id": "TEC MOM Uploaded",
            "state": "TEC MOM Uploaded",
            "workflow_state_name": "TEC MOM Uploaded",
            "style": "Warning",
            "icon": "upload",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "TEC MOM Verified By CGM",
            "state": "TEC MOM Verified By CGM",
            "workflow_state_name": "TEC MOM Verified By CGM",
            "style": "Info",
            "icon": "user-check",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "TEC MOM Verified By MD",
            "state": "TEC MOM Verified By MD",
            "workflow_state_name": "TEC MOM Verified By MD",
            "style": "Success",
            "icon": "crown",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "FEC MOM Uploaded",
            "state": "FEC MOM Uploaded",
            "workflow_state_name": "FEC MOM Uploaded",
            "style": "Warning",
            "icon": "upload",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "FEC MOM Verified By CGM",
            "state": "FEC MOM Verified By CGM",
            "workflow_state_name": "FEC MOM Verified By CGM",
            "style": "Info",
            "icon": "user-check",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "FEC MOM Verified By MD",
            "state": "FEC MOM Verified By MD",
            "workflow_state_name": "FEC MOM Verified By MD",
            "style": "Success",
            "icon": "crown",
            "doc_status": 1,  # This might be final approved state
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "Rejected",
            "state": "Rejected",
            "workflow_state_name": "Rejected",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 2,  # Cancelled
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "Review",
            "state": "Review",
            "workflow_state_name": "Review",
            "style": "Info",
            "icon": "eye",
            "doc_status": 0,
            "is_optional_state": 0,
            "creation_date": "2024-01-01"
        }
    ]
    
    return workflow_states

def create_all_workflow_states():
    """Create all workflow states in the system"""
    
    states = get_all_workflow_states()
    created_count = 0
    updated_count = 0
    
    print("Creating/Updating Workflow States...\n")
    
    for state_config in states:
        state_name = state_config["workflow_state_name"]
        
        try:
            if not frappe.db.exists("Workflow State", state_name):
                # Create new workflow state
                workflow_state = frappe.get_doc({
                    "doctype": "Workflow State",
                    "workflow_state_name": state_name,
                    "style": state_config.get("style", "Primary"),
                    "icon": state_config.get("icon", "")
                })
                workflow_state.insert(ignore_permissions=True)
                created_count += 1
                print(f"✓ Created: {state_name}")
            else:
                # Update existing workflow state
                workflow_state = frappe.get_doc("Workflow State", state_name)
                workflow_state.style = state_config.get("style", "Primary")
                if state_config.get("icon"):
                    workflow_state.icon = state_config["icon"]
                workflow_state.save(ignore_permissions=True)
                updated_count += 1
                print(f"↻ Updated: {state_name}")
                
        except Exception as e:
            print(f"❌ Error with state {state_name}: {str(e)}")
    
    frappe.db.commit()
    print(f"\n✅ Created: {created_count}, Updated: {updated_count}")
    
    return created_count, updated_count

def get_workflow_states_by_style(style):
    """Get workflow states filtered by style"""
    
    states = get_all_workflow_states()
    return [s for s in states if s["style"] == style]

def get_workflow_states_by_doc_status(doc_status):
    """Get workflow states filtered by document status"""
    
    states = get_all_workflow_states()
    return [s for s in states if s["doc_status"] == doc_status]

def print_workflow_states_summary():
    """Print a summary of all workflow states"""
    
    states = get_all_workflow_states()
    
    # Count by style
    style_counts = {}
    for state in states:
        style = state["style"]
        style_counts[style] = style_counts.get(style, 0) + 1
    
    # Count by doc_status
    status_counts = {0: 0, 1: 0, 2: 0}
    for state in states:
        status = state["doc_status"]
        status_counts[status] = status_counts.get(status, 0) + 1
    
    print("\n📊 Workflow States Summary\n")
    print(f"Total States: {len(states)}")
    
    print("\n🎨 States by Style:")
    for style, count in style_counts.items():
        print(f"  {style}: {count}")
    
    print("\n📄 States by Document Status:")
    print(f"  Draft (0): {status_counts[0]}")
    print(f"  Submitted (1): {status_counts[1]}")
    print(f"  Cancelled (2): {status_counts[2]}")
    
    print("\n📋 All States:")
    for i, state in enumerate(states, 1):
        print(f"  {i:2d}. {state['state']:<35} [{state['style']}]")

def get_workflow_state_transitions_map():
    """Get a map of which states typically transition to which states"""
    
    transitions_map = {
        "Draft": ["RQ Submitted For Approval"],
        "RQ Submitted For Approval": ["RQ Approved", "Rejected"],
        "RQ Approved": ["BCCM Submitted For Approval"],
        "BCCM Submitted For Approval": ["BCCM Verified By PD", "Rejected"],
        "BCCM Verified By PD": ["BCCM Verified By CGM", "Rejected"],
        "BCCM Verified By CGM": ["BCCM Verified By MD", "Rejected"],
        "BCCM Verified By MD": ["UBO Submitted For Approval"],
        "UBO Submitted For Approval": ["UBO Verified By CGM", "Rejected"],
        "UBO Verified By CGM": ["UBO Verified By MD", "Rejected"],
        "UBO Verified By MD": ["Bid Published"],
        "Bid Published": ["No Vendors Query"],
        "No Vendors Query": ["TEC MOM Uploaded"],
        "TEC MOM Uploaded": ["TEC MOM Verified By CGM", "Rejected"],
        "TEC MOM Verified By CGM": ["TEC MOM Verified By MD", "Rejected"],
        "TEC MOM Verified By MD": ["FEC MOM Uploaded"],
        "FEC MOM Uploaded": ["FEC MOM Verified By CGM", "Rejected"],
        "FEC MOM Verified By CGM": ["FEC MOM Verified By MD", "Rejected"],
        "FEC MOM Verified By MD": [],  # Final state
        "Rejected": ["Draft"]  # Can go back to draft
    }
    
    return transitions_map

def validate_workflow_state_flow():
    """Validate that the workflow state flow is complete"""
    
    states = get_all_workflow_states()
    transitions_map = get_workflow_state_transitions_map()
    
    state_names = [s["state"] for s in states]
    issues = []
    
    # Check if all states are in the map
    for state in state_names:
        if state not in transitions_map and state != "Review":
            issues.append(f"State '{state}' not found in transitions map")
    
    # Check if all referenced states exist
    for from_state, to_states in transitions_map.items():
        if from_state not in state_names:
            issues.append(f"From state '{from_state}' not found in states list")
        for to_state in to_states:
            if to_state not in state_names:
                issues.append(f"To state '{to_state}' not found in states list")
    
    if issues:
        print("❌ Validation Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✅ Workflow state flow validation passed!")
    
    return len(issues) == 0

# Example usage:
if __name__ == "__main__":
    # Get all states
    states = get_all_workflow_states()
    print(f"Total workflow states: {len(states)}")
    
    # Print summary
    print_workflow_states