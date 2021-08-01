import frappe
from frappe.utils import flt, cint
from frappe.client import get_list

@frappe.whitelist()
def area():
    # if page_length: limit_page_length = page_length
    # if limit: limit_page_length = limit
    # limit_page_length = cint(limit_page_length) if limit_page_length else None
    return frappe.db.sql("""
			SELECT area_name,pincode
			FROM `tabDelivery Area`	WHERE disabled = 0 GROUP BY 2""", as_dict=True)
    # return 0
    # return get_list("Item Group")
    # return get_list("Delivery Area")