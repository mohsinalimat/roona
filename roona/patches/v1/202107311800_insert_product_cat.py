import frappe

def execute():
	frappe.reload_doctype("Item Group")
	insert_product_cat()

def insert_product_cat():
    frappe.db.sql(" update `tabItem Group` set is_group = 1 where name = 'Products'")
	# roona Product Catogery / Item Group
    insert_item_group = [
		{'doctype':'Item Group', 'name':'Vegetables', 'item_group_name':'Vegetables', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 1, 'disabled' : 0},
		{'doctype':'Item Group', 'name':'Fruits', 'item_group_name':'Fruits', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 2, 'disabled' : 0},
		{'doctype':'Item Group', 'name':'Fish & Seafoods', 'item_group_name':'Fish & Seafoods', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 3, 'disabled' : 0},
		{'doctype':'Item Group', 'name':'Fresh Water Fish', 'item_group_name':'Fresh Water Fish', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 4, 'disabled' : 0},
		{'doctype':'Item Group', 'name':'Prawns & Crabs', 'item_group_name':'Prawns & Crabs', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 5, 'disabled' : 0},
		{'doctype':'Item Group', 'name':'Poultry & Eggs', 'item_group_name':'Poultry & Eggs', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 6, 'disabled' : 0},
		{'doctype':'Item Group', 'name':'Goat & Lamb', 'item_group_name':'Goat & Lamb', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 7, 'disabled' : 0},
		{'doctype':'Item Group', 'name':'Eggs', 'item_group_name':'Eggs', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 8, 'disabled' : 1},
		{'doctype':'Item Group', 'name':'Pickles', 'item_group_name':'Pickles', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 9, 'disabled' : 1},
		{'doctype':'Item Group', 'name':'Cold Cuts', 'item_group_name':'Cold Cuts', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 10, 'disabled' : 1},
		{'doctype':'Item Group', 'name':'Frozen', 'item_group_name':'Frozen', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 11, 'disabled' : 1},
		{'doctype':'Item Group', 'name':'Ready to Cook', 'item_group_name':'Ready to Cook', 'parent_item_group':'Products', 'old_parent':'Products' , 'weightage' : 12, 'disabled' : 1},
	]
    
    for d in insert_item_group:
        try:
            frappe.get_doc(d).insert()    
        except frappe.NameError:
            pass