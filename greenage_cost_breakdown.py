
def calculate_costs(solar_kwp, inverter_kva, battery_kwh):
    # Rates (including markup)
    midrange_rates = {
        "solar": 299000,
        "inverter": 143000,
        "battery": 312000
    }

    highend_rates = {
        "solar": 299000,
        "inverter": 286000,
        "battery": 344500
    }

    # Markup & extras
    accessories_percent = 0.15
    installation_percent = 0.13
    discount_percent = 0.02

    def compute_breakdown(rates):
        solar_cost = solar_kwp * rates["solar"]
        inverter_cost = inverter_kva * rates["inverter"]
        battery_cost = battery_kwh * rates["battery"]
        equipment_total = solar_cost + inverter_cost + battery_cost

        accessories_cost = equipment_total * accessories_percent
        installation_cost = equipment_total * installation_percent
        discount = equipment_total * discount_percent

        total_project_cost = equipment_total + accessories_cost + installation_cost - discount

        return {
            "Solar": solar_cost,
            "Inverter": inverter_cost,
            "Battery": battery_cost,
            "Accessories": accessories_cost,
            "Installation": installation_cost,
            "Discount": discount,
            "Total": total_project_cost
        }

    midrange = compute_breakdown(midrange_rates)
    highend = compute_breakdown(highend_rates)

    return midrange, highend


def print_breakdown(label, breakdown):
    print(f"\n### {label} Option")
    print("| Item         | Amount (₦)     |")
    print("|--------------|----------------|")
    print(f"| Solar        | ₦{breakdown['Solar']:,.0f}       |")
    print(f"| Inverter     | ₦{breakdown['Inverter']:,.0f}       |")
    print(f"| Battery      | ₦{breakdown['Battery']:,.0f}     |")
    print(f"| Accessories  | ₦{breakdown['Accessories']:,.0f}       |")
    print(f"| Installation | ₦{breakdown['Installation']:,.0f}       |")
    print(f"| **Discount** | **−₦{breakdown['Discount']:,.0f}**   |")
    print(f"| **Total**    | **₦{breakdown['Total']:,.0f}** |")


# Example usage:
solar_kwp = 2
inverter_kva = 2
battery_kwh = 5

midrange, highend = calculate_costs(solar_kwp, inverter_kva, battery_kwh)

print_breakdown("Midrange", midrange)
print_breakdown("High-End", highend)
