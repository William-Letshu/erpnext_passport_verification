import frappe
from frappe.model.document import Document

class Customer(Document):
    def validate(self):
        self.layby_eligibility = self.check_layby_eligibility()

    def check_layby_eligibility(self):
        """
        Determines if the customer is eligible for lay-by purchases
        based on verification type and mobile number.
        """
        if (self.verification_type == "ID Number" and self.id_number) or (
            self.verification_type == "Passport" and self.passport_number and self.passport_country_of_origin
        ):
            if self.mobile_no:  # Ensure primary mobile number exists
                return 1
        return 0
