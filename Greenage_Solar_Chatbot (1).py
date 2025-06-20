
import streamlit as st

def calculate_cost(solar_kwp, inverter_kva, battery_kwh, category="Midrange"):
    if category.lower() == "midrange":
        solar_rate = 299000
        inverter_rate = 143000
        battery_rate = 312000
    elif category.lower() == "high-end":
        solar_rate = 299000
        inverter_rate = 286000
        battery_rate = 344500
    else:
        return "Invalid category selected."

    markup = 1.3
    accessories_percent = 0.15
    installation_percent = 0.13
    discount_percent = 0.02

    solar_cost = solar_kwp * solar_rate * markup
    inverter_cost = inverter_kva * inverter_rate * markup
    battery_cost = battery_kwh * battery_rate * markup

    equipment_total = solar_cost + inverter_cost + battery_cost
    accessories_cost = equipment_total * accessories_percent
    installation_cost = equipment_total * installation_percent
    discount = equipment_total * discount_percent

    total_project_cost = equipment_total + accessories_cost + installation_cost - discount
    return round(total_project_cost, 2)

st.title("🌞 Greenage Solar Chatbot")
st.write("Enter your solar system specs to get a price estimate.")

solar_kwp = st.number_input("🔋 Solar panel capacity (kWp)", min_value=0.0, value=2.0)
inverter_kva = st.number_input("⚡ Inverter capacity (kVA)", min_value=0.0, value=2.0)
battery_kwh = st.number_input("🔋 Battery capacity (kWh)", min_value=0.0, value=5.0)
category = st.selectbox("Select system type", ["Midrange", "High-end"])

if st.button("💰 Calculate Price"):
    price = calculate_cost(solar_kwp, inverter_kva, battery_kwh, category)
    st.success(f"Estimated total project cost ({category}): ₦{price:,.0f}")
