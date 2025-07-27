

import frappe
from typing import List, Dict, Any

from cerp.procurement_module.setup.procurement_module_setup.bid_doc_role_create import create_bid_roles
from cerp.procurement_module.setup.procurement_module_setup.bid_doc_workflow_action_master_create import create_bid_doc_workflow_actions
from cerp.procurement_module.setup.procurement_module_setup.bid_doc_workflow_states_create import create_bid_doc_workflow_states
from cerp.procurement_module.setup.procurement_module_setup.bid_doc_workflow_transition_create import create_bid_doc_workflow_transitions

from cerp.procurement_module.setup.procurement_module_setup.bid_doc_workflow_create import create_bid_workflow

from cerp.procurement_module.setup.procurement_module_setup.bid_doc_role_profile_create import create_bid_doc_role_profiles

from cerp.procurement_module.setup.procurement_module_setup.bid_doc_user_create import create_bid_user



def create_bid_doc_workflow_combined():
    """
    Comprehensive method to create Bid Document Workflow
    
    Uses general methods to create all workflow components
    """
    try:
        # Create roles
        roles_result = create_bid_roles()
        
        # Create workflow actions
        actions_result = create_bid_doc_workflow_actions()
        
        # Create workflow states
        states_result = create_bid_doc_workflow_states()
        
        # Create workflow transitions
        transitions_result = create_bid_doc_workflow_transitions()
        
        # Create workflow
        workflow_result = create_bid_workflow()

        role_profiles_setup = create_bid_doc_role_profiles()

        users_result = create_bid_user()
        
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
