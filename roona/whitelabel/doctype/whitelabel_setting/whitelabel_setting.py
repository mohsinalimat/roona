# Copyright (c) 2021, Roona and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class WhitelabelSetting(Document):
	def validate(self):
		# if cint(get_frappe_version()) >= 13:
			if self.whitelabel_app_name:
				frappe.db.set_value("System Settings","System Settings","app_name",self.whitelabel_app_name)
			# else:
			# 	if "erpnext" in frappe.get_installed_apps():
			# 		frappe.db.set_value("System Settings","System Settings","app_name","ERPNext")
			# 	else:
			# 		frappe.db.set_value("System Settings","System Settings","app_name","Frappe")

