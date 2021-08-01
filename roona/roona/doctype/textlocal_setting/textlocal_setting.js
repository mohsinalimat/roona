// Copyright (c) 2021, Roona and contributors
// For license information, please see license.txt

frappe.ui.form.on('Textlocal Setting', {
	refresh: function(frm) {
		// frappe.call({
		// 	method:"frappe.client.get_value",
		// 	async:false,
		// 	args:{
		// 		doctype:'SMS Sender',
		// 		filters:{
		// 			sender:cur_frm.doc.sender
		// 		},
		// 		fieldname:['sender']
		// 	},callback:function(r){
		// 		console.log(r.message)
		// 		if(r.message != undefined){
		// 			cur_frm.set_value('sender',r.message.sender)
		// 			cur_frm.refresh_fields('sender')
		// 		}
		// 	}
		// });

		// filterChildFields(frm,'senders','sender','sender','default_sender');
	}
});

function filterChildFields(frm, tableName, fieldTrigger, fieldName, fieldFiltered) {
    frm.fields_dict[tableName].grid.get_field(fieldFiltered).get_query = function(doc, cdt, cdn) {
        var child = locals[cdt][cdn];
        return {    
            filters:[
                [fieldName, '=', child[fieldTrigger]]
            ]
        }
    }
}

