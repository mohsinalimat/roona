import frappe
from frappe import _

@frappe.whitelist()
def set_app_name(app_name):
	frappe.reload_doctype("System Settings")
	settings = frappe.get_doc("System Settings")
	settings.db_set("app_name", app_name, commit=True)
	return """success"""
