// // Copyright (c) 2025, inxeoz and contributors
// // For license information, please see license.txt

// Helper functions
const removeRowFromTable = (frm, tableName, cdn) => {
    frm.doc[tableName] = frm.doc[tableName].filter(item => item.name !== cdn);
    frm.refresh_field(tableName);
};

const checkDuplicate = (table, field, value, currentCdn) => {
    return table.some(item => item.name !== currentCdn && item[field] === value);
};

const clearFields = (cdt, cdn, fields) => {
    const clearData = {};
    fields.forEach(field => clearData[field] = '');
    frappe.model.set_value(cdt, cdn, clearData);
};

frappe.ui.form.on('MOM TABLE', {
    meeting_id: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        
        if (!row.meeting_id) {
            clearFields(cdt, cdn, ['agenda', 'type_of_meeting']);
            return;
        }
        
        // Check for duplicates
        if (checkDuplicate(frm.doc.mom_table, 'meeting_id', row.meeting_id, cdn)) {
            frappe.msgprint(__('This Meeting ID is already selected'));
            removeRowFromTable(frm, 'mom_table', cdn);
            return;
        }
        
        // Fetch meeting details
        frappe.call({
            method: 'frappe.client.get_value',
            args: {
                doctype: 'Minutes of Meeting',
                filters: { name: row.meeting_id },
                fieldname: ['agenda', 'type_of_meeting']
            },
            callback: function(r) {
                if (r.message) {
                    frappe.model.set_value(cdt, cdn, {
                        'agenda': r.message.agenda || '',
                        'type_of_meeting': r.message.type_of_meeting || ''
                    });
                }
            }
        });
    },
    
    mom_table_add: function(frm, cdt, cdn) {
        clearFields(cdt, cdn, ['agenda', 'type_of_meeting']);
    }
});

frappe.ui.form.on('Committee Member Table', {
    member_id: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        
        if (!row.member_id) {
            clearFields(cdt, cdn, ['member_name', 'designation', 'role_in_committee']);
            return;
        }
        
        // Check for duplicates
        if (checkDuplicate(frm.doc.committee_member_table, 'member_id', row.member_id, cdn)) {
            frappe.msgprint(__('This Member is already in the committee'));
            removeRowFromTable(frm, 'committee_member_table', cdn);
            return;
        }
        
        // Fetch member details
        frappe.call({
            method: 'frappe.client.get_value',
            args: {
                doctype: 'Member',
                filters: { name: row.member_id },
                fieldname: ['member_name', 'designation', 'role_in_committee']
            },
            callback: function(r) {
                if (!r.message) return;
                
                // Check for Chairman role
                if (r.message.role_in_committee === "Chairman") {
                    const hasChairman = frm.doc.committee_member_table.some(
                        item => item.name !== cdn && item.role_in_committee === "Chairman"
                    );
                    
                    if (hasChairman) {
                        frappe.msgprint(__("Only One Chairman allowed"));
                        removeRowFromTable(frm, 'committee_member_table', cdn);
                        return;
                    }
                }
                
                // Set values in the row
                frappe.model.set_value(cdt, cdn, {
                    'member_name': r.message.member_name || '',
                    'designation': r.message.designation || '',
                    'role_in_committee': r.message.role_in_committee || '',
                });
            }
        });
    },
    
    committee_member_table_add: function(frm, cdt, cdn) {
        clearFields(cdt, cdn, ['member_name', 'designation', 'role_in_committee']);
    },
    
    committee_member_table_remove: function(frm) {
        frm.refresh_field('committee_member_table');
    }
});

frappe.ui.form.on("Bid Document", {
    onload: function(frm) {
        // Fetch data for existing MOM table rows
        if (frm.doc.mom_table) {
            frm.doc.mom_table.forEach(row => {
                if (row.meeting_id && (!row.agenda || !row.type_of_meeting)) {
                    frm.trigger('meeting_id', row.doctype, row.name);
                }
            });
        }

        // Fetch data for existing committee member table rows
        if (frm.doc.committee_member_table) {
            frm.doc.committee_member_table.forEach(row => {
                if (row.member_id && (!row.member_name || !row.designation)) {
                    frm.trigger('member_id', row.doctype, row.name);
                }
            });
        }
    },

    refresh: function(frm) {
        const user_roles = frappe.user_roles;
        
        if (frm.doc.workflow_state === "Rejected" && user_roles.includes('Procurement Officer')) {
            frm.add_custom_button("Use as Template", function() {
                const template_fields = {
                    bid_title: frm.doc.bid_title,
                    description__scope_of_work: frm.doc.description__scope_of_work,
                    bid_type: frm.doc.bid_type,
                    submission_start: frm.doc.submission_start,
                    submission_end: frm.doc.submission_end
                };
                
                frappe.new_doc("Bid Document", template_fields);
            });
        }
    }
});