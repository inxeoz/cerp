

import frappe
from typing import List, Dict, Any

from cerp.procurement_module.setup.default_setup_methods.create_workflow_state import create_workflow_state

from cerp.procurement_module.setup.procurement_module_setup.get_bid_doc_workflow_states import get_merged_bid_workflow_states



def create_bid_document_workflow_states():

    try:
        # Create workflow states
        states = get_merged_bid_workflow_states()
        states_result = create_workflow_state(states)
      
        return {
            "status": "success",
            "states": states_result,
        }
    
    except Exception as e:
        frappe.log_error(f"Bid Document Workflow Setup Error: {str(e)}")
        return {
            "status": "error", 
            "message": str(e)
        }
