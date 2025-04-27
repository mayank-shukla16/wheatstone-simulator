import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wheatstone Bridge Simulator", layout="wide")

st.title("⚡ Wheatstone Bridge Interactive Simulation & Real-Life Applications")
st.write("""
This simulation helps you understand how a Wheatstone Bridge works and how it powers real-life applications like:
- **Smartwatches for step detection**
- **Light detection systems (like automatic streetlights)**

Adjust resistor values and see how the bridge balances!
""")

st.image("https://raw.githubusercontent.com/mayank-shukla16/wheatstone-simulator/main/assets./wheatstone%20bridge%20circuit%20diagram.jpg", caption="Basic Wheatstone Bridge Circuit")

st.header("🔧 Set Resistor Values (Ohms)")
R1 = st.slider('R1', 1.0, 1000.0, 100.0)
R2 = st.slider('R2', 1.0, 1000.0, 100.0)
R3 = st.slider('R3', 1.0, 1000.0, 100.0)
Rx = st.slider('Unknown Resistor (Rx)', 1.0, 1000.0, 100.0)
Vs = st.slider('Supply Voltage (V)', 1.0, 10.0, 5.0)

# Calculate node voltages
Vab = Vs * (R2 / (R1 + R2) - Rx / (R3 + Rx))

st.subheader(f"🔍 Bridge Output Voltage (Vab): {Vab:.3f} V")

if abs(Vab) < 0.01:
    st.success("✅ Bridge is Balanced!")
else:
    st.error("❌ Bridge is Not Balanced!")

st.header("📱 Real-Life Applications with Interactive Demos")

st.subheader("1️⃣ Smartwatches & Fitness Trackers — Step Detection")
st.write("""
Smartwatches use tiny **strain gauges** connected in a Wheatstone Bridge setup beneath their step detection sensors. 
When you move your wrist or take a step, it slightly bends a flexible surface, changing resistance.
This imbalance creates a small voltage difference — the microcontroller converts this to a step count.
""")

st.image("https://raw.githubusercontent.com/mayank-shukla16/wheatstone-simulator/main/assets./strain%20guage%20and%20wheatstone%20bridge%20circuit%20diagram.jpg", caption="Strain Gauge Bridge Setup for Step Detection")

# Simulate strain effect
strain = st.slider("Simulated Wrist Movement (Strain %)", 0.0, 5.0, 0.0)
R_strain = 100.0 + strain  # Assuming initial resistance 100 Ohms
Vab_smartwatch = Vs * (R2 / (R1 + R2) - R_strain / (R3 + R_strain))
st.write(f"🦶 Output Voltage with Movement: {Vab_smartwatch:.3f} V")

if abs(Vab_smartwatch) > 0.05:
    st.success("Detected: Movement registered as a step!")
else:
    st.info("No significant movement detected.")

st.subheader("2️⃣ Automatic Light Detection — LDR Control")
st.write("""
Light sensors use **Light Dependent Resistors (LDR)** in a Wheatstone Bridge.
As ambient light changes, the resistance of the LDR varies.
This causes a voltage imbalance that switches streetlights on or off automatically.
""")

st.image("https://raw.githubusercontent.com/mayank-shukla16/wheatstone-simulator/main/assets./ldr%20working%20principle%20diagram.jpg", caption="LDR Working Principle")

# Simulate light intensity effect
light_intensity = st.slider("Simulated Light Intensity (Lux)", 0.0, 1000.0, 500.0)
R_LDR = 1000.0 / (light_intensity + 1)  # Simulated inverse relationship
Vab_light = Vs * (R2 / (R1 + R2) - R_LDR / (R3 + R_LDR))
st.write(f"💡 Output Voltage at Current Light Level: {Vab_light:.3f} V")

if Vab_light > 0.05:
    st.success("Streetlight: ON (It's getting dark)")
else:
    st.info("Streetlight: OFF (Daytime detected)")

st.header("📊 Visualizing Voltage Difference vs Rx")

Rx_values = np.linspace(1, 1000, 500)
Vab_values = Vs * (R2 / (R1 + R2) - Rx_values / (R3 + Rx_values))

fig, ax = plt.subplots()
ax.plot(Rx_values, Vab_values, label='Vab vs Rx')
ax.axhline(0, color='red', linestyle='--', label='Balanced Bridge (V=0)')
ax.set_xlabel('Rx (Ohms)')
ax.set_ylabel('Vab (Volts)')
ax.set_title('Voltage Difference vs Unknown Resistor')
ax.legend()
st.pyplot(fig)

st.write("""
👆 The red line represents a balanced bridge. Adjust the sliders above to see how the graph changes in real-time!
""")
