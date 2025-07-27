

import frappe
from typing import List, Dict, Any

# from cerp.procurement_module.setup.procurement_module_setup.bid_doc_role_create import create_bid_roles
from cerp.procurement_module.setup.procurement_module_setup.bid_doc_workflow_action_master_create import create_bid_doc_workflow_actions
from cerp.procurement_module.setup.procurement_module_setup.bid_doc_workflow_states_create import create_bid_document_workflow_states
from cerp.procurement_module.setup.procurement_module_setup.bid_doc_workflow_transition_create import create_bid_doc_workflow_transitions

from cerp.procurement_module.setup.procurement_module_setup.bid_doc_workflow_create import create_bid_workflow

from cerp.procurement_module.setup.procurement_module_setup.bid_doc_role_profile_create import create_bid_doc_role_profiles

from cerp.procurement_module.setup.procurement_module_setup.bid_doc_user_create import create_bid_user


from cerp.procurement_module.setup.procurement_module_setup.bid_doc_workspace_create import create_bid_workspace

from cerp.procurement_module.setup.procurement_module_setup.bid_doc_html_block_create import create_bid_name_email_html_block


def create_bid_doc_workflow_combined():
    """
    Comprehensive method to create Bid Document Workflow
    
    Uses general methods to create all workflow components
    """
    try:
        # Create roles
        #roles_result = create_bid_roles() # roles will be added through document 
        
        # Create workflow actions
        actions_result = create_bid_doc_workflow_actions() #done
        
        # Create workflow states
        states_result = create_bid_document_workflow_states() #done

        # Create workflow
        workflow_result = create_bid_workflow() #done
        
        # Create workflow transitions
        transitions_result = create_bid_doc_workflow_transitions() #done from create_bid_workflow
        

        role_profiles_setup = create_bid_doc_role_profiles() # done

        users_result = create_bid_user() # done

        workspace_result = create_bid_workspace() #done

        custom_html_block_result = create_bid_name_email_html_block() #done
        
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
