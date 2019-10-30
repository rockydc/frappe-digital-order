// Copyright (c) 2019, Kelompok 6 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Request Order', {
	// refresh: function(frm) {

	// }
	id_menu: function(frm){
		frm.doc.pesanan = []

		if(frm.doc.id_menu){
			frappe.call({
				method: "frappe.client.get",
				args: {
					doctype: ""
				}
			,})
		}
	}
});
