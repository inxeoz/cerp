import frappe
from typing import List, Dict, Union, Any

# Comprehensive setup function
def comprehensive_workflow_setup(
    roles_data: List[Dict[str, Any]] = None,
    role_profiles_data: List[Dict[str, Any]] = None,
    workflow_states_data: List[Dict[str, Any]] = None,
    workflow_actions_data: List[Dict[str, Any]] = None,
    workflow_data: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Example Usage:
    
    workflow_setup_config = {
        "roles_data": [
            {"role_name": "Purchase Manager"},
            {"role_name": "Finance Approver"}
        ],
        "role_profiles_data": [
            {
                "role_profile_name": "Purchase Workflow Profile",
                "roles": [
                    {"role": "Purchase Manager"},
                    {"role": "Finance Approver"}
                ]
            }
        ],
        "workflow_states_data": [
            {"workflow_state_name": "Draft", "style": "Primary"},
            {"workflow_state_name": "Approved", "style": "Success"}
        ],
        "workflow_actions_data": [
            {"workflow_action_name": "Submit"},
            {"workflow_action_name": "Approve"}
        ],
        "workflow_data": {
            "workflow_name": "Purchase Request Workflow",
            "document_type": "Purchase Request"
            # ... other workflow configuration
        }
    }
    
    # Call the setup function
    result = comprehensive_workflow_setup(**workflow_setup_config)
    """
    try:
        # Setup components in order
        roles_result = create_role(roles_data)
        role_profiles_result = create_role_profile(role_profiles_data)
        workflow_states_result = create_workflow_state(workflow_states_data)
        workflow_actions_result = create_workflow_action_master(workflow_actions_data)
        workflow_result = create_workflow(workflow_data)
        
        return {
            "status": "success",
            "roles": roles_result,
            "role_profiles": role_profiles_result,
            "workflow_states": workflow_states_result,
            "workflow_actions": workflow_actions_result,
            "workflow": workflow_result
        }
    
    except Exception as e:
        frappe.log_error(f"Comprehensive Workflow Setup Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }

# Expose as whitelisted method
@frappe.whitelist()
def setup_workflow_components(
    roles_data=None,
    role_profiles_data=None,
    workflow_states_data=None,
    workflow_actions_data=None,
    workflow_data=None
):