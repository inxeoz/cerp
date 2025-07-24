import frappe
from typing import List, Dict, Union, Any

def create_workflow_action_master(actions_data: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create workflow action masters with flexible configuration
    
    Example Data Structures:
    
    # Single Workflow Action Configuration
    single_workflow_action = {
        "workflow_action_name": "Submit",      # Unique action name
        "description": "Submit document for approval" # Optional description
    }
    
    # Multiple Workflow Actions Configuration
    multiple_workflow_actions = [
        {
            "workflow_action_name": "Approve",
            "description": "Approve the document"
        },
        {
            "workflow_action_name": "Reject",
            "description": "Reject the document"
        }
    ]
    
    Args:
        actions_data (List[Dict], optional): List of action master configurations
    
    Returns:
        Dict containing creation details
    """
    try:
        # If no data provided, use default method
        if actions_data is None:
            actions_data = _get_default_workflow_actions()
        
        created_actions = []
        existing_actions = []
        
        for action_config in actions_data:
            action_name = action_config.get('workflow_action_name')
            
            if not action_name:
                continue
            
            # Check if workflow action exists
            if not frappe.db.exists("Workflow Action Master", action_name):
                try:
                    new_action = frappe.get_doc({
                        "doctype": "Workflow Action Master",
                        "workflow_action_name": action_name,
                        "description": action_config.get('description', '')
                    }).insert(ignore_permissions=True)
                    
                    created_actions.append(action_name)
                except Exception as action_error:
                    frappe.log_error(f"Error creating workflow action {action_name}: {str(action_error)}")
            else:
                existing_actions.append(action_name)
        
        frappe.db.commit()
        
        return {
            "status": "success",
            "created_actions": created_actions,
            "existing_actions": existing_actions
        }
    
    except Exception as e:
        frappe.log_error(f"Workflow Action Master Creation Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }
