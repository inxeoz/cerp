import frappe
from typing import List, Dict, Any

def get_bid_users():
    """Returns users configuration"""
    
    users = [
        {
            "user_first_name": "Ravi",                         
            "user_email": "inxeoz@inxeoz.com",                
            "role_profile_name": "Procurement Officer Profile" 
        },
        {
            "user_first_name": "Kishan",                     
            "user_email": "kishan@inxeoz.com",               
            "role_profile_name": "Procurement Officer Profile" 
        },

         {
            "user_first_name": "Yadav",                     
            "user_email": "yadav@inxeoz.com",               
            "role_profile_name": "Procurement Officer Profile" 
        }
    ]
    
    return users