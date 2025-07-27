

import frappe
from typing import List, Dict, Any


from cerp.procurement_module.setup.default_setup_methods.create_workflow_action_master import create_workflow_action_master

from cerp.procurement_module.setup.procurement_module_setup.get_bid_workflow_actions import get_bid_workflow_actions


def create_bid_doc_workflow_actions() -> Dict[str, Any]:

    try:

        # Extract unique roles from workflow transitions
        actions = get_bid_workflow_actions()

        actions_result = create_workflow_action_master(actions)

        return {
            "actions": actions_result,
        }
    
    except Exception as e:
        frappe.log_error(f"Bid Document Workflow Setup Error: {str(e)}")
        return {
            "status": "error", 
            "message": str(e)
        }
