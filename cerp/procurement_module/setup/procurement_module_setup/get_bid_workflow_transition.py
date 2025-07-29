import frappe
from typing import List, Dict, Any

def get_workflow_transitions_table():
    """Returns workflow transitions configuration as a list of dictionaries"""
    
    workflow_transitions = [
        {
            "no": 1,
            "state": "Draft",
            "action": "Submit RQ For Approval",
            "next_state": "RQ Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },
        {
            "no": 2,
            "state": "RQ Submitted For Approval",
            "action": "Approve RQ",
            "next_state": "RQ Approved By MD",
            "allowed": "Managing Director",
            "condition" : ""
        },
        {
            "no": 3,
            "state": "RQ Approved By MD",
            "action": "Submit BCCM For Approval",
            "next_state": "BCCM Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },
        {
            "no": 4,
            "state": "BCCM Submitted For Approval",
            "action": "Approve BCCM",
            "next_state": "BCCM Approved By PD",
            "allowed": "Project Director",
            "condition" : ""
        },
        {
            "no": 5,
            "state": "BCCM Approved By PD",
            "action": "Approve BCCM",
            "next_state": "BCCM Approved By CGM",
            "allowed": "Chief General Manager",
            "condition" : ""
        },
        {
            "no": 6,
            "state": "BCCM Approved By CGM",
            "action": "Approve BCCM",
            "next_state": "BCCM Approved By MD",
            "allowed": "Managing Director",
            "condition" : ""
        },
        {
            "no": 7,
            "state": "BCCM Approved By MD",
            "action": "Submit UBO For Approval",
            "next_state": "UBO Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition": (
                "doc.get('ubo_upload_status') and "
                "doc.get('ubo_upload_status') == 1"
            )
        },
        {
            "no": 8,
            "state": "UBO Submitted For Approval",
            "action": "Approve UBO",
            "next_state": "UBO Approved By CGM",
            "allowed": "Chief General Manager",
            "condition" : ""
        },
        {
            "no": 9,
            "state": "UBO Approved By CGM",
            "action": "Approve UBO",
            "next_state": "UBO Approved By MD",
            "allowed": "Managing Director",
            "condition" : ""
        },
        {
            "no": 10,
            "state": "UBO Approved By MD",
            "action": "Publish Bid",
            "next_state": "Bid Published",
            "allowed": "Marketing Team",
            "condition" : ""
        },
        
        {
            "no": 11,
            "state": "No Vendors Query",
            "action": "Submit for Approval",
            "next_state": "TECMOM Uploaded",
            "allowed": "Procurement Officer",
            "condition" : ""
        },
        {
            "no": 12,
            "state": "TECMOM Uploaded",
            "action": "Approve TECMOM",
            "next_state": "TECMOM Approved By CGM",
            "allowed": "Chief General Manager",
            "condition" : ""
        },
        {
            "no": 13,
            "state": "TECMOM Approved By CGM",
            "action": "Approve TECMOM",
            "next_state": "TECMOM Approved By MD",
            "allowed": "Managing Director",
            "condition" : ""
        },
        {
            "no": 14,
            "state": "TECMOM Approved By MD",
            "action": "Submit for Approval",
            "next_state": "FECMOM Uploaded",
            "allowed": "Procurement Officer",
            "condition" : ""
        },
        {
            "no": 15,
            "state": "FECMOM Uploaded",
            "action": "Approve FECMOM",
            "next_state": "FECMOM Approved By CGM",
            "allowed": "Chief General Manager",
            "condition" : ""
        },
        {
            "no": 16,
            "state": "FECMOM Approved By CGM",
            "action": "Approve FECMOM",
            "next_state": "FECMOM Approved By MD",
            "allowed": "Managing Director",
            "condition" : ""
        },



        
        # Reject transitions
        {
            "no": 17,
            "state": "RQ Submitted For Approval",
            "action": "Reject RQ",
            "next_state": "RQ Rejected By MD",
            "allowed": "Managing Director",
            "condition" : ""
        },
        {
            "no": 18,
            "state": "BCCM Submitted For Approval",
            "action": "Reject BCCM",
            "next_state": "BCCM Rejected By PD",
            "allowed": "Project Director",
            "condition" : ""
        },
        {
            "no": 19,
            "state": "BCCM Approved By PD",
            "action": "Reject BCCM",
            "next_state": "BCCM Rejected By CGM",
            "allowed": "Chief General Manager",
            "condition" : ""
        },
        {
            "no": 20,
            "state": "BCCM Approved By CGM",
            "action": "Reject BCCM",
            "next_state": "BCCM Rejected By MD",
            "allowed": "Managing Director",
            "condition" : ""
        },
        {
            "no": 21,
            "state": "UBO Submitted For Approval",
            "action": "Reject UBO",
            "next_state": "UBO Rejected By CGM",
            "allowed": "Chief General Manager",
            "condition" : ""
        },
        {
            "no": 22,
            "state": "UBO Approved By CGM",
            "action": "Reject UBO",
            "next_state": "UBO Rejected By MD",
            "allowed": "Managing Director",
            "condition" : ""
        },
        {
            "no": 23,
            "state": "TECMOM Uploaded",
            "action": "Reject TECMOM",
            "next_state": "TECMOM Rejected By CGM",
            "allowed": "Chief General Manager",
            "condition" : ""
        },
        {
            "no": 24,
            "state": "TECMOM Approved By CGM",
            "action": "Reject TECMOM",
            "next_state": "TECMOM Rejected By MD",
            "allowed": "Managing Director",
            "condition" : ""
        },
        {
            "no": 25,
            "state": "FECMOM Uploaded",
            "action": "Reject FECMOM",
            "next_state": "FECMOM Rejected By CGM",
            "allowed": "Chief General Manager",
            "condition" : ""
        },
        {
            "no": 26,
            "state": "FECMOM Approved By CGM",
            "action": "Reject FECMOM",
            "next_state": "FECMOM Rejected By MD",
            "allowed": "Managing Director",
            "condition" : ""
        },



        #Rejcted to working state

        {
            "no": 27,
            "state": "RQ Rejected By MD",
            "action": "Submit RQ For Approval",
            "next_state": "RQ Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },


        {
            "no": 28,
            "state": "BCCM Rejected By PD",
            "action":  "Submit BCCM For Approval",
            "next_state": "BCCM Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },
        {
            "no": 29,
            "state": "BCCM Rejected By CGM",
            "action":  "Submit BCCM For Approval",
            "next_state": "BCCM Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },
        {
            "no": 30,
            "state": "BCCM Rejected By MD",
            "action":  "Submit BCCM For Approval",
            "next_state": "BCCM Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },


        {
            "no": 31,
            "state": "UBO Rejected By CGM",
            "action":  "Submit UBO For Approval",
            "next_state": "UBO Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },

        {
            "no": 32,
            "state": "UBO Rejected By MD",
            "action":  "Submit UBO For Approval",
            "next_state": "UBO Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },





        {
            "no": 33,
            "state": "TECMOM Rejected By CGM",
            "action":  "Submit TECMOM For Approval",
            "next_state": "TECMOM Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },

        {
            "no": 34,
            "state": "TECMOM Rejected By MD",
            "action":  "Submit TECMOM For Approval",
            "next_state": "TECMOM Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },





        {
            "no": 35,
            "state": "FECMOM Rejected By CGM",
            "action":  "Submit FECMOM For Approval",
            "next_state": "FECMOM Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },
        {
            "no": 36,
            "state": "FECMOM Rejected By MD",
            "action":  "Submit FECMOM For Approval",
            "next_state": "FECMOM Submitted For Approval",
            "allowed": "Procurement Officer",
            "condition" : ""
        },


        {
            "no": 37,
            "state": "Bid Published",
            "action":  "Submit As No Vendors Query",
            "next_state": "No Vendors Query",
            "allowed": "Marketing Team",
            "condition": (
                "doc.get('workflow_state') == 'Bid Published' and "
                "doc.get('vendors_query_response') and "
                "doc.get('vendors_query_response') == []"
            )
        },
        {
            "no": 38,
            "state": "Bid Published",
            "action":  "Submit As Vendors Query",
            "next_state": "Vendors Query",
            "allowed": "Marketing Team",
            "condition": (
                "doc.get('workflow_state') == 'Bid Published' and "
                "doc.get('vendors_query_response') and "
                "doc.get('vendors_query_response') != []"
            )

        }

    ]
    
    return workflow_transitions