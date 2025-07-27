import frappe
from typing import List, Dict, Any

def get_bid_roles():

    """Returns roles configuration"""
    
    roles = [

        {
        "role_name":  "Procurement Officer" ,      # Required unique role name
        "desk_access": 1,                      # Desktop access (default: 1)
        "disabled": 0,                         # Role disabled status (default: 0)
        "description": "details" # Optional description
        },

        {
        "role_name":  "Project Director" ,       # Required unique role name
        "desk_access": 1,                      # Desktop access (default: 1)
        "disabled": 0,                         # Role disabled status (default: 0)
        "description": "details" # Optional description
        },

        {
        "role_name": "Chief General Manager" ,      # Required unique role name
        "desk_access": 1,                      # Desktop access (default: 1)
        "disabled": 0,                         # Role disabled status (default: 0)
        "description": "details" # Optional description
        },

        {
        "role_name": "Managing Director" ,     # Required unique role name
        "desk_access": 1,                      # Desktop access (default: 1)
        "disabled": 0,                         # Role disabled status (default: 0)
        "description": "details" # Optional description
        },
         {
        "role_name": "Marketing Team" ,     # Required unique role name
        "desk_access": 1,                      # Desktop access (default: 1)
        "disabled": 0,                         # Role disabled status (default: 0)
        "description": "details" # Optional description
        }    
        
         ]
    
    return roles