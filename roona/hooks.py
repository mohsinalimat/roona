from . import __version__ as app_version

app_name = "roona"
app_title = "Roona"
app_publisher = "Roona"
app_description = "Ecommerce Application"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "lovinmaxwell@gmail.com"
app_license = "MIT"
app_logo_url = '/assets/roona/images/logo.svg'

# website_context = {
# 	"favicon": 	"/assets/roona/images/cart.svg",
# 	"splash_image": "/assets/roona/images/cart.svg"
# }

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://erpnext.com?source=via_email_footer" target="_blank">
			Roona
		</a>
	</span>
"""
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/roona/css/whitelabel_app.css"
app_include_js = "/assets/roona/js/whitelabel.js"

# include js, css files in header of web template
web_include_css = "/assets/roona/css/whitelabel_web.css"
# web_include_js = "/assets/roona/js/roona.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "roona/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

website_context = {
	"favicon": "/assets/roona/images/favicon.svg",
	"splash_image": "/assets/roona/images/splash_image.svg"
}
# after_migrate = ['whitelabel.api.whitelabel_patch']

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "roona.utils.jinja_methods",
# 	"filters": "roona.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "roona.install.before_install"
# after_install = "roona.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "roona.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"roona.tasks.all"
# 	],
# 	"daily": [
# 		"roona.tasks.daily"
# 	],
# 	"hourly": [
# 		"roona.tasks.hourly"
# 	],
# 	"weekly": [
# 		"roona.tasks.weekly"
# 	],
# 	"monthly": [
# 		"roona.tasks.monthly"
# 	],
# }
# boot_session = "whitelabel.api.boot_session"
# Testing
# -------

# before_tests = "roona.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "roona.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "roona.task.get_dashboard_data"
# }

# override_whitelisted_methods = {
# 	"frappe.utils.change_log.show_update_popup": "whitelabel.api.ignore_update_popup"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"roona.auth.validate"
# ]

