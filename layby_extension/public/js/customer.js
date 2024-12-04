frappe.ui.form.on('Customer', {
    verification_type: function (frm) {
        // Dynamically show or hide fields based on Verification Type
        if (frm.doc.verification_type === "ID Number") {
            frm.set_df_property("id_number", "reqd", true);
            frm.set_df_property("passport_number", "reqd", false);
            frm.set_df_property("passport_country_of_origin", "reqd", false);

            frm.set_df_property("id_number", "hidden", false);
            frm.set_df_property("passport_number", "hidden", true);
            frm.set_df_property("passport_country_of_origin", "hidden", true);
        } else if (frm.doc.verification_type === "Passport") {
            frm.set_df_property("passport_number", "reqd", true);
            frm.set_df_property("passport_country_of_origin", "reqd", true);
            frm.set_df_property("id_number", "reqd", false);

            frm.set_df_property("id_number", "hidden", true);
            frm.set_df_property("passport_number", "hidden", false);
            frm.set_df_property("passport_country_of_origin", "hidden", false);
        } else {
            frm.set_df_property("id_number", "reqd", false);
            frm.set_df_property("passport_number", "reqd", false);
            frm.set_df_property("passport_country_of_origin", "reqd", false);

            frm.set_df_property("id_number", "hidden", true);
            frm.set_df_property("passport_number", "hidden", true);
            frm.set_df_property("passport_country_of_origin", "hidden", true);
        }
    },

    validate: function (frm) {
        // Enforce validation before saving
        if (frm.doc.verification_type === "ID Number" && !frm.doc.id_number) {
            frappe.msgprint(__("Please provide an ID Number."));
            frappe.validated = false;
        } else if (frm.doc.verification_type === "Passport" && 
            (!frm.doc.passport_number || !frm.doc.passport_country_of_origin)) {
            frappe.msgprint(__("Please provide a Passport Number and Country of Origin."));
            frappe.validated = false;
        }
    },

    refresh: function (frm) {
        // Trigger the visibility logic on form load
        frm.trigger("verification_type");
    }
});
