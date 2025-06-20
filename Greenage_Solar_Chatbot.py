{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ef5091b0-53d7-4809-8898-3ef2ef2c6276",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "💬 Welcome to Greenage Solar Chatbot!\n",
      "Let's calculate the price for your solar system setup.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter solar panel capacity in kWp (e.g., 2):  2\n",
      "Enter inverter capacity in kVA (e.g., 2):  2\n",
      "Enter battery capacity in kWh (e.g., 5):  5\n",
      "Do you want 'Midrange' or 'High-end'?  Midrange\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "✅ Estimated total project cost (Midrange): ₦4,003,272\n"
     ]
    }
   ],
   "source": [
    "def calculate_cost(solar_kwp, inverter_kva, battery_kwh, category=\"Midrange\"):\n",
    "    # Pricing rates\n",
    "    if category.lower() == \"midrange\":\n",
    "        solar_rate = 299000\n",
    "        inverter_rate = 143000\n",
    "        battery_rate = 312000\n",
    "    elif category.lower() == \"high-end\":\n",
    "        solar_rate = 299000\n",
    "        inverter_rate = 286000\n",
    "        battery_rate = 344500\n",
    "    else:\n",
    "        return \"Invalid category selected.\"\n",
    "\n",
    "    # Markup & extras\n",
    "    markup = 1.3  # 30%\n",
    "    accessories_percent = 0.15\n",
    "    installation_percent = 0.13\n",
    "    discount_percent = 0.02\n",
    "\n",
    "    # Equipment costs (with markup)\n",
    "    solar_cost = solar_kwp * solar_rate * markup\n",
    "    inverter_cost = inverter_kva * inverter_rate * markup\n",
    "    battery_cost = battery_kwh * battery_rate * markup\n",
    "\n",
    "    equipment_total = solar_cost + inverter_cost + battery_cost\n",
    "\n",
    "    # Accessories and fees\n",
    "    accessories_cost = equipment_total * accessories_percent\n",
    "    installation_cost = equipment_total * installation_percent\n",
    "    discount = equipment_total * discount_percent\n",
    "\n",
    "    total_project_cost = equipment_total + accessories_cost + installation_cost - discount\n",
    "\n",
    "    return round(total_project_cost, 2)\n",
    "\n",
    "\n",
    "# --- Chatbot start ---\n",
    "print(\"💬 Welcome to Greenage Solar Chatbot!\")\n",
    "print(\"Let's calculate the price for your solar system setup.\\n\")\n",
    "\n",
    "try:\n",
    "    solar_kwp = float(input(\"Enter solar panel capacity in kWp (e.g., 2): \"))\n",
    "    inverter_kva = float(input(\"Enter inverter capacity in kVA (e.g., 2): \"))\n",
    "    battery_kwh = float(input(\"Enter battery capacity in kWh (e.g., 5): \"))\n",
    "    category = input(\"Do you want 'Midrange' or 'High-end'? \").strip()\n",
    "\n",
    "    price = calculate_cost(solar_kwp, inverter_kva, battery_kwh, category)\n",
    "\n",
    "    print(f\"\\n✅ Estimated total project cost ({category}): ₦{price:,.0f}\")\n",
    "\n",
    "except Exception as e:\n",
    "    print(\"⚠️ Error: Please enter valid numbers.\")\n",
    "    print(\"Details:\", e)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8af73d3-ef8a-47e3-979b-5ba8a99232e9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
