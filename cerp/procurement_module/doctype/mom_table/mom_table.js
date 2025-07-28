// frappe.ui.form.on('MOM TABLE', {
//     meeting_id: function(frm, cdt, cdn) {
//         // Get the current row
//         let row = locals[cdt][cdn];
        
//         if (row.meeting_id) {
//             // Fetch data from Minutes of Meeting
//             frappe.call({
//                 method: 'frappe.client.get_value',
//                 args: {
//                     doctype: 'Minutes of Meeting',
//                     filters: { name: row.meeting_id },
//                     fieldname: ['agenda', 'type_of_meeting']
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         // Set the values in the child table row
//                         frappe.model.set_value(cdt, cdn, 'agenda', r.message.agenda || '');
//                         frappe.model.set_value(cdt, cdn, 'type_of_meeting', r.message.type_of_meeting || '');
                        
//                         // Refresh the child table
//                         frm.refresh_field('tec_mom');
//                     }
//                 }
//             });
//         } else {
//             // Clear fields if meeting_id is removed
//             frappe.model.set_value(cdt, cdn, 'agenda', '');
//             frappe.model.set_value(cdt, cdn, 'type_of_meeting', '');
//             frm.refresh_field('tec_mom');
//         }
//     }
// });