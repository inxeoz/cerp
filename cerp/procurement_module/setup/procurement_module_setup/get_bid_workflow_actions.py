import frappe
from typing import List, Dict, Any

def get_bid_workflow_actions():
    """Returns workflow transitions configuration as a list of dictionaries"""
    
    actions = [
        {
            "workflow_action_name": "Submit RQ For Approval"
        },
        {
            "workflow_action_name": "Approve RQ"
        },
        {
            "workflow_action_name": "Submit BCCM For Approval"
        },
        {
            "workflow_action_name": "Approve BCCM"
        },
        {
            "workflow_action_name": "Submit UBO For Approval"
        },
        {
            "workflow_action_name": "Approve UBO"
        },
        {
            "workflow_action_name": "Publish Bid"
        },
        {
            "workflow_action_name": "Submit for Approval"
        },
        {
            "workflow_action_name": "Approve TECMOM"
        },
        {
            "workflow_action_name": "Approve FECMOM"
        },
        {
            "workflow_action_name": "Reject RQ"
        },
        {
            "workflow_action_name": "Reject BCCM"
        },
        {
            "workflow_action_name": "Reject UBO"
        },
        {
            "workflow_action_name": "Reject TECMOM"
        },
        {
            "workflow_action_name": "Reject FECMOM"
        },
        {
            "workflow_action_name": "Submit TECMOM For Approval"
        },
        {
            "workflow_action_name": "Submit FECMOM For Approval"
        },

        {
              "workflow_action_name":  "Submit As No Vendors Query"
        },

        {
            "workflow_action_name":   "Submit As Vendors Query"
        }
    ]
    
    return actions