import frappe

def get_workflow_transitions_table():
    """Returns workflow transitions configuration as a list of dictionaries"""
    
    workflow_transitions = [
        {
            "no": 1,
            "state": "Draft",
            "action": "Submit for Approval",
            "next_state": "RQ Submitted For Approval",
            "allowed": "Procurement Officer"
        },
        {
            "no": 2,
            "state": "RQ Submitted For Approval",
            "action": "Approve",
            "next_state": "RQ Approved",
            "allowed": "Managing Director"
        },
        {
            "no": 3,
            "state": "RQ Approved",
            "action": "Submit for Approval",
            "next_state": "BCCM Submitted For Approval",
            "allowed": "Procurement Officer"
        },
        {
            "no": 4,
            "state": "BCCM Submitted For Approval",
            "action": "Verify",
            "next_state": "BCCM Verified By PD",
            "allowed": "Project Director"
        },
        {
            "no": 5,
            "state": "BCCM Verified By PD",
            "action": "Verify",
            "next_state": "BCCM Verified By CGM",
            "allowed": "Chief General Manager"
        },
        {
            "no": 6,
            "state": "BCCM Verified By CGM",
            "action": "Verify",
            "next_state": "BCCM Verified By MD",
            "allowed": "Managing Director"
        },
        {
            "no": 7,
            "state": "BCCM Verified By MD",
            "action": "Submit for Approval",
            "next_state": "UBO Submitted For Approval",
            "allowed": "Procurement Officer"
        },
        {
            "no": 8,
            "state": "UBO Submitted For Approval",
            "action": "Verify",
            "next_state": "UBO Verified By CGM",
            "allowed": "Chief General Manager"
        },
        {
            "no": 9,
            "state": "UBO Verified By CGM",
            "action": "Verify",
            "next_state": "UBO Verified By MD",
            "allowed": "Managing Director"
        },
        {
            "no": 10,
            "state": "UBO Verified By MD",
            "action": "Publish",
            "next_state": "Bid Published",
            "allowed": "Marketing Team"
        },
        {
            "no": 11,
            "state": "No Vendors Query",
            "action": "Submit for Approval",
            "next_state": "TEC MOM Uploaded",
            "allowed": "Procurement Officer"
        },
        {
            "no": 12,
            "state": "TEC MOM Uploaded",
            "action": "Verify",
            "next_state": "TEC MOM Verified By CGM",
            "allowed": "Chief General Manager"
        },
        {
            "no": 13,
            "state": "TEC MOM Verified By CGM",
            "action": "Verify",
            "next_state": "TEC MOM Verified By MD",
            "allowed": "Managing Director"
        },
        {
            "no": 14,
            "state": "TEC MOM Verified By MD",
            "action": "Submit for Approval",
            "next_state": "FEC MOM Uploaded",
            "allowed": "Procurement Officer"
        },
        {
            "no": 15,
            "state": "FEC MOM Uploaded",
            "action": "Verify",
            "next_state": "FEC MOM Verified By CGM",
            "allowed": "Chief General Manager"
        },
        {
            "no": 16,
            "state": "FEC MOM Verified By CGM",
            "action": "Verify",
            "next_state": "FEC MOM Verified By MD",
            "allowed": "Managing Director"
        },
        # Reject transitions
        {
            "no": 17,
            "state": "RQ Submitted For Approval",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Managing Director"
        },
        {
            "no": 18,
            "state": "BCCM Submitted For Approval",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Project Director"
        },
        {
            "no": 19,
            "state": "BCCM Verified By PD",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Chief General Manager"
        },
        {
            "no": 20,
            "state": "BCCM Verified By CGM",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Managing Director"
        },
        {
            "no": 21,
            "state": "UBO Submitted For Approval",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Chief General Manager"
        },
        {
            "no": 22,
            "state": "UBO Verified By CGM",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Managing Director"
        },
        {
            "no": 23,
            "state": "TEC MOM Uploaded",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Chief General Manager"
        },
        {
            "no": 24,
            "state": "TEC MOM Verified By CGM",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Managing Director"
        },
        {
            "no": 25,
            "state": "FEC MOM Uploaded",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Chief General Manager"
        },
        {
            "no": 26,
            "state": "FEC MOM Verified By CGM",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Managing Director"
        }
    ]
    
    return workflow_transitions