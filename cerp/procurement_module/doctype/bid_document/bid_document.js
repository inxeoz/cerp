// // Copyright (c) 2025, inxeoz and contributors
// // For license information, please see license.txt

// // frappe.ui.form.on("Bid Document", {
// // 	refresh(frm) {

// // 	},
// // });


// function action_option_to_upload_pending(frm) {
//     user_roles = frappe.user_roles

//     if (user_roles.includes('Managing Director')) {
//         if (frm.doc.bcc_upload_status == 1) {

//             // add a normal menu item
//             page.add_action_item('Delete', () => delete_items())

//         }
//     }
// }


// function next_state(frm) {
//    console.log('Doc Status:', frm.doc.workflow_state);
//    console.log('Role[0]', frappe.user_roles[0])
// }

// function first_upper(text) {

//     let str_arr = text.split(" ");
//     console.log(str_arr)
//     let upper_str = "";

//     for (const str of str_arr) {
//         if (str === str.toUpperCase()) {
//             console.log(str)
//             upper_str += " "+str;
//         }else{
//           break;
//         }
//     }

//     return upper_str.trim();

// }



frappe.ui.form.on("Bid Document", {
    refresh(frm) {
   
        user =frappe.session.user
        user_roles = frappe.user_roles

        if (frm.doc.workflow_state === "Rejected" && user_roles.includes('Procurement Officer') ) {
            frm.add_custom_button("Use as Template", function() {
                // Your logic to create bid form goes here

                   let fields = [
                    // "bid_document_status",
                    "bid_title",
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