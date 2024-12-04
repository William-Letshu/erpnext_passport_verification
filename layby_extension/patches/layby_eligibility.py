import frappe

def execute():
    customers = frappe.get_all("Customer", fields=["name", "verification_type", "id_number", "passport_number", "passport_country_of_origin", "mobile_no"])
    for customer in customers:
        layby_eligibility = 0
        if (
            (customer.verification_type == "ID Number" and customer.id_number)
            or (customer.verification_type == "Passport" and customer.passport_number and customer.passport_country_of_origin)
        ) and customer.mobile_no:
            layby_eligibility = 1
        frappe.db.set_value("Customer", customer.name, "layby_eligibility", layby_eligibility)
    frappe.db.commit()
