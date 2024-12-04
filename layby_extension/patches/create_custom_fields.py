import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Customer": [
            {
                "fieldname": "verification_type",
                "label": "Verification Type",
                "fieldtype": "Select",
                "options": "\nNone\nID Number\nPassport",
                "insert_after": "email_id",
                "reqd": 0
            },
            {
                "fieldname": "layby_eligibility",
                "label": "Lay-by Eligibility",
                "fieldtype": "Check",
                "insert_after": "passport_country_of_origin",
                "read_only": 0  # Make the field writable
            }
        ]
    }
    create_custom_fields(custom_fields, update=True)
