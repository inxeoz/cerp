// // Copyright (c) 2025, inxeoz and contributors
// // For license information, please see license.txt

// // frappe.ui.form.on("Bid Document", {
// // 	refresh(frm) {

// // 	},
// // });




frappe.ui.form.on("Bid Document", {
    refresh(frm) {

        user =frappe.session.user

        console.log(user)

        user_roles = frappe.user_roles

        if (frm.doc.workflow_state === "Rejected" && user_roles.includes('Procurement Officer') ) {
            frm.add_custom_button("Use as Template", function() {
                // Your logic to create bid form goes here

                   let fields = [
                    // "bid_document_status",
                    "bid_title",
                    "requirement_document_reference",
                    "description__scope_of_work",
                    "bid_type",
                    "submission_start",
                    "submission_end"
                ];
                 // Create a data object for new_doc fields
                let field_data = {};
                fields.forEach(field => {
                    field_data[field] = frm.doc[field];
                });

                // Create the new document with these field values
                frappe.new_doc("Bid Document", field_data);
                
            });
        }

    }
});