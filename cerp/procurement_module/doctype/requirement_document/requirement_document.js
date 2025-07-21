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

frappe.ui.form.on("Requirement Document", {
    refresh(frm) {
        if (frm.doc.workflow_state === "Approved by MD Sir") {
            frm.add_custom_button("Create Bid Form", function() {
                // Your logic to create bid form goes here
                
                  frappe.new_doc("Bid Creation Form", {
                    // Replace 'requirement' with actual fieldname in Bid Form
                    requirements: frm.doc.name
                });
            });
        }
    }
});
