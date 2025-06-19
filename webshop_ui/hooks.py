from . import __version__ as app_version

app_name = \"webshop_ui\"
app_title = \"Webshop UI\"
app_publisher = \"Your Company\"
app_description = \"Custom Frappe Webshop UI based on organic fruits and vegetables template\"
app_icon = \"octicon octicon-package\"
app_color = \"green\"
app_email = \"your@email.com\"
app_license = \"MIT\"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = \"/assets/webshop_ui/css/webshop_ui.css\"
# app_include_js = \"/assets/webshop_ui/js/webshop_ui.js\"

# include js, css files in header of web template
website_context = {
    \"favicon\": \"/assets/webshop_ui/images/favicon.ico\",
    \"splash_image\": \"/assets/webshop_ui/images/splash.png\"
}

# Website template overrides
# --------------------------
# Override webshop templates
website_template_overrides = [
    {
        \"path\": \"templates/includes/cart.html\",
        \"template\": \"webshop_ui/templates/includes/cart.html\"
    },
    {
        \"path\": \"templates/includes/navbar.html\", 
        \"template\": \"webshop_ui/templates/includes/navbar.html\"
    },
    {
        \"path\": \"templates/includes/footer.html\",
        \"template\": \"webshop_ui/templates/includes/footer.html\"
    }
]

# Custom CSS and JS for webshop
# ------------------------------
webform_include_css = [
    \"/assets/webshop_ui/css/organic-theme.css\"
]

webform_include_js = [
    \"/assets/webshop_ui/js/organic-theme.js\"
]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = \"login\"

# website user home page (by Role)
# role_home_page = {
#\t\"Customer\": \"/me\",
#\t\"Supplier\": \"/supplier\"
# }

# Website user home page (by function)
# get_website_user_home_page = \"webshop_ui.utils.get_home_page\"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = [\"Web Page\"]

# Installation
# ------------

# before_install = \"webshop_ui.install.before_install\"
# after_install = \"webshop_ui.install.after_install\"

# Uninstallation
# --------------

# before_uninstall = \"webshop_ui.uninstall.before_uninstall\"
# after_uninstall = \"webshop_ui.uninstall.after_uninstall\"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = \"webshop_ui.notifications.get_notification_config\"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# \t\"Event\": \"frappe.desk.doctype.event.event.get_permission_query_conditions\",
# }
#
# has_permission = {
# \t\"Event\": \"frappe.desk.doctype.event.event.has_permission\",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# \t\"ToDo\": \"custom_app.overrides.CustomToDo\"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# \t\"*\": {
# \t\t\"on_update\": \"method\",
# \t\t\"on_cancel\": \"method\",
# \t\t\"on_trash\": \"method\"
#\t}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# \t\"all\": [
# \t\t\"webshop_ui.tasks.all\"
# \t],
# \t\"daily\": [
# \t\t\"webshop_ui.tasks.daily\"
# \t],
# \t\"hourly\": [
# \t\t\"webshop_ui.tasks.hourly\"
# \t],
# \t\"weekly\": [
# \t\t\"webshop_ui.tasks.weekly\"
# \t]
# \t\"monthly\": [
# \t\t\"webshop_ui.tasks.monthly\"
# \t]
# }

# Testing
# -------

# before_tests = \"webshop_ui.install.before_tests\"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# \t\"frappe.desk.doctype.event.event.get_events\": \"webshop_ui.event.get_events\"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# \t\"Task\": \"webshop_ui.task.get_dashboard_data\"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = [\"Auto Repeat\"]


# User Data Protection
# --------------------

user_data_fields = [
    {
        \"doctype\": \"{doctype_1}\",
        \"filter_by\": \"{filter_by}\",
        \"redact_fields\": [\"{field_1}\", \"{field_2}\"],
        \"partial\": 1,
    },
    {
        \"doctype\": \"{doctype_2}\",
        \"filter_by\": \"{filter_by}\",
        \"partial\": 1,
    },
    {
        \"doctype\": \"{doctype_3}\",
        \"filter_by\": \"{filter_by}\",
        \"strict\": False,
    },
    {
        \"doctype\": \"{doctype_4}\"
    }
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# \t\"webshop_ui.auth.validate\"
# ]

# Translation
# --------------------------------

# Make property setters available across apps
# override_doctype_dashboards = {
# \t\"Item\": \"webshop_ui.overrides.item_dashboard\"
# }