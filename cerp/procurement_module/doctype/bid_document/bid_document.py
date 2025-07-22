# Copyright (c) 2025, inxeoz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BidDocument(Document):
    def validate(self):
        role_counts = {}
        for row in self.committee_member:
            role = row.role_in_committee
            if role:
                role_counts[role] = role_counts.get(role, 0) + 1

        if role_counts.get("Chairman", 0) > 1:
            frappe.throw("Only one 'Chairman' is allowed in the committee.")
