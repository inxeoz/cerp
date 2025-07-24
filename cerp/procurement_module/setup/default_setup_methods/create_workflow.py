import frappe
from typing import List, Dict, Union, Any


def create_workflow(workflow_data: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Create workflow with flexible configuration
    
    Example Data Structures:
    
    # Workflow Configuration
    workflow_config = {
        "workflow_name": "Purchase Request Workflow",  # Unique workflow name
        "document_type": "Purchase Request",           # DocType for workflow
        "is_active": 1,                                # Workflow active status
        "send_email_alert": 0,                         # Email alert flag
        "states": [                                    # Workflow states
            {
                "state": "Draft",
                "doc_status": 0,
                "allow_edit": "Requestor"
            },
            {
                "state": "Pending Approval",
                "doc_status": 0,
                "allow_edit": "Approver"
            }
        ],
        "transitions": [                               # Workflow transitions
            {
                "state": "Draft",
                "action": "Submit",
                "next_state": "Pending Approval",
                "allowed": "Requestor"
            },
            {
                "state": "Pending Approval",
                "action": "Approve",
                "next_state": "Approved",
                "allowed": "Approver"
            }
        ]
    }
    
    Args:
        workflow_data (Dict, optional): Workflow configuration
    
    Returns:
        Dict containing creation details
    """
    try:
        # If no data provided, use default method
        if workflow_data is None:
            workflow_data = _get_default_workflow()
        
        workflow_name = workflow_data.get('workflow_name')
        
        # Check if workflow exists
        if frappe.db.exists("Workflow", workflow_name):
            return {
                "status": "exists",
                "workflow_name": workflow_name
            }
        
        try:
            # Create workflow
            new_workflow = frappe.get_doc({
                "doctype": "Workflow",
                "workflow_name": workflow_name,
                "document_type": workflow_data.get('document_type', ''),
                "is_active": workflow_data.get('is_active', 1),
                "send_email_alert": workflow_data.get('send_email_alert', 0)
            })
            
            # Add workflow states
            for state in workflow_data.get('states', []):
                new_workflow.append("states", state)
            
            # Add workflow transitions
            for transition in workflow_data.get('transitions', []):
                new_workflow.append("transitions", transition)
            
            # Insert workflow
            new_workflow.insert(ignore_permissions=True)
            
            frappe.db.commit()
            
            return {
                "status": "success",
                "workflow_name": workflow_name
            }
        
        except Exception as workflow_error:
            frappe.log_error(f"Error creating workflow {workflow_name}: {str(workflow_error)}")
            return {
                "status": "error",
                "message": str(workflow_error)
            }
    
    except Exception as e:
        frappe.log_error(f"Workflow Creation Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }
