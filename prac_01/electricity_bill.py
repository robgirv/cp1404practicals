TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
chosen_tariff = int(input("Which tariff? 11 or 31: "))
daily_use_in_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
if chosen_tariff == 11:
    estimated_bill = ((TARIFF_11 * daily_use_in_kwh) * number_of_billing_days)
else:
    estimated_bill = ((TARIFF_31 * daily_use_in_kwh) * number_of_billing_days)
print(f"Estimated bill: ${estimated_bill:.2f}")
