from __future__ import unicode_literals

import frappe
from erpnext.shopping_cart.product_info import get_product_info_for_website
from erpnext.portal.product_configurator.utils import get_conditions,get_product_settings
from frappe.utils import cint, fmt_money, flt, nowdate, getdate
from erpnext.accounts.doctype.pricing_rule.pricing_rule import get_pricing_rule_for_item
from erpnext.utilities.product import adjust_qty_for_expired_items, get_price, get_qty_in_stock, get_non_stock_item_status
from erpnext.shopping_cart.doctype.shopping_cart_settings.shopping_cart_settings \
	import get_shopping_cart_settings, show_quantity_in_website
from erpnext.shopping_cart.cart import _get_cart_quotation, _set_price_list


@frappe.whitelist(allow_guest=True)
def get_items(filters=None, search=None):
	start = frappe.form_dict.get('start', 0)
	products_settings = get_product_settings()
	page_length = 1000

	filters = filters or []
	# convert to list of filters
	if isinstance(filters, dict):
		filters = [['Item', fieldname, '=', value] for fieldname, value in filters.items()]

	enabled_items_filter = get_conditions({ 'disabled': 0 }, 'and')

	show_in_website_condition = ''
	if products_settings.hide_variants:
		show_in_website_condition = get_conditions({'show_in_website': 1 }, 'and')
	else:
		show_in_website_condition = get_conditions([
			['show_in_website', '=', 1],
			['show_variant_in_website', '=', 1]
		], 'or')

	search_condition = ''
	if search:
		# Default fields to search from
		default_fields = {'name', 'item_name', 'description', 'item_group'}

		# Get meta search fields
		meta = frappe.get_meta("Item")
		meta_fields = set(meta.get_search_fields())

		# Join the meta fields and default fields set
		search_fields = default_fields.union(meta_fields)
		try:
			if frappe.db.count('Item', cache=True) > 50000:
				search_fields.remove('description')
		except KeyError:
			pass

		# Build or filters for query
		search = '%{}%'.format(search)
		or_filters = [[field, 'like', search] for field in search_fields]

		search_condition = get_conditions(or_filters, 'or')

	filter_condition = get_conditions(filters, 'and')

	where_conditions = ' and '.join(
		[condition for condition in [enabled_items_filter, show_in_website_condition, \
			search_condition, filter_condition] if condition]
	)

	left_joins = []
	for f in filters:
		if len(f) == 4 and f[0] != 'Item':
			left_joins.append(f[0])

	left_join = ' '.join(['LEFT JOIN `tab{0}` on (`tab{0}`.parent = `tabItem`.name)'.format(l) for l in left_joins])

	results = frappe.db.sql('''
		SELECT
			`tabItem`.`name`, `tabItem`.`item_name`, `tabItem`.`item_code`,
			`tabItem`.`website_image`, `tabItem`.`image`,
			`tabItem`.`web_long_description`, `tabItem`.`description`,
			`tabItem`.`route`, `tabItem`.`item_group`
		FROM
			`tabItem`
		{left_join}
		WHERE
			{where_conditions}
		GROUP BY
			`tabItem`.`name`
		ORDER BY
			`tabItem`.`weightage` DESC
		LIMIT
			{page_length}
		OFFSET
			{start}
	'''.format(
			where_conditions=where_conditions,
			start=start,
			page_length=page_length,
			left_join=left_join
		)
	, as_dict=1)

	for r in results:
		r.description = r.web_long_description or r.description
		r.image = r.website_image or r.image
		product_info = get_product_info_for_website(r.item_code, skip_quotation_creation=True).get('product_info')
		if product_info:
			r.formatted_price = product_info['price'].get('formatted_price') if product_info['price'] else None
			r.stock = product_info['stock_qty'][0][0] if product_info['stock_qty'] else None

	return results

# get_product_info_for_website

# def get_price(item_code, price_list, customer_group, company, qty=1):
# 	template_item_code = frappe.db.get_value("Item", item_code, "variant_of")

# 	if price_list:
# 		price = frappe.get_all("Item Price", fields=["price_list_rate", "currency"],
# 			filters={"price_list": price_list, "item_code": item_code})

# 		if template_item_code and not price:
# 			price = frappe.get_all("Item Price", fields=["price_list_rate", "currency"],
# 				filters={"price_list": price_list, "item_code": template_item_code})

