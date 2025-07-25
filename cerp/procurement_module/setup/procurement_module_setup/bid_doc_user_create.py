

import frappe
from typing import List, Dict, Any

from cerp.procurement_module.setup.default_setup_methods.create_user import create_user
from cerp.procurement_module.setup.procurement_module_setup.get_bid_doc_users import get_bid_users

def create_bid_user():
    """
    Create role profiles for Bid Document Workflow
    """
    try:
        # Get workflow transitions
        users = get_bid_users()
        
        # Create role profiles
        user_create_result = create_user(users)
        
        return {
            "status": "success",
            "role_profiles": user_create_result
        }
    
    except Exception as e:
        frappe.log_error(f"Bid Document User Setup Error: {str(e)}")
        return {
            "status": "error", 
            "message": str(e)
        }