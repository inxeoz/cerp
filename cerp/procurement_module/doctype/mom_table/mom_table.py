# Copyright (c) 2025, inxeoz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class MOMTABLE(Document):
    def validate(self):
        """
        Automatically fetch data from MOM document when this child table is used
        """
        self.fetch_mom_details()
    
    def fetch_mom_details(self):
        """
        Fetch details from the linked MOM document
        """
        # Check if there's a MOM reference field in the child table
        if hasattr(self, 'meeting_id') and self.mom_reference:
            try:
                # Fetch MOM document details
                mom_doc = frappe.get_doc("MOM", self.mom_reference)
                
                # Auto-populate fields from MOM document
                # Example fields - adjust according to your actual field names
                if hasattr(mom_doc, 'type_of_meeting'):
                    self.type_of_meeting = mom_doc.type_of_meeting
                # Add more fields as needed
                
            except frappe.DoesNotExistError:
                frappe.msgprint(_("Selected MOM document does not exist"))
            except Exception as e:
                frappe.log_error(f"Error fetching MOM details: {str(e)}")