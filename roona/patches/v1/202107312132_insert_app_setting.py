import frappe
from roona.utils.install import add_standard_app_setting_items

def execute():
	# Add standard navbar items for ERPNext in Navbar Settings
	frappe.reload_doc('roona', 'doctype', 'roona_app_setting')
	frappe.reload_doc('roona', 'doctype', 'roona_app_item')
	add_standard_app_setting_items()