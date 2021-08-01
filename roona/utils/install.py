import frappe

def add_standard_app_setting_items():
	app_settings = frappe.get_single("Roona App Setting")

	app_setting_items = [
		{
			'item_name': 'Max Days Available Delivery',
			'item_key': 'MAX_DELIVERY_DAY',
			'item_value': '_',
		},
		{
			'item_name': 'Delivery Charge',
			'item_key': 'DELIVERY_CHARGE',
			'item_value': '_',
		},
		{
			'item_name': 'Free delivery only after cart value',
			'item_key': 'FREE_DELIVERY_AFTER',
			'item_value': '_',
		},
		{
			'item_name': 'Total Cart Valid Amount',
			'item_key': 'CART_VALID_AFTER',
			'item_value': '_',
		},
		{
			'item_name': 'Contact Us',
			'item_key': 'CONTACT_US',
			'item_value': '_',
		},
		{
			'item_name': 'Currency',
			'item_key': 'CURRENCY',
			'item_value': '₹',
		},
		{
			'item_name': 'Currency Code',
			'item_key': 'CURRENCY_CODE',
			'item_value': 'INR',
		},
		{
			'item_name': 'Cancellation timing',
			'item_key': 'DURATION_FOR_CANCELLATION',
			'item_value': '_',
		},
		{
			'item_name': 'Max Amount FOR COD',
			'item_key': 'MAXIMUM_AMOUNT_COD',
			'item_value': '_',
		},
		{
			'item_name': '	On Hold Order Will Be Cancelled In (MIN)',
			'item_key': 'HOLD_ORDER_CANCELED_IN',
			'item_value': '_',
		},
		{
			'item_name': 'Customer Support Mail',
			'item_key': 'SUPPORT_MAIL',
			'item_value': '_',
		},
		{
			'item_name': 'Customer Support Call',
			'item_key': 'SUPPORT_CALL',
			'item_value': '_',
		},
		{
			'item_name': 'Customer Whatapp Support',
			'item_key': 'SUPPORT_WHATSAPP_CALL',
			'item_value': '_',
		},
		{
			'item_name': 'About Us App Text',
			'item_key': 'APP_ABOUT_US_TEXT',
			'item_value': '_',
		},
		{
			'item_name': 'Facebook',
			'item_key': 'SOCIAL_FACEBOOK_LINK',
			'item_value': 'https://www.facebook.com',
		},
		{
			'item_name': 'Twitter',
			'item_key': 'SOCIAL_TWITTER_LINK',
			'item_value': 'https://twitter.com',
		},
		{
			'item_name': 'Instagram',
			'item_key': 'SOCIAL_INSTAGRAM_LINK',
			'item_value': 'https://www.instagram.com',
		},
		{
			'item_name': 'Pinterest',
			'item_key': 'SOCIAL_PINTEREST_LINK',
			'item_value': 'http://pinterest.com',
		},
		{
			'item_name': 'Youtube',
			'item_key': 'SOCIAL_YOUTUBE_LINK',
			'item_value': 'http://youtube.com',
		},
		{
			'item_name': 'iOS Apple Store Link',
			'item_key': 'IOS_APP_LINK',
			'item_value': '_',
		},
		{
			'item_name': 'Android Play Store Link',
			'item_key': 'ANDROID_APP_LINK',
			'item_value': '_',
		},
	]

	app_settings.app_settings = []

	for item in app_setting_items:
		app_settings.append('app_settings', item)

	app_settings.save()

# def install_basic_docs():
# 	# core users / roles
# 	install_docs = [
# 		{'doctype': "Role", "role_name": "Roona Customer", "desk_access" : 0},
# 		{'doctype': "Role", "role_name": "Translator"},
# 		{'doctype': "Workflow State", "workflow_state_name": "Pending",
# 			"icon": "question-sign", "style": ""},
# 		{'doctype': "Workflow State", "workflow_state_name": "Approved",
# 			"icon": "ok-sign", "style": "Success"},
# 		{'doctype': "Workflow State", "workflow_state_name": "Rejected",
# 			"icon": "remove", "style": "Danger"},
# 		{'doctype': "Workflow Action Master", "workflow_action_name": "Approve"},
# 		{'doctype': "Workflow Action Master", "workflow_action_name": "Reject"},
# 		{'doctype': "Workflow Action Master", "workflow_action_name": "Review"},
# 		{'doctype': "Email Domain", "domain_name":"example.com", "email_id": "account@example.com", "password": "pass", "email_server": "imap.example.com","use_imap": 1, "smtp_server": "smtp.example.com"},
# 		{'doctype': "Email Account", "domain":"example.com", "email_id": "notifications@example.com", "default_outgoing": 1},
# 		{'doctype': "Email Account", "domain":"example.com", "email_id": "replies@example.com", "default_incoming": 1}
# 	]

# 	for d in install_docs:
# 		try:
# 			frappe.get_doc(d).insert()
# 		except frappe.NameError:
# 			pass

def update_customer_access():
	frappe.db.sql(" update `tabRole` set desk_access = 0 where name = 'Customer'")
	add_permissions()

def add_permissions():
	from frappe.permissions import add_permission, update_permission_property
	for doctype in ('Sales Invoice', 'Sales Order'):
		add_permission(doctype, 'All', 0)
		role = 'Customer'
		add_permission(doctype, role, 0)
		update_permission_property(doctype, role, 0, 'if_owner',1)
		update_permission_property(doctype, role, 0, 'select',1)
		update_permission_property(doctype, role, 0, 'read',1)
		update_permission_property(doctype, role, 0, 'write',1)
		update_permission_property(doctype, role, 0, 'create',1)
		update_permission_property(doctype, role, 0, 'submit',1)
		update_permission_property(doctype, role, 0, 'export',1)
		update_permission_property(doctype, role, 0, 'print',1)
		update_permission_property(doctype, role, 0, 'email',1)
		update_permission_property(doctype, role, 0, 'permlevel',0)
		update_permission_property(doctype, role, 0, 'delete',0)
		update_permission_property(doctype, role, 0, 'cancel',0)
		update_permission_property(doctype, role, 0, 'amend',0)
		update_permission_property(doctype, role, 0, 'report',0)
		update_permission_property(doctype, role, 0, 'import',0)
		update_permission_property(doctype, role, 0, 'set_user_permissions',0)
		update_permission_property(doctype, role, 0, 'share',0)