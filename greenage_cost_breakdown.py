import streamlit as st
import pandas as pd

def calculate_breakdown(solar_kwp, inverter_kva, battery_kwh, category):
    if category == "Midrange":
        rates = {"solar": 230000, "inverter": 110000, "battery": 240000}
    elif category == "High-end":
        rates = {"solar": 230000, "inverter": 220000, "battery": 265000}
    else:
        return None

    markup = 1.3
    accessories_percent = 0.15
    installation_percent = 0.13
    discount_percent = 0.02

    solar_cost = solar_kwp * rates["solar"] * markup
    inverter_cost = inverter_kva * rates["inverter"] * markup
    battery_cost = battery_kwh * rates["battery"] * markup

    equipment_total = solar_cost + inverter_cost + battery_cost
    accessories_cost = equipment_total * accessories_percent
    installation_cost = equipment_total * installation_percent
    discount = equipment_total * discount_percent
    total_cost = equipment_total + accessories_cost + installation_cost - discount

    return {
        "Solar": round(solar_cost),
        "Inverter": round(inverter_cost),
        "Battery": round(battery_cost),
        "Accessories": round(accessories_cost),
        "Installation": round(installation_cost),
        "Discount": -round(discount),
        "Total": round(total_cost)
    }

# Streamlit UI
st.title("🔋 Greenage Solar Quote Comparison")

solar_kwp = st.number_input("Enter solar panel capacity (kWp)", value=2.0)
inverter_kva = st.number_input("Enter inverter capacity (kVA)", value=2.0)
battery_kwh = st.number_input("Enter battery capacity (kWh)", value=5.0)
compare_option = st.selectbox("Choose comparison type", ["Midrange", "High-end", "Both"])

if st.button("Generate Estimate"):
    if compare_option == "Both":
        midrange_data = calculate_breakdown(solar_kwp, inverter_kva, battery_kwh, "Midrange")
        highend_data = calculate_breakdown(solar_kwp, inverter_kva, battery_kwh, "High-end")

        df = pd.DataFrame({
            "Item": list(midrange_data.keys()),
            "Midrange (₦)": list(midrange_data.values()),
            "High-end (₦)": list(highend_data.values())
        })
        st.table(df)

    else:
        result = calculate_breakdown(solar_kwp, inverter_kva, battery_kwh, compare_option)
        df = pd.DataFrame({
            "Item": list(result.keys()),
            f"{compare_option} (₦)": list(result.values())
        })
        st.table(df)



