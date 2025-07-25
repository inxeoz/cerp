import frappe
from typing import List, Dict, Union, Any

from cerp.procurement_module.setup.default_setup_methods.validate_icon import validate_workflow_icon


def create_workflow_state(workflow_states_data: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create workflow states with flexible configuration and icon validation
    
    Args:
        workflow_states_data (List[Dict], optional): List of workflow state configurations
    
    Returns:
        Dict containing creation details
    """
    try:
        # If no data provided, use default method
        if workflow_states_data is None:
            workflow_states_data = []
        
        created_states = []
        existing_states = []
        failed_states = []
        
        for state_config in workflow_states_data:
            state_name = state_config.get('workflow_state_name')
            
            if not state_name:
                continue
            
            # Validate icon using imported function
            icon = validate_workflow_icon(state_config.get('icon', ''))
            
            try:
                # Check if workflow state exists
                if not frappe.db.exists("Workflow State", state_name):
                    new_state = frappe.get_doc({
                        "doctype": "Workflow State",
                        "workflow_state_name": state_name,
                        "style": state_config.get('style', ''),
                        "icon": icon,  # Use validated icon
                        "doc_status": state_config.get('doc_status', 0),
                        "is_optional_state": state_config.get('is_optional_state', 0)
                    })
                    if state_config.get('update_field'):
                        new_state.update_field = state_config.get('update_field')
                    
                    if state_config.get('update_value'):
                        new_state.update_value = state_config.get('update_value')

                    new_state.insert(ignore_permissions=True)
                    
                    created_states.append(state_name)
                else:
                    existing_states.append(state_name)
            
            except Exception as state_error:
                # Capture detailed error information
                error_info = {
                    "state_name": state_name,
                    "icon": icon,
                    "error": str(state_error)
                }
                failed_states.append(error_info)
                
                # Log error with a descriptive message
                frappe.log_error(
                    title=f"Workflow State Creation Error: {state_name}",
                    message=str(error_info)
                )
        
        # Commit database changes
        frappe.db.commit()
        
        # Determine overall status
        status = "success"
        if failed_states:
            status = "partial_error"
        
        return {
            "status": status,
            "created_states": created_states,
            "existing_states": existing_states,
            "failed_states": failed_states
        }
    
    except Exception as e:
        # Capture any unexpected errors during the entire process
        frappe.log_error(
            title="Workflow State Creation Global Error",
            message=str(e)
        )
        return {
            "status": "error",
            "message": str(e)
        }