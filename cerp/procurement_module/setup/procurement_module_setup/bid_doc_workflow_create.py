

import frappe
from typing import List, Dict, Any

from cerp.procurement_module.setup.default_setup_methods.create_role import create_role
from cerp.procurement_module.setup.default_setup_methods.create_workflow_state import create_workflow_state
from cerp.procurement_module.setup.default_setup_methods.create_workflow_transition import create_workflow_transition
from cerp.procurement_module.setup.default_setup_methods.create_workflow import create_workflow
from cerp.procurement_module.setup.default_setup_methods.create_role_profile import create_role_profile
from cerp.procurement_module.setup.default_setup_methods.create_workflow_action_master import create_workflow_action_master

from cerp.procurement_module.setup.procurement_module_setup.get_bid_doc_workflow_states import get_merged_bid_workflow_states
from cerp.procurement_module.setup.procurement_module_setup.get_bid_workflow_transition import get_workflow_transitions_table

from cerp.procurement_module.setup.procurement_module_setup.bid_doc_role_profile_create import create_bid_document_role_profiles
from cerp.procurement_module.setup.default_setup_methods.validate_icon import validate_workflow_icon

from cerp.procurement_module.setup.procurement_module_setup.bid_doc_user_create import create_bid_user

def prepare_bid_document_workflow_data() -> Dict[str, Any]:
    """
    Prepare comprehensive workflow data for Bid Document
    
    Returns:
        Dict containing all workflow components
    """
    # Extract unique roles from workflow transitions
    workflow_transitions = get_workflow_transitions_table()
    roles = list(set(transition['allowed'] for transition in workflow_transitions))
    
    # Extract unique actions from workflow transitions
    actions = list(set(transition['action'] for transition in workflow_transitions))
    
    # Prepare workflow states
    workflow_states = get_merged_bid_workflow_states()
    
    return {
        "Role": [{"role_name": role} for role in roles],
        "Workflow Action Master": [{"workflow_action_name": action} for action in actions],
        "Workflow State": workflow_states,
        "Workflow Transition": workflow_transitions,
        "Workflow": [{
            "workflow_name": "Bid Document Workflow",
            "document_type": "Bid Document",
            "is_active": 1,
            "send_email_alert": 1,
            "states": [
                {
                    "state": state['workflow_state_name'],
                    "doc_status": state['doc_status'],
                    "allow_edit": state['only_allow_edit_for'],
                    "update_value" : state['update_value'],
                    "update_field" : state['update_field']
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
        }]
    }

def create_bid_document_workflow():
    """
    Comprehensive method to create Bid Document Workflow
    
    Uses general methods to create all workflow components
    """
    try:
        # Prepare workflow data
        workflow_data = prepare_bid_document_workflow_data()
        
        # Create roles
        roles_result = create_role(workflow_data['Role'])
        
        # Create workflow actions
        actions_result = create_workflow_action_master(workflow_data['Workflow Action Master'])
        
        # Create workflow states
        states_result = create_workflow_state(workflow_data['Workflow State'])
        
        # Create workflow transitions
        transitions_result = create_workflow_transition(workflow_data['Workflow Transition'])
        
        # Create workflow
        workflow_result = create_workflow(workflow_data['Workflow'][0])
        
        return {
            "status": "success",
            "roles": roles_result,
            "actions": actions_result,
            "states": states_result,
            "transitions": transitions_result,
            "workflow": workflow_result
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



# Comprehensive setup method
@frappe.whitelist()
def complete_bid_document_workflow_setup():
    """
    Comprehensive setup method for Bid Document Workflow
    """
    try:
        # Setup workflow
        workflow_setup = setup_bid_document_workflow()
        
        # Setup role profiles
        role_profiles_setup = create_bid_document_role_profiles()

        users_result = create_bid_user()
        
        return {
            "status": "success",
            "workflow_setup": workflow_setup,
            "role_profiles_setup": role_profiles_setup,
            "user setup" : users_result
        }
    
    except Exception as e:
        frappe.log_error(f"Complete Bid Document Workflow Setup Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }

# Example usage
def workflow_setup_example():
    """
    Example of setting up Bid Document Workflow
    """
    # Call the comprehensive setup method
    result = complete_bid_document_workflow_setup()
    
    # You can add additional logging or processing here
    if result['status'] == 'success':
        print("Bid Document Workflow setup completed successfully")
    else:
        print(f"Workflow setup failed: {result.get('message', 'Unknown error')}")
    
    return result
