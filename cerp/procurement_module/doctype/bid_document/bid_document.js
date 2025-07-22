// // Copyright (c) 2025, inxeoz and contributors
// // For license information, please see license.txt

// // frappe.ui.form.on("Bid Document", {
// // 	refresh(frm) {

// // 	},
// // });

// frappe.ui.form.on('Bid Document', {
//     // refresh: function(frm) {
//     //}

//      validate: function(frm) {

        
//         let role_counts = {};

//         // Iterate all rows in the child table 'committee_member_table'
//         frm.doc.committee_member.forEach(row => {
//             let role = row.role_in_committee;  // Use the exact fieldname (case-sensitive)
//             if (role) {
//                 // Count occurrences
//                 if (role_counts[role]) {
//                     role_counts[role] += 1;
//                 } else {
//                     role_counts[role] = 1;
//                 }
//             }
//         });

        
//           // If more than one Chairman, prevent saving
//         if (role_counts["Chairman"] > 1) {
//             frappe.throw("Chairman can't be selected more than once.");
//         }

//         // Show message if dictionary is not empty
//         if (Object.keys(role_counts).length > 0) {
//             let msg = JSON.stringify(role_counts, null, 2); // Pretty print JSON
//             // frappe.msgprint({
//             //     title: 'Role Counts in Committee',
//             //     message: `<pre>${msg}</pre>`,
//             //     indicator: 'green'
//             // });
//         }
//     }
// });
