frappe.provide('frappe.desktop');

$.extend(frappe.desktop, {
    reset_background: function () {
        if (!frappe.boot.user.background_image) {
            // todo to be configurable
            var background = "background-color: black;";

            // Override frappe default color
            frappe.dom.set_style(repl('%(selector)s { \
                %(background)s \
            }', {
                selector: '#page-desktop',
                background: background
            }));
        }
    }
});

$(document).on("desktop-render", function () {
    if (!frappe.list_desktop) {
        frappe.desktop.reset_background();
    }
});