# 		if price:
# 			pricing_rule = get_pricing_rule_for_item(frappe._dict({
# 				"item_code": item_code,
# 				"qty": qty,
# 				"stock_qty": qty,
# 				"transaction_type": "selling",
# 				"price_list": price_list,
# 				"customer_group": customer_group,
# 				"company": company,
# 				"conversion_rate": 1,
# 				"for_shopping_cart": True,
# 				"currency": frappe.db.get_value("Price List", price_list, "currency")
# 			}))

# 			if pricing_rule:
# 				if pricing_rule.pricing_rule_for == "Discount Percentage":
# 					price[0].price_list_rate = flt(price[0].price_list_rate * (1.0 - (flt(pricing_rule.discount_percentage) / 100.0)))

# 				if pricing_rule.pricing_rule_for == "Rate":
# 					price[0].price_list_rate = pricing_rule.price_list_rate

# 			price_obj = price[0]
# 			if price_obj:
# 				price_obj["formatted_price"] = fmt_money(price_obj["price_list_rate"], currency=price_obj["currency"])

# 				price_obj["currency_symbol"] = not cint(frappe.db.get_default("hide_currency_symbol")) \
# 					and (frappe.db.get_value("Currency", price_obj.currency, "symbol", cache=True) or price_obj.currency) \
# 					or ""

# 				uom_conversion_factor = frappe.db.sql("""select	C.conversion_factor
# 					from `tabUOM Conversion Detail` C
# 					inner join `tabItem` I on C.parent = I.name and C.uom = I.sales_uom
# 					where I.name = %s""", item_code)

# 				uom_conversion_factor = uom_conversion_factor[0][0] if uom_conversion_factor else 1
# 				price_obj["formatted_price_sales_uom"] = fmt_money(price_obj["price_list_rate"] * uom_conversion_factor, currency=price_obj["currency"])

# 				if not price_obj["price_list_rate"]:
# 					price_obj["price_list_rate"] = 0

# 				if not price_obj["currency"]:
# 					price_obj["currency"] = ""

# 				if not price_obj["formatted_price"]:
# 					price_obj["formatted_price"] = ""

# 			return price_obj

# def get_product_info_for_website(item_code, skip_quotation_creation=False):
# 	"""get product price / stock info for website"""

# 	cart_settings = get_shopping_cart_settings()
# 	if not cart_settings.enabled:
# 		return frappe._dict()

# 	cart_quotation = frappe._dict()

# 	selling_price_list = cart_quotation.get("selling_price_list") if cart_quotation else _set_price_list(cart_settings, None)

# 	price = get_price(
# 		item_code,
# 		selling_price_list,
# 		cart_settings.default_customer_group,
# 		cart_settings.company
# 	)

# 	stock_status = get_qty_in_stock(item_code, "website_warehouse")

# 	product_info = {
# 		"price": price,
# 		"stock_qty": stock_status.stock_qty,
# 		"in_stock": stock_status.in_stock if stock_status.is_stock_item else get_non_stock_item_status(item_code, "website_warehouse"),
# 		"qty": 0,
# 		"uom": frappe.db.get_value("Item", item_code, "stock_uom"),
# 		"show_stock_qty": show_quantity_in_website(),
# 		"sales_uom": frappe.db.get_value("Item", item_code, "sales_uom")
# 	}

# 	if product_info["price"]:
# 		if frappe.session.user != "Guest":
# 			item = cart_quotation.get({"item_code": item_code}) if cart_quotation else None
# 			if item:
# 				product_info["qty"] = item[0].qty

# 	return frappe._dict({
# 		"product_info": product_info,
# 		"cart_settings": cart_settings
# 	})

# def get_qty_in_stock(item_code, warehouse=None):
# 	in_stock, stock_qty = 0, ''
# 	template_item_code, is_stock_item = frappe.db.get_value("Item", item_code, ["variant_of", "is_stock_item"])

# 	if warehouse:
# 		stock_qty = frappe.db.sql("""
# 			select GREATEST(S.actual_qty - S.reserved_qty - S.reserved_qty_for_production - S.reserved_qty_for_sub_contract, 0) / IFNULL(C.conversion_factor, 1)
# 			from tabBin S
# 			inner join `tabItem` I on S.item_code = I.Item_code
# 			left join `tabUOM Conversion Detail` C on I.sales_uom = C.uom and C.parent = I.Item_code
# 			where S.item_code=%s and S.warehouse=%s""", (item_code, warehouse))

# 		if stock_qty:
# 			stock_qty = adjust_qty_for_expired_items(item_code, stock_qty, warehouse)
# 			in_stock = stock_qty[0][0] > 0 and 1 or 0

# 	return frappe._dict({"in_stock": in_stock, "stock_qty": stock_qty, "is_stock_item": is_stock_item})
