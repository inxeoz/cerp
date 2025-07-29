# # Copyright (c) 2025, inxeoz and contributors
# # For license information, please see license.txt

import frappe
from frappe.model.document import Document
import logging

from cerp.procurement_module.setup.procurement_module_setup.get_bid_doc_workflow_states import get_merged_bid_workflow_states

#To Hide Draft state Bid document for listing For Managing Director
def permission_query_conditions(user):

    if not user:
        user = frappe.session.user

    
    roles = frappe.get_roles(user)

    states = get_merged_bid_workflow_states()

    not_show_states = []

    for state in states :
        only_visible_to = state["only_visible_to"]
        only_hide_to = state["only_hide_to"]

        if len(only_visible_to) > 0:
            if roles[0] not in only_visible_to:
                not_show_states.append(state["workflow_state_name"])

        if roles[0] in only_hide_to:
            not_show_states.append(state["workflow_state_name"])

    joined_list = f"('{ "','".join(not_show_states)}')"
    #frappe.msgprint(f"{joined_list}")

    return f"`tabBid Document`.workflow_state NOT IN {joined_list}"



class BidDocument(Document):

    def before_save(self):
        # Get the current value from the database before this save
        self._previous_workflow_state = frappe.db.get_value(self.doctype, self.name, "workflow_state")
        # Check if document is attached
        if self.attach_document:
            # Set UBO Upload Status to 1
            self.ubo_upload_status = 1
        else:
            self.ubo_upload_status = 0



        if self.link_to_corrigendum:
            # Set UBO Upload Status to 1
            self.corrigendum_uploaded = 1
        else:
            self.corrigendum_uploaded = 0

    def on_update(self):

        #frappe.msgprint(f"Bid Document {self.name}")

        pass


    def validate(self):
        pass     

