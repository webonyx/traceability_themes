# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "traceability_themes"
app_title = "Traceability Themes"
app_publisher = "Webonyx"
app_description = "Themes for ERPNext Traceability app"
app_icon = "octicon octicon-globe"
app_color = "blue"
app_email = "viet@webonyx.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/css/dark-theme.min.css"
app_include_js = "/assets/js/traceability_themes.min.js"

# Installation
# ------------

before_install = "traceability_themes.install.before_install"

# Override Page Controller
# ------------
# extend_website_page_controller_context = {
# 	"frappe.www.desk" : [
# 		"traceability_themes.www.desk"
# 	]
# }

