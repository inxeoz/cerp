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

    def on_update(self):

        frappe.msgprint(f"Bid Document {self.name}")

        return
        def first_upper(text):

            str_arr = text.split(" ")
            print(str_arr)
            upper_str = ""
            for token in str_arr:
            
                if token.isupper():
                    print(token)
                    upper_str += " "+token
                else:
                    break
            return upper_str.strip()

        # ① Check if workflow_state is 'Rejected' when document is updated

        if self.workflow_state == "Rejected":
            # ② Get current user's roles
            user_roles = frappe.get_roles(frappe.session.user)
    
            state = first_upper ( self._previous_workflow_state )

            if user_roles:
                # ③ Set status stating who rejected (using role, single string or multiple)
                self.db_set("bid_document_status", f"{state} Rejected by {user_roles[0]}")
                # ⚠️ Use db_set() to avoid recursion and ensure immediate DB write

    def validate(self):
        role_counts = {}
        for row in self.committee_member_table:
            role = row.role_in_committee
            if role:
                role_counts[role] = role_counts.get(role, 0) + 1

        if role_counts.get("Chairman", 0) > 1:
            frappe.throw("Only one 'Chairman' is allowed in the committee.")



# # Copyright (c) 2025, inxeoz and contributors
# # For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class BidDocument(Document):

#     def on_update(self):
#         # ① Check if workflow_state is 'Rejected' when document is updated
#         if self.workflow_state == "Rejected":
#             # ② Get current user's roles
#             user_roles = frappe.get_roles(frappe.session.user)

#             if user_roles:
#                 # ③ Set status stating who rejected (using role, single string or multiple)
#                 self.db_set("bid_document_status", f"Rejected by {user_roles[0]}")
#                 # ⚠️ Use db_set() to avoid recursion and ensure immediate DB write

#     def validate(self):
#         # ① Count committee member roles to prevent multiple Chairmen
#         role_counts = {}
#         for row in self.committee_member:
#             role = row.role_in_committee
#             if role:
#                 role_counts[role] = role_counts.get(role, 0) + 1

#         if role_counts.get("Chairman", 0) > 1:
#             frappe.throw("Only one 'Chairman' is allowed in the committee.")

#         # ② Set bid status to reflect current role — optional if workflow state is not 'Rejected
