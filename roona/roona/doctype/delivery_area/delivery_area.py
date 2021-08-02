# Copyright (c) 2021, Roona and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import (strip)

class DeliveryArea(Document):
	def autoname(self):
		self.area_name = strip(self.area_name)
		self.name = self.area_name

