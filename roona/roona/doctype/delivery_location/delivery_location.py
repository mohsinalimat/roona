# Copyright (c) 2021, Roona and contributors
# For license information, please see license.txt

# import frappe
from frappe.utils.nestedset import NestedSet
from frappe.utils import (strip)

class DeliveryLocation(NestedSet):
	def autoname(self):
		self.location_name = strip(self.location_name)
		self.name = self.location_name
