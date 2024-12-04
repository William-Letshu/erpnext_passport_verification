import frappe
from frappe.model.document import Document

class Customer(Document):
    def validate(self):
        if self.verification_type == "ID Number" and not self.id_number:
            frappe.throw("ID Number is required when 'Verification Type' is 'ID Number'.")
        elif self.verification_type == "Passport" and (not self.passport_number or not self.passport_country_of_origin):
            frappe.throw("Passport Number and Country of Origin are required when 'Verification Type' is 'Passport'.")

        self.layby_eligibility = self.check_layby_eligibility()

    def check_layby_eligibility(self):
        """
        Determines if the customer is eligible for lay-by purchases
        based on verification type and mobile number.
        """
        if (self.verification_type == "ID Number" and self.id_number) or (
            self.verification_type == "Passport" and self.passport_number and self.passport_country_of_origin
        ):
            if self.mobile_no:
                return 1
        return 0
