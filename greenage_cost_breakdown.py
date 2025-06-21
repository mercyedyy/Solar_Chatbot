import streamlit as st

# Base buying costs (before markup)
buying_costs = {
    "Midrange": {
        "solar": 230000,
        "inverter": 110000,
        "battery": 240000
    },
    "High-end": {
        "solar": 230000,
        "inverter": 220000,
        "battery": 265000
    }
}

# Markup and other percentages
markup_percent = 0.3
accessories_percent = 0.15
installation_percent = 0.13
discount_percent = 0.02

def calculate_breakdown(solar_kwp, inverter_kva, battery_kwh, category):
    if category not in buying_costs:
        return "Invalid category."

    # Get base rates
    rates = buying_costs[category]
    
    # Apply markup
    solar_cost = solar_kwp * rates["solar"] * (1 + markup_percent)
    inverter_cost = inverter_kva * rates["inverter"] * (1 + markup_percent)
    battery_cost = battery_kwh * rates["battery"] * (1 + markup_percent)

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

# --- Streamlit UI ---
st.title("🔆 Greenage Solar System Estimator")
st.write("Enter your system specs to view both Midrange and High-end cost breakdowns:")

solar_kwp = st.number_input("☀️ Solar panel capacity (kWp)", min_value=0.0, value=2.0)
inverter_kva = st.number_input("⚡ Inverter capacity (kVA)", min_value=0.0, value=2.0)
battery_kwh = st.number_input("🔋 Battery capacity (kWh)", min_value=0.0, value=5.0)

if st.button("🧾 Show Price Estimate"):
    for category in ["Midrange", "High-end"]:
        st.subheader(f"{category} System Estimate")
        breakdown = calculate_breakdown(solar_kwp, inverter_kva, battery_kwh, category)
        if isinstance(breakdown, str):
            st.error(breakdown)
        else:
            for item, cost in breakdown.items():
                label = "💰 " if item == "Total" else "•"
                st.write(f"{label} {item}: ₦{cost:,.0f}")

