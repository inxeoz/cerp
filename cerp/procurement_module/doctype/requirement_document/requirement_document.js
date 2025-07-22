// Copyright (c) 2025, inxeoz and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Requirement Document", {
// 	refresh(frm) {

// 	},
// });


// frappe.ui.form.on('Requirement Document', {
// 	refresh(frm) {
// 		// your code here
// 	}
// })


/// in client side use non-critical features and there implementation

frappe.ui.form.on("Requirement Document", {
    refresh(frm) {

        user =frappe.session.user

        console.log(user)

        user_roles = frappe.user_roles

       

        if (frm.doc.workflow_state === "Approved by MD Sir" && user_roles.includes('Procurement Officer') ) {
            frm.add_custom_button("Create Bid Document", function() {
                // Your logic to create bid form goes here
                
                  frappe.new_doc("Bid Document", {
                    // Replace 'requirement' with actual fieldname in Bid Form
                    requirement_document_reference: frm.doc.name,
                    bid_title: frm.doc.requirement_title,
                    description__scope_of_work: frm.doc.description__scope

                });
            });
        }

        if (frm.doc.workflow_state === "Rejected" && user_roles.includes('Procurement Officer') ) {
            frm.add_custom_button("Use as Template", function() {
                // Your logic to create bid form goes here
                  frappe.new_doc("Requirement Document", {
                    // Replace 'requirement' with actual fieldname in Bid Form
                    name: frm.doc.name,
                    requirement_title: frm.doc.requirement_title,
                    description__scope: frm.doc.description__scope,
                    department: frm.doc.department,
                    estimated_budget: frm.doc.estimated_budget,
                    date_of_creation: frm.doc.date_of_creation

                });
            });
        }


    }
});


