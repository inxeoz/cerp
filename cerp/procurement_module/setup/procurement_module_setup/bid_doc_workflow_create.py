

import frappe
from typing import List, Dict, Any


from cerp.procurement_module.setup.default_setup_methods.create_workflow import create_workflow

from cerp.procurement_module.setup.procurement_module_setup.get_bid_doc_workflow_states import get_merged_bid_workflow_states
from cerp.procurement_module.setup.procurement_module_setup.get_bid_workflow_transition import get_workflow_transitions_table


def create_bid_workflow() -> Dict[str, Any]:

    try:

        # Extract unique roles from workflow transitions
        workflow_transitions = get_workflow_transitions_table()
        # Prepare workflow states
        workflow_states = get_merged_bid_workflow_states()

        Workflow= {
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
                        "allowed": transition['allowed'],
                        "condition" : transition['condition']
                    } for transition in workflow_transitions
                ]
            }

        # Create workflow
        workflow_result = create_workflow(Workflow)
        
        return {
            "workflow": workflow_result
        }
    
    except Exception as e:
        frappe.log_error(f"Bid Document Workflow Setup Error: {str(e)}")
        return {
            "status": "error", 
            "message": str(e)
        }

