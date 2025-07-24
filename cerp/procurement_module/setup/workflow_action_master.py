import frappe

def get_workflow_action_masters():
    """Returns all workflow action master configurations"""
    
    workflow_actions = [
        {
            "id": "Send for Review",
            "workflow_action_name": "Send for Review",
            "icon": "send",
            "style": "Primary",
            "description": "Send document for review",
            "is_standard": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "Publish",
            "workflow_action_name": "Publish",
            "icon": "globe",
            "style": "Success",
            "description": "Publish the document",
            "is_standard": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "Submit for Approval",
            "workflow_action_name": "Submit for Approval",
            "icon": "check-circle",
            "style": "Warning",
            "description": "Submit document for approval",
            "is_standard": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "Dispose",
            "workflow_action_name": "Dispose",
            "icon": "trash",
            "style": "Danger",
            "description": "Dispose the document",
            "is_standard": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "Verify",
            "workflow_action_name": "Verify",
            "icon": "shield-check",
            "style": "Info",
            "description": "Verify the document",
            "is_standard": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "Review",
            "workflow_action_name": "Review",
            "icon": "eye",
            "style": "Info",
            "description": "Review the document",
            "is_standard": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "Reject",
            "workflow_action_name": "Reject",
            "icon": "x-circle",
            "style": "Danger",
            "description": "Reject the document",
            "is_standard": 0,
            "creation_date": "2024-01-01"
        },
        {
            "id": "Approve",
            "workflow_action_name": "Approve",
            "icon": "check",
            "style": "Success",
            "description": "Approve the document",
            "is_standard": 0,
            "creation_date": "2024-01-01"
        }
    ]
    
    return workflow_actions

def create_all_workflow_actions():
    """Create all workflow action masters in the system"""
    
    actions = get_workflow_action_masters()
    created_count = 0
    updated_count = 0
    
    print("Creating/Updating Workflow Action Masters...\n")
    
    for action_config in actions:
        action_name = action_config["workflow_action_name"]
        
        try:
            if not frappe.db.exists("Workflow Action Master", action_name):
                # Create new workflow action
                workflow_action = frappe.get_doc({
                    "doctype": "Workflow Action Master",
                    "workflow_action_name": action_name
                })
                workflow_action.insert(ignore_permissions=True)
                created_count += 1
                print(f"✓ Created: {action_name}")
            else:
                print(f"→ Already exists: {action_name}")
                updated_count += 1
                
        except Exception as e:
            print(f"❌ Error with action {action_name}: {str(e)}")
    
    frappe.db.commit()
    print(f"\n✅ Created: {created_count}, Existing: {updated_count}")
    
    return created_count, updated_count

def get_workflow_actions_by_type():
    """Get workflow actions grouped by their type/purpose"""
    
    actions = get_workflow_action_masters()
    
    action_types = {
        "submission": ["Send for Review", "Submit for Approval"],
        "approval": ["Approve", "Verify", "Review"],
        "rejection": ["Reject", "Dispose"],
        "publication": ["Publish"]
    }
    
    grouped_actions = {}
    for action_type, action_names in action_types.items():
        grouped_actions[action_type] = [
            action for action in actions 
            if action["workflow_action_name"] in action_names
        ]
    
    return grouped_actions

def print_workflow_actions_summary():
    """Print a summary of all workflow actions"""
    
    actions = get_workflow_action_masters()
    grouped = get_workflow_actions_by_type()
    
    print("\n📋 Workflow Actions Summary\n")
    print(f"Total Actions: {len(actions)}")
    
    print("\n🔤 All Actions:")
    for i, action in enumerate(actions, 1):
        print(f"  {i}. {action['workflow_action_name']:<25} [{action.get('style', 'Default')}]")
    
    print("\n📊 Actions by Type:")
    for action_type, type_actions in grouped.items():
        print(f"\n  {action_type.title()}:")
        for action in type_actions:
            print(f"    - {action['workflow_action_name']}")

def get_action_usage_in_workflows():
    """Get information about which workflows use which actions"""
    
    # This would query actual workflows to see action usage
    # For now, returning expected usage based on the workflow states
    
    action_usage = {
        "Send for Review": ["Bid Document Workflow"],
        "Submit for Approval": ["Bid Document Workflow", "RQ Workflow", "BCCM Workflow", "UBO Workflow"],
        "Approve": ["Bid Document Workflow", "General Approval Workflow"],
        "Verify": ["BCCM Workflow", "UBO Workflow", "TEC MOM Workflow", "FEC MOM Workflow"],
        "Review": ["Document Review Workflow"],
        "Reject": ["All Approval Workflows"],
        "Publish": ["Bid Publishing Workflow"],
        "Dispose": ["Document Disposal Workflow"]
    }
    
    return action_usage

def validate_workflow_actions():
    """Validate that all required workflow actions exist"""
    
    required_actions = [
        "Send for Review",
        "Submit for Approval", 
        "Approve",
        "Verify",
        "Review",
        "Reject",
        "Publish"
    ]
    
    missing_actions = []
    existing_actions = []
    
    print("\n🔍 Validating Workflow Actions...\n")
    
    for action in required_actions:
        if frappe.db.exists("Workflow Action Master", action):
            existing_actions.append(action)
            print(f"✓ Found: {action}")
        else:
            missing_actions.append(action)
            print(f"❌ Missing: {action}")
    
    if missing_actions:
        print(f"\n⚠️  Missing {len(missing_actions)} required actions")
        print("Run create_all_workflow_actions() to create them")
    else:
        print("\n✅ All required workflow actions exist!")
    
    return existing_actions, missing_actions

def export_workflow_actions_to_json(filename="workflow_actions.json"):
    """Export workflow actions to JSON file"""
    import json
    
    actions = get_workflow_action_masters()
    
    with open(filename, 'w') as f:
        json.dump(actions, f, indent=2)
    
    print(f"Exported {len(actions)} workflow actions to {filename}")

def create_custom_workflow_action(action_name, icon=None, style=None, description=None):
    """Create a custom workflow action"""
    
    if frappe.db.exists("Workflow Action Master", action_name):
        print(f"Workflow action '{action_name}' already exists")
        return frappe.get_doc("Workflow Action Master", action_name)
    
    try:
        workflow_action = frappe.get_doc({
            "doctype": "Workflow Action Master",
            "workflow_action_name": action_name
        })
        
        workflow_action.insert(ignore_permissions=True)
        frappe.db.commit()
        
        print(f"✓ Created custom workflow action: {action_name}")
        return workflow_action
        
    except Exception as e:
        print(f"❌ Error creating workflow action: {str(e)}")
        return None

def get_workflow_action_transitions():
    """Get typical transitions associated with each action"""
    
    action_transitions = {
        "Send for Review": {
            "typical_from_states": ["Draft"],
            "typical_to_states": ["Under Review", "RQ Submitted For Approval"]
        },
        "Submit for Approval": {
            "typical_from_states": ["Draft", "Reviewed", "Modified"],
            "typical_to_states": ["Pending Approval", "Submitted For Approval"]
        },
        "Approve": {
            "typical_from_states": ["Pending Approval", "Under Review"],
            "typical_to_states": ["Approved", "Next Approval Level"]
        },
        "Verify": {
            "typical_from_states": ["Submitted", "Under Verification"],
            "typical_to_states": ["Verified", "Next Verification Level"]
        },
        "Review": {
            "typical_from_states": ["Submitted", "Draft"],
            "typical_to_states": ["Under Review", "Reviewed"]
        },
        "Reject": {
            "typical_from_states": ["Any State except Final"],
            "typical_to_states": ["Rejected", "Draft"]
        },
        "Publish": {
            "typical_from_states": ["Approved", "Verified"],
            "typical_to_states": ["Published", "Live"]
        },
        "Dispose": {
            "typical_from_states": ["Rejected", "Obsolete"],
            "typical_to_states": ["Disposed", "Archived"]
        }
    }
    
    return action_transitions

# Utility function to check action availability
def is_action_available_for_state(action_name, current_state):
    """Check if an action is typically available for a given state"""
    
    transitions = get_workflow_action_transitions()
    
    if action_name not in transitions:
        return False
    
    typical_from_states = transitions[action_name]["typical_from_states"]
    
    # Special case for Reject which can be from any state
    if action_name == "Reject" and current_state not in ["Approved", "Published", "Disposed"]:
        return True
    
    return current_state in typical_from_states

# Example usage:
if __name__ == "__main__":
    # Get all actions
    actions = get_workflow_action_masters()
    print(f"Total workflow actions: {len(actions)}")
    
    # Print summary
    print_workflow_actions_summary()
    
    # Validate actions
    existing, missing = validate_workflow_actions()
    
    # Create all actions if needed
    # create_all_workflow_actions()
    
    # Check action availability
    print("\n🔍 Action Availability Check:")
    print(f"Can 'Approve' from 'Pending Approval': {is_action_available_for_state('Approve', 'Pending Approval')}")
    print(f"Can 'Reject' from 'Under Review': {is_action_available_for_state('Reject', 'Under Review')}")