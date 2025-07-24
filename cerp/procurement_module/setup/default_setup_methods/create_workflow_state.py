import frappe
from typing import List, Dict, Union, Any



def create_workflow_state(workflow_states_data: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create workflow states with flexible configuration
    
    Example Data Structures:
    
    # Single Workflow State Configuration
    single_workflow_state = {
        "workflow_state_name": "Draft",        # Unique state name
        "style": "Primary",                    # UI style (optional)
        "icon": "file",                        # State icon (optional)
        "doc_status": 0,                       # Document status
        "is_optional_state": 0                 # Optional state flag
    }
    
    # Multiple Workflow States Configuration
    multiple_workflow_states = [
        {
            "workflow_state_name": "Pending Approval",
            "style": "Warning",
            "icon": "send",
            "doc_status": 0
        },
        {
            "workflow_state_name": "Approved",
            "style": "Success",
            "icon": "check",
            "doc_status": 1
        }
    ]
    
    Args:
        workflow_states_data (List[Dict], optional): List of workflow state configurations
    
    Returns:
        Dict containing creation details
    """
    try:
        # If no data provided, use default method
        if workflow_states_data is None:
            workflow_states_data = _get_default_workflow_states()
        
        created_states = []
        existing_states = []
        
        for state_config in workflow_states_data:
            state_name = state_config.get('workflow_state_name')
            
            if not state_name:
                continue
            
            # Check if workflow state exists
            if not frappe.db.exists("Workflow State", state_name):
                try:
                    new_state = frappe.get_doc({
                        "doctype": "Workflow State",
                        "workflow_state_name": state_name,
                        "style": state_config.get('style', ''),
                        "icon": state_config.get('icon', ''),
                        "doc_status": state_config.get('doc_status', 0),
                        "is_optional_state": state_config.get('is_optional_state', 0)
                    }).insert(ignore_permissions=True)
                    
                    created_states.append(state_name)
                except Exception as state_error:
                    frappe.log_error(f"Error creating workflow state {state_name}: {str(state_error)}")
            else:
                existing_states.append(state_name)
        
        frappe.db.commit()
        
        return {
            "status": "success",
            "created_states": created_states,
            "existing_states": existing_states
        }
    
    except Exception as e:
        frappe.log_error(f"Workflow State Creation Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }
