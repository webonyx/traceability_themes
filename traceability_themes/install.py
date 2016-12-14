# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe, os

def before_install():
	"""Make symlink to frappe for building"""
	app_name = __name__.split(".")[0]
	source = frappe.get_app_path("frappe", "public", "js", "lib")
	target = frappe.get_app_path(app_name, "public", "js", "lib")

	if not os.path.exists(target):
		os.symlink(source, target)

	for _dir in ["font", "octicons", "shepherd"]:
		source = frappe.get_app_path("frappe", "public", "css", _dir)
		target = frappe.get_app_path(app_name, "public", "css", _dir)

		if not os.path.exists(target):
			os.symlink(source, target)

	for _css in ["bootstrap.css", "font-awesome.css", "cal-heatmap.css", "c3.min.css"]:
		source = frappe.get_app_path("frappe", "public", "css", _css)
		target = frappe.get_app_path(app_name, "public", "css", _css)

		if not os.path.exists(target):
			os.symlink(source, target)
