import frappe
from typing import List, Dict, Any

from cerp.procurement_module.setup.default_setup_methods.create_role import create_role
from cerp.procurement_module.setup.procurement_module_setup.get_bid_roles import get_bid_roles

def create_bid_roles() -> Dict[str, Any]:
    """
    Prepare comprehensive workflow data for Bid Document
    
    Returns:
        Dict containing all workflow components
    """
    try:
            
        # Extract unique roles from workflow transitions
        roles = get_bid_roles()

        roles_result = create_role(roles)

        return {
            "roles": roles_result
        }
        
    except Exception as e:
        frappe.log_error(f"Bid Document Workflow Setup Error: {str(e)}")
        return {
            "status": "error", 
            "message": str(e)
        }

