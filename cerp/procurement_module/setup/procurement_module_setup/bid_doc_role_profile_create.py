

import frappe
from typing import List, Dict, Any

from cerp.procurement_module.setup.default_setup_methods.create_role_profile import create_role_profile


from cerp.procurement_module.setup.procurement_module_setup.get_bid_doc_workflow_states import get_merged_bid_workflow_states

from cerp.procurement_module.setup.default_setup_methods.validate_icon import validate_workflow_icon

def create_bid_doc_role_profiles():
    """
    Create role profiles for Bid Document Workflow
    """
    try:
        # Get workflow transitions
        workflow_states = get_merged_bid_workflow_states()
        
        # Extract unique roles from workflow transitions
        roles = list(set(state['only_allow_edit_for'] for state in workflow_states))
        
        # Prepare role profiles
        role_profiles = [
            {
                "role_profile": f"{role} Profile",
                "roles": [{"role": role}],
                "description": f"Workflow profile for {role}"
            }
            for role in roles
        ]
        
        # Create role profiles
        role_profiles_result = create_role_profile(role_profiles)
        
        return {
            "status": "success",
            "role_profiles": role_profiles_result
        }
    
    except Exception as e:
        frappe.log_error(f"Bid Document Role Profiles Setup Error: {str(e)}")
        return {
            "status": "error", 
            "message": str(e)
        }