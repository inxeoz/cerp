import frappe
from typing import List, Dict, Any

def prepare_bid_document_workflow_data() -> Dict[str, Any]:
    """
    Prepare comprehensive workflow data for Bid Document
    
    Returns:
        Dict containing all workflow components
    """
    # Prepare Roles
    roles = prepare_bid_document_roles()
    
    # Prepare Role Profiles
    role_profiles = prepare_bid_document_role_profiles(roles)
    
    # Prepare Workflow States
    workflow_states = prepare_bid_document_workflow_states()
    
    # Prepare Workflow Actions
    workflow_actions = prepare_bid_document_workflow_actions()
    
    # Prepare Workflow Transitions
    workflow_transitions = prepare_bid_document_workflow_transitions()
    
    # Prepare Workflow Configuration
    workflow = prepare_bid_document_workflow_configuration(
        workflow_states, 
        workflow_transitions
    )
    
    return {
        "Role": roles,
        "Role Profile": role_profiles,
        "Workflow State": workflow_states,
        "Workflow Action Master": workflow_actions,
        "Workflow Transition": workflow_transitions,
        "Workflow": [workflow]
    }

def prepare_bid_document_roles() -> List[Dict[str, Any]]:
    """
    Prepare roles for Bid Document Workflow
    
    Returns:
        List of role configurations
    """
    return [
        {"role_name": "Procurement Officer"},
        {"role_name": "Managing Director"},
        {"role_name": "Project Director"},
        {"role_name": "Chief General Manager"},
        {"role_name": "Marketing Team"},
        {"role_name": "System Manager"}
    ]

def prepare_bid_document_role_profiles(roles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Prepare role profiles for Bid Document Workflow
    
    Args:
        roles (List[Dict]): List of role configurations
    
    Returns:
        List of role profile configurations
    """
    return [
        {
            "role_profile_name": "Procurement Workflow Profile",
            "roles": [
                {"role": "Procurement Officer"}
            ],
            "description": "Profile for Procurement Officers"
        },
        {
            "role_profile_name": "Approval Workflow Profile",
            "roles": [
                {"role": "Managing Director"},
                {"role": "Project Director"},
                {"role": "Chief General Manager"}
            ],
            "description": "Profile for Approval Authorities"
        },
        {
            "role_profile_name": "Marketing Workflow Profile",
            "roles": [
                {"role": "Marketing Team"},
                {"role": "System Manager"}
            ],
            "description": "Profile for Marketing and System Management"
        }
    ]

def prepare_bid_document_workflow_states() -> List[Dict[str, Any]]:
    """
    Prepare workflow states for Bid Document
    
    Returns:
        List of workflow state configurations
    """
    # Use the existing get_merged_bid_workflow_states() function
    return get_merged_bid_workflow_states()

def prepare_bid_document_workflow_actions() -> List[Dict[str, Any]]:
    """
    Prepare workflow actions for Bid Document
    
    Returns:
        List of workflow action configurations
    """
    return [
        {"workflow_action_name": "Submit for Approval"},
        {"workflow_action_name": "Approve"},
        {"workflow_action_name": "Verify"},
        {"workflow_action_name": "Reject"},
        {"workflow_action_name": "Publish"}
    ]

def prepare_bid_document_workflow_transitions() -> List[Dict[str, Any]]:
    """
    Prepare workflow transitions for Bid Document
    
    Returns:
        List of workflow transition configurations
    """
    # Use the existing get_workflow_transitions_table() function
    return get_workflow_transitions_table()

def prepare_bid_document_workflow_configuration(
    workflow_states: List[Dict[str, Any]], 
    workflow_transitions: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Prepare workflow configuration for Bid Document
    
    Args:
        workflow_states (List[Dict]): Workflow states
        workflow_transitions (List[Dict]): Workflow transitions
    
    Returns:
        Dict containing workflow configuration
    """
    return {
        "workflow_name": "Bid Document Workflow",
        "document_type": "Bid Document",
        "is_active": 1,
        "send_email_alert": 1,
        "states": [
            {
                "state": state['workflow_state_name'],
                "doc_status": state['doc_status'],
                "allow_edit": state['only_allow_edit_for']
            } for state in workflow_states
        ],
        "transitions": [
            {
                "state": transition['state'],
                "action": transition['action'],
                "next_state": transition['next_state'],
                "allowed": transition['allowed']
            } for transition in workflow_transitions
        ]
    }

def create_bid_document_workflow():
    """
    Comprehensive method to create Bid Document Workflow
    
    Uses general methods to create all workflow components
    """
    try:
        # Prepare workflow data
        workflow_data = prepare_bid_document_workflow_data()
        
        # Create workflow components using general methods
        workflow_setup_result = create_workflow_components(workflow_data)
        
        return {
            "status": "success",
            "workflow_setup": workflow_setup_result
        }
    
    except Exception as e:
        frappe.log_error(f"Bid Document Workflow Setup Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }

# Expose as whitelisted method
@frappe.whitelist()
def setup_bid_document_workflow():
    """
    Publicly accessible method to trigger Bid Document Workflow setup
    """
    return create_bid_document_workflow()

# Example usage
def workflow_setup_example():
    """
    Example of setting up Bid Document Workflow
    """
    # Call the setup method
    result = setup_bid_document_workflow()
    
    # You can add additional logging or processing here
    if result['status'] == 'success':
        print("Bid Document Workflow setup completed successfully")
    else:
        print(f"Workflow setup failed: {result.get('message', 'Unknown error')}")
    
    return result