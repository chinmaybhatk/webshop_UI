from . import __version__ as app_version

app_name = "webshop_ui"
app_title = "Webshop UI"
app_publisher = "Your Company"
app_description = "Custom Frappe Webshop UI based on organic fruits and vegetables template"
app_icon = "octicon octicon-package"
app_color = "green"
app_email = "your@email.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of web template
website_context = {
    "favicon": "/assets/webshop_ui/images/favicon.ico",
    "splash_image": "/assets/webshop_ui/images/splash.png"
}

# Website Assets
# --------------
# These will be included in the website automatically
web_include_css = [
    "/assets/webshop_ui/css/organic-theme.css"
]

web_include_js = [
    "/assets/webshop_ui/js/organic-theme.js"
]

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "home"

# Website route rules
# -------------------
website_route_rules = [
    {"from_route": "/", "to_route": "home"},
]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "webshop_ui.install.before_install"
# after_install = "webshop_ui.install.after_install"

# Uninstallation
# --------------

# before_uninstall = "webshop_ui.uninstall.before_uninstall"
# after_uninstall = "webshop_ui.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "webshop_ui.notifications.get_notification_config"

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
# 		"webshop_ui.tasks.all"
# 	],
# 	"daily": [
# 		"webshop_ui.tasks.daily"
# 	],
# 	"hourly": [
# 		"webshop_ui.tasks.hourly"
# 	],
# 	"weekly": [
# 		"webshop_ui.tasks.weekly"
# 	]
# 	"monthly": [
# 		"webshop_ui.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "webshop_ui.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "webshop_ui.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "webshop_ui.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# User Data Protection
# --------------------

# user_data_fields = [
#     {
#         "doctype": "{doctype_1}",
#         "filter_by": "{filter_by}",
#         "redact_fields": ["{field_1}", "{field_2}"],
#         "partial": 1,
#     },
#     {
#         "doctype": "{doctype_2}",
#         "filter_by": "{filter_by}",
#         "partial": 1,
#     },
#     {
#         "doctype": "{doctype_3}",
#         "filter_by": "{filter_by}",
#         "strict": False,
#     },
#     {
#         "doctype": "{doctype_4}"
#     }
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"webshop_ui.auth.validate"
# ]
