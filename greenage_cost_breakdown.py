import streamlit as st
import pandas as pd

# Base buying costs before markup
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

# Markup and cost percentages
markup_percent = 0.3
accessories_percent = 0.15
installation_percent = 0.13
discount_percent = 0.02

def calculate_breakdown(solar_kwp, inverter_kva, battery_kwh, category):
    if category not in buying_costs:
        return "Invalid category."

    rates = buying_costs[category]
    
    # Equipment costs after markup
    solar_cost = solar_kwp * rates["solar"] * (1 + markup_percent)
    inverter_cost = inverter_kva * rates["inverter"] * (1 + markup_percent)
    battery_cost = battery_kwh * rates["battery"] * (1 + markup_percent)

    equipment_total = solar_cost + inverter_cost + battery_cost
    accessories_cost = equipment_total * accessories_percent
    installation_cost = equipment_total * installation_percent
    discount = equipment_total * discount_percent
    total_project_cost = equipment_total + accessories_cost + installation_cost - discount

    # Prepare data for display
    data = {
        "Item": ["Solar", "Inverter", "Battery", "Accessories", "Installation", "Discount", "Total"],
        "Amount (₦)": [
            round(solar_cost),
            round(inverter_cost),
            round(battery_cost),
            round(accessories_cost),
            round(installation_cost),
            -round(discount),
            round(total_project_cost)
        ]
    }

    df = pd.DataFrame(data)
    return df

# --- Streamlit UI ---
st.title("🔆 Greenage Solar System Estimator")
st.write("Select your system type and enter specifications to get a detailed price estimate.")

# User inputs
category = st.selectbox("Select system type", ["Midrange", "High-end"])
solar_kwp = st.number_input("☀️ Solar panel capacity (kWp)", min_value=0.0, value=2.0)
inverter_kva = st.number_input("⚡ Inverter capacity (kVA)", min_value=0.0, value=2.0)
battery_kwh = st.number_input("🔋 Battery capacity (kWh)", min_value=0.0, value=5.0)

# Calculate and display
if st.button("📊 Calculate Cost"):
    breakdown_df = calculate_breakdown(solar_kwp, inverter_kva, battery_kwh, category)
    st.subheader(f"{category} System Estimate")
    st.table(breakdown_df)


