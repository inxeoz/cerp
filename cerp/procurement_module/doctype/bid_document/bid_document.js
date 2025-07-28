// // Copyright (c) 2025, inxeoz and contributors
// // For license information, please see license.txt

frappe.ui.form.on('MOM TABLE', {
    
    // meeting id function
    meeting_id: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        
        if (row.meeting_id) {
            frappe.call({
                method: 'frappe.client.get_value',
                args: {
                    doctype: 'Minutes of Meeting',
                    filters: { name: row.meeting_id },
                    fieldname: ['agenda', 'type_of_meeting']
                },
                callback: function(r) {
                    if (r.message) {
                        // Set values in the row
                        frappe.model.set_value(cdt, cdn, {
                            'agenda': r.message.agenda || '',
                            'type_of_meeting': r.message.type_of_meeting || ''
                        });
                    }
                }
            });
        } else {
            // Clear fields
            frappe.model.set_value(cdt, cdn, {
                'agenda': '',
                'type_of_meeting': ''
            });
        }
    },
    
    // Trigger when a new row is added
    tec_mom_add: function(frm, cdt, cdn) {
        // Clear fields for new row
        let row = locals[cdt][cdn];
        row.agenda = '';
        row.type_of_meeting = '';
    }
});

frappe.ui.form.on("Bid Document", {

    onload: function(frm) {
        // Fetch data for existing rows when form loads
        if (frm.doc.tec_mom) {
            frm.doc.tec_mom.forEach(function(row) {
                if (row.meeting_id && (!row.agenda || !row.type_of_meeting)) {
                    // Trigger the meeting_id function for each row
                    frm.trigger('meeting_id', row.doctype, row.name);
                }
            });
        }
    },

    refresh(frm) {
   
        user =frappe.session.user
        user_roles = frappe.user_roles

        // want to hide some sections
    

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



// frappe.ui.form.on('MOM TABLE', {
//     meeting_id: function(frm, cdt, cdn) {
//         let row = locals[cdt][cdn];
        
//         if (row.meeting_id) {
//             // Fetch full document
//             frappe.call({
//                 method: 'frappe.client.get',
//                 args: {
//                     doctype: 'Minutes of Meeting',
//                     name: row.meeting_id
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         let mom = r.message;
                        
//                         // Display fetched data
//                         frappe.msgprint(`
//                             <h4>Fetched MOM Details:</h4>
//                             <table class="table table-bordered">
//                                 <tr>
//                                     <td><b>Meeting ID</b></td>
//                                     <td>${mom.name}</td>
//                                 </tr>
//                                 <tr>
//                                     <td><b>Agenda</b></td>
//                                     <td>${mom.agenda || '<i>No agenda set</i>'}</td>
//                                 </tr>
//                                 <tr>
//                                     <td><b>Type of Meeting</b></td>
//                                     <td>${mom.type_of_meeting || '<i>No type set</i>'}</td>
//                                 </tr>
//                             </table>
//                         `);
//                     }
//                 },
//                 error: function(err) {
//                     frappe.msgprint({
//                         title: 'Error',
//                         message: 'Could not fetch MOM details',
//                         indicator: 'red'
//                     });
//                 }
//             });
//         }
//     }
// });
