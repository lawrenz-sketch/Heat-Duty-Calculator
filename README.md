# Heat Duty Calculator

An app that quickly calculates how much energy is needed to heat or cool a liquid using real-time data, preventing manual calculation mistakes when checking work in the field.

## Features
- Live heat-duty calculation: `Q = m × Cp × (Tout - Tin)`
- Inputs for mass flow rate, specific heat capacity, inlet temperature, outlet temperature, and boiling point
- Safe-liquid status and boiling-point warning
- Clear units and calculation notes

## Run locally

Requires Python 3.9 or newer.

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies and launch:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Your browser should open the app at the local address shown in the terminal.

## Calculation
`Q (kW) = mass flow rate (kg/s) × specific heat capacity (kJ/kg·°C) × (outlet temperature − inlet temperature) (°C)`

This is a simplified sensible-heat calculation. The warning compares the target temperature with the user-entered boiling point and does not model pressure-dependent boiling or latent heat.
