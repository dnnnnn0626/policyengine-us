from policyengine_us.model_api import *


class la_child_tax_credit_non_refundable(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana non-refundable Child Expense Tax credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.revenue.louisiana.gov/IndividualIncomeTax/SchoolReadinessTaxCredit"
    defined_for = StateCode.LA
    
    def formula(tax_unit, period, parameters):
        child_expense_credit = tax_unit("la_child_expense_tax_credit", period)
        eligible = ~tax_unit("la_child_expense_tax_credit_refundable_eligible", period)
        return eligible * child_expense_credit
