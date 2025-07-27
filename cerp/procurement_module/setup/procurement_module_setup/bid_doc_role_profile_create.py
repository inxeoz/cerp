

import frappe
from typing import List, Dict, Any

from cerp.procurement_module.setup.default_setup_methods.create_role_profile import create_role_profile


from cerp.procurement_module.setup.procurement_module_setup.get_bid_roles import get_bid_roles

from cerp.procurement_module.setup.default_setup_methods.validate_icon import validate_workflow_icon

def create_bid_doc_role_profiles():
    """
    Create role profiles for Bid Document Workflow
    """
    try:
        
        # Extract unique roles from workflow transitions
        profiles = list(set(profile['role_name'] for profile in get_bid_roles()))
        
        # Prepare role profiles
        role_profiles = [
            {
                "role_profile": f"{profile} Profile",
                "roles": [{"role": profile}],
                "description": f"Workflow profile for {profile}"
            }
            for profile in profiles
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