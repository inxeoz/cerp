import frappe
from typing import List, Dict, Any

def get_bid_users():
    """Returns users configuration"""
    
    users = [
        {
            "user_first_name": "Proc",                         
            "user_email": "1@inxeoz.com",                
            "role_profile_name": "Procurement Officer Profile" ,
            "new_password" : "asd@123",
            "allowed_modules": ["Procurement Module" , "Desk"]    
        },
        {
            "user_first_name": "Dir",                     
            "user_email": "2@inxeoz.com",               
            "role_profile_name": "Project Director Profile" ,
            "new_password" : "asd@123",
            "allowed_modules": ["Procurement Module" , "Desk"] 
        },
        {
            "user_first_name": "Chief",                     
            "user_email": "3@inxeoz.com",               
            "role_profile_name": "Chief General Manager Profile" ,
            "new_password" : "asd@123",
            "allowed_modules": ["Procurement Module" , "Desk"] 
        },
        {
            "user_first_name": "Man",                     
            "user_email": "4@inxeoz.com",               
            "role_profile_name": "Managing Director Profile" ,
            "new_password" : "asd@123",
            "allowed_modules": ["Procurement Module" , "Desk"] 
        },
        {
            "user_first_name": "MKT",                     
            "user_email": "5@inxeoz.com",               
            "role_profile_name": "Marketing Team Profile" ,
            "new_password" : "asd@123",
            "allowed_modules": ["Procurement Module" , "Desk"] 
        },

        {
            "user_first_name": "VEN1",                     
            "user_email": "6@inxeoz.com",               
            "role_profile_name": "Vendor Profile" ,
            "new_password" : "asd@123",
            "allowed_modules": ["Procurement Module" , "Desk"] 
        }
        {
            "user_first_name": "VEN2",                     
            "user_email": "7@inxeoz.com",               
            "role_profile_name": "Vendor Profile" ,
            "new_password" : "asd@123",
            "allowed_modules": ["Procurement Module" , "Desk"] 
        }
        
    ]
    
    return users