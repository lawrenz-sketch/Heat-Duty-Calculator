import streamlit as st

st.set_page_config(page_title="Heat Duty Calculator", page_icon="🌡️", layout="centered")

st.title("🌡️ Heat Duty Calculator")
st.caption("Calculate the heat duty required to change a fluid's temperature.")

st.latex(r"Q = \dot{m} \times C_p \times (T_{out} - T_{in})")
st.info("With mass flow in kg/s and specific heat capacity in kJ/(kg·°C), heat duty is calculated in kW.")

with st.container(border=True):
    st.subheader("Operating inputs")
    c1, c2 = st.columns(2)
    with c1:
        mass_flow = st.number_input("Mass Flow Rate (m)", min_value=0.0, value=0.0, step=0.5, format="%.4f", help="kg/s")
        cp = st.number_input("Specific Heat Capacity (Cp)", min_value=0.0, value=4.18, step=0.01, format="%.4f", help="kJ/(kg·°C)")
        inlet_temp = st.number_input("Inlet Temperature (Tin)", value=0.0, step=1.0, format="%.2f", help="°C")
    with c2:
        outlet_temp = st.number_input("Outlet Temperature (Tout)", value=0.0, step=1.0, format="%.2f", help="°C")
        boiling_point = st.number_input("Fluid Boiling Point", value=100.0, step=1.0, format="%.2f", help="°C")

heat_duty = mass_flow * cp * (outlet_temp - inlet_temp)

st.divider()
st.subheader("Results")
r1, r2 = st.columns(2)
with r1:
    st.metric("Required Heat Duty (Q)", f"{heat_duty:,.4f} kW")
with r2:
    st.metric("Temperature Difference", f"{outlet_temp - inlet_temp:,.2f} °C")

if outlet_temp >= boiling_point:
    st.error("⚠️ WARNING: Target temperature meets or exceeds the boiling point. A phase change to gas may occur.")
elif outlet_temp < boiling_point:
    st.success("✅ Safe Liquid Phase: Operating below the boiling threshold.")
else:
    st.warning("Enter valid operating conditions to determine system status.")

with st.expander("How the calculation works"):
    st.markdown("""
    - **m** — mass flow rate in kg/s
    - **Cp** — specific heat capacity in kJ/(kg·°C)
    - **Tout** — outlet/target temperature in °C
    - **Tin** — inlet temperature in °C
    - **Q** — heat duty in kW

    A positive result means heat is added; a negative result means heat is removed.
    This is a simplified sensible-heat calculation and does not include latent heat during phase change.
    The boiling-point warning is an indicator only; actual boiling conditions depend on pressure and fluid composition.
    """)
