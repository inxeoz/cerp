import frappe
from typing import List, Dict, Any

@frappe.whitelist()
def get_merged_bid_workflow_states() -> List[Dict[str, Any]]:
    """Returns merged workflow states configuration"""

    rq_allowed_section = ["status_section", "requirements_section"]

    bccm_allowed_section = rq_allowed_section + ["main_bid_details_section", "committee_section"]

    ubo_allowed_section = bccm_allowed_section + ["ubo_section"]

    bid_published_allowed_section = ubo_allowed_section + ["vendor_query_response_section"]

    corrigendum_allowed_section = bid_published_allowed_section + ["corrigendum_section"]

    tecmom_allowed_section = corrigendum_allowed_section + ["tecmom_section"]

    fecmom_allowed_section = tecmom_allowed_section + ["fecmom_section"]

    workflow_states = [
        {
            "workflow_state_name": "Draft",
            "style": "Primary",
            "icon": "file",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "draft",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": ["Procurement Officer"],
            "only_hide_to": [],
            "visible_section": rq_allowed_section
        },
        {
            "workflow_state_name": "RQ Submitted For Approval",
            "style": "Warning",
            "icon": "share",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for MD Approval",
            "only_allow_edit_for": "Managing Director",
            "only_visible_to": ["Procurement Officer", "Managing Director"],
            "only_hide_to": [],
            "visible_section": rq_allowed_section
        },
        {
            "workflow_state_name": "RQ Approved By MD",
            "style": "Success",
            "icon": "check",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending to creation of BCCM",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": ["Procurement Officer", "Managing Director"],
            "only_hide_to": [],
            "visible_section": rq_allowed_section
        },
        {
            "workflow_state_name": "BCCM Submitted For Approval",
            "style": "Warning",
            "icon": "share",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for PD Approval",
            "only_allow_edit_for": "Project Director",
            "only_visible_to": ["Procurement Officer", "Project Director"],
            "only_hide_to": [],
            "visible_section": bccm_allowed_section
        },
        {
            "workflow_state_name": "BCCM Approved By PD",
            "style": "Info",
            "icon": "user-check",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for CGM Approval",
            "only_allow_edit_for": "Chief General Manager",
            "only_visible_to": ["Procurement Officer", "Project Director", "Chief General Manager"],
            "only_hide_to": [],
            "visible_section": bccm_allowed_section
        },
        {
            "workflow_state_name": "BCCM Approved By CGM",
            "style": "Info",
            "icon": "user-check",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for MD Approval",
            "only_allow_edit_for": "Managing Director",
            "only_visible_to": ["Procurement Officer", "Chief General Manager", "Managing Director"],
            "only_hide_to": [],
            "visible_section": bccm_allowed_section
        },
        {
            "workflow_state_name": "BCCM Approved By MD",
            "style": "Success",
            "icon": "crown",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending to upload BCC Offline",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": ["Procurement Officer", "Managing Director"],
            "only_hide_to": [],
            "visible_section": bccm_allowed_section
        },
        {
            "workflow_state_name": "UBO Submitted For Approval",
            "style": "Warning",
            "icon": "share",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for CGM Approval",
            "only_allow_edit_for": "Chief General Manager",
            "only_visible_to": ["Procurement Officer", "Chief General Manager"],
            "only_hide_to": [],
            "visible_section": ubo_allowed_section
        },
        {
            "workflow_state_name": "UBO Approved By CGM",
            "style": "Info",
            "icon": "user-check",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for MD Approval",
            "only_allow_edit_for": "Managing Director",
            "only_visible_to": ["Procurement Officer", "Chief General Manager", "Managing Director"],
            "only_hide_to": [],
			"visible_section": ubo_allowed_section
        },
        {
            "workflow_state_name": "UBO Approved By MD",
            "style": "Success",
            "icon": "crown",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending to publish bid",
            "only_allow_edit_for": "Marketing Team",
            "only_visible_to": ["Procurement Officer", "Managing Director", "Marketing Team"],
            "only_hide_to": [],
			"visible_section": ubo_allowed_section
        },
        {
            "workflow_state_name": "Bid Published",
            "style": "Success",
            "icon": "globe",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "waiting for Vendors query",
            "only_allow_edit_for": "System Manager",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": bid_published_allowed_section
        },
        {
            "workflow_state_name": "No Vendors Query",
            "style": "Info",
            "icon": "question-circle",
            "doc_status": 0,
            "is_optional_state": 1,
            "update_field": "bid_document_status",
            "update_value": "pending to upload TEC MOM",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": ["Procurement Officer", "Managing Director", "Marketing Team"],
            "only_hide_to": [],
            "visible_section": corrigendum_allowed_section
        },

        {
            "workflow_state_name": "TECMOM Submitted For Approval",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "TECMOM Submitted For Approval",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": tecmom_allowed_section
        },

        {
            "workflow_state_name": "TECMOM Uploaded",
            "style": "Warning",
            "icon": "upload",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for CGM Approval",
            "only_allow_edit_for": "Chief General Manager",
            "only_visible_to": ["Procurement Officer", "Chief General Manager"],
            "only_hide_to": [],
            "visible_section": tecmom_allowed_section
        },
        {
            "workflow_state_name": "TECMOM Approved By CGM",
            "style": "Info",
            "icon": "user-check",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for MD Approval",
            "only_allow_edit_for": "Managing Director",
            "only_visible_to": ["Procurement Officer", "Chief General Manager", "Managing Director"],
            "only_hide_to": [],
            "visible_section": tecmom_allowed_section
        },
        {
            "workflow_state_name": "TECMOM Approved By MD",
            "style": "Success",
            "icon": "crown",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending to upload FECMOM",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": ["Procurement Officer", "Managing Director"],
            "only_hide_to": [],
            "visible_section": tecmom_allowed_section
        },

        {
            "workflow_state_name": "FECMOM Submitted For Approval",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "FECMOM Submitted For Approval",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": fecmom_allowed_section
        },

        {
            "workflow_state_name": "FECMOM Uploaded",
            "style": "Warning",
            "icon": "upload",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for CGM Approval",
            "only_allow_edit_for": "Chief General Manager",
            "only_visible_to": ["Procurement Officer", "Managing Director"],
            "only_hide_to": [],
            "visible_section": fecmom_allowed_section
        },
        {
            "workflow_state_name": "FECMOM Approved By CGM",
            "style": "Info",
            "icon": "user-check",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "pending for MD Approval",
            "only_allow_edit_for": "Managing Director",
            "only_visible_to": ["Procurement Officer", "Chief General Manager", "Managing Director"],
            "only_hide_to": [],
            "visible_section": fecmom_allowed_section
        },
        {
            "workflow_state_name": "FECMOM Approved By MD",
            "style": "Success",
            "icon": "crown",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "Approved",
            "only_allow_edit_for": "System Manager",
            "only_visible_to": ["Procurement Officer", "Managing Director", "Marketing Team"],
            "only_hide_to": [],
            "visible_section": fecmom_allowed_section
        },
        {
            "workflow_state_name": "Rejected",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "Rejected",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": []
        },
        {
            "workflow_state_name": "RQ Rejected By MD",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "RQ Rejected By MD",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": rq_allowed_section
        },
        {
            "workflow_state_name": "BCCM Rejected By PD",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "BCCM Rejected By PD",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": bccm_allowed_section
        },
        {
            "workflow_state_name": "BCCM Rejected By CGM",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "BCCM Rejected By CGM",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": bccm_allowed_section
        },
        {
            "workflow_state_name": "BCCM Rejected By MD",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "BCCM Rejected By MD",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": bccm_allowed_section
        },
        {
            "workflow_state_name": "UBO Rejected By CGM",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "UBO Rejected By CGM",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": ubo_allowed_section
        },
        {
            "workflow_state_name": "UBO Rejected By MD",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "UBO Rejected By MD",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": ubo_allowed_section
        },
        {
            "workflow_state_name": "TECMOM Rejected By CGM",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "TECMOM Rejected By CGM",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": tecmom_allowed_section
        },
        {
            "workflow_state_name": "TECMOM Rejected By MD",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "TECMOM Rejected By MD",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": tecmom_allowed_section
        },
        {
            "workflow_state_name": "FECMOM Rejected By CGM",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "FECMOM Rejected By CGM",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": fecmom_allowed_section
        },
        {
            "workflow_state_name": "FECMOM Rejected By MD",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "FECMOM Rejected By MD",
            "only_allow_edit_for": "Procurement Officer",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": fecmom_allowed_section
        },

        {
            "workflow_state_name": "Vendors Query",
            "style": "Danger",
            "icon": "x-circle",
            "doc_status": 0,
            "is_optional_state": 0,
            "update_field": "bid_document_status",
            "update_value": "Response Sheet Submitetd By Vendors",
            "only_allow_edit_for": "Marketing Team",
            "only_visible_to": [],
            "only_hide_to": [],
            "visible_section": fecmom_allowed_section
        }
    ]

    return workflow_states
