# Pulsatile Pump Modelling

A comprehensive computational fluid dynamics (CFD) simulation of pulsatile blood flow through the heart, combining cardiac physiology with fluid mechanics to model and visualize hemodynamic behavior.

## 📋 Project Overview

This project models the pulsatile (rhythmic) flow of blood through the cardiovascular system during a complete cardiac cycle. It integrates realistic cardiac physiology parameters with computational fluid dynamics to simulate:

- **Cardiac Cycle Dynamics**: Models the four phases of the cardiac cycle (isovolumetric contraction, ejection, isovolumetric relaxation, and filling)
- **Blood Flow Kinematics**: Simulates particle advection through a velocity field to visualize blood movement
- **Hemodynamic Parameters**: Calculates and visualizes Reynolds number and wall shear stress throughout the cycle
- **Pressure-Volume Relationships**: Generates pressure-volume loops characteristic of cardiac function

### Motivation

This project was developed for the **Fluid Mechanics for Medical Scientists** course to bridge the gap between cardiovascular physiology and computational methods. Understanding pulsatile flow dynamics is critical for:
- Predicting blood vessel damage and atherosclerosis development
- Designing medical devices (stents, artificial heart valves)
- Diagnosing cardiovascular diseases
- Optimizing drug delivery mechanisms

## 🎯 Methodology

### Approach

The simulation follows a modular architecture separating concerns into three main components:

1. **Cardiac Physiology Module** (`physiology.py`)
   - Defines a realistic cardiac model with measured physiological parameters
   - Implements the complete cardiac cycle with four distinct phases
   - Calculates time-dependent inlet velocity, pressure, and volume profiles
   - Computes hemodynamic metrics (Reynolds number, wall shear stress)

2. **Flow Solver** (`solver.py`)
   - Integrates particles through the velocity field using simple advection
   - Maintains particle positions and recycles them at domain boundaries
   - Records velocity, Reynolds number, and shear stress histories
   - Generates velocity field profiles based on inlet conditions

3. **Visualization Engine** (`visualization.py`)
   - Real-time animation of pulsatile blood flow with tracer particles
   - Streamline plots showing velocity field evolution
   - Pressure-volume (PV) loops characteristic of cardiac function
   - Waveform plots of velocity, Reynolds number, and wall shear stress

### Cardiac Model Parameters

The model incorporates realistic human physiological parameters:

| Parameter | Value | Description |
|-----------|-------|-------------|
| Heart Rate (HR) | 75 bpm | Typical resting heart rate |
| End-Diastolic Volume (EDV) | 120 mL | Maximum ventricular volume |
| End-Systolic Volume (ESV) | 50 mL | Minimum ventricular volume |
| Stroke Volume (SV) | 70 mL | EDV - ESV |
| Blood Density (ρ) | 1060 kg/m³ | Physiological value for whole blood |
| Blood Viscosity (μ) | 0.0035 Pa·s | Dynamic viscosity at 37°C |
| Vessel Radius | 0.01 m | 1 cm radius aorta approximation |

### Cardiac Cycle Phases

The cardiac cycle is divided into four phases, each with specific duration and characteristics:

1. **Isovolumetric Contraction** (10% of cycle): Ventricular pressure rises with constant volume
2. **Ejection** (30% of cycle): Blood is pumped out as volume decreases and pressure drops
3. **Isovolumetric Relaxation** (10% of cycle): Ventricular pressure drops with constant volume
4. **Filling** (50% of cycle): Ventricle refills with blood returning from circulation

## 🚀 Getting Started

### Requirements

```
Python 3.7+
NumPy
Matplotlib
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/A-b29/Pulsatile-Pump-Modelling.git
cd Pulsatile-Pump-Modelling
```

2. Install dependencies:
```bash
pip install numpy matplotlib
```

### Running the Simulation

Execute the main script to launch the interactive animation:

```bash
python main.py
```

This will display a 6-panel visualization showing:
- **Top-left**: Pulsatile blood particle flow (red dots)
- **Top-middle**: Velocity streamlines with color-mapped magnitude
- **Top-right**: Pressure-volume loop tracing the cardiac cycle
- **Bottom-left**: Inlet velocity waveform
- **Bottom-middle**: Reynolds number evolution
- **Bottom-right**: Wall shear stress evolution

## 📊 Project Structure

```
Pulsatile-Pump-Modelling/
├── README.md                          # This file
├── main.py                            # Entry point for the simulation
├── physiology.py                      # CardiacModel class
├── solver.py                          # FlowSolver class for flow integration
├── visualization.py                   # Visualizer class for animation
└── Fluid_Mechanics_Project_*.pdf      # Original project specification
```

### Module Descriptions

#### `main.py`
Entry point that orchestrates the simulation by:
1. Creating a cardiac model with physiological parameters
2. Initializing a flow solver with the cardiac model
3. Setting up the visualization engine
4. Running the animated simulation

#### `physiology.py` - `CardiacModel`
**Key Methods:**
- `phase(t)`: Returns the current phase within the cardiac cycle
- `volume(t)`: Calculates ventricular volume at time t
- `pressure(t)`: Calculates ventricular pressure at time t
- `inlet_velocity(t)`: Calculates inlet velocity following a sinusoidal profile during ejection
- `reynolds(v)`: Computes Reynolds number for given velocity
- `shear(v)`: Calculates wall shear stress

#### `solver.py` - `FlowSolver`
**Key Methods:**
- `step()`: Advances simulation by one time step (Δt = 0.02 s)
- `velocity_field(v)`: Generates 2D velocity field using a Gaussian profile
- Maintains histories of velocity, Reynolds number, and shear stress

#### `visualization.py` - `Visualizer`
**Key Methods:**
- `update(frame)`: Updates all six visualization panels for each animation frame
- `animate()`: Runs the animation with 800 frames at 40 ms intervals

## 📈 Physical Insights

The simulation demonstrates several important cardiovascular concepts:

1. **Pulsatile Nature**: Flow is not continuous but pulsatile, with significant temporal variation
2. **Reynolds Number**: Typically ranges from 100-400, indicating transitional flow with some turbulent characteristics
3. **Wall Shear Stress**: Varies significantly during the cardiac cycle, affecting endothelial cell function
4. **PV Loop Area**: Represents the work done by the heart during one cycle
5. **Velocity Profile**: Parabolic-like distribution across the vessel radius (simplified Gaussian approximation)

## 🔬 Key Findings

The simulation reveals:
- Peak blood velocity occurs mid-ejection with corresponding maximum Reynolds number
- Wall shear stress follows a similar pattern to velocity, critical for vascular health
- The PV loop traces the characteristic quadrilateral pattern of normal cardiac function
- Blood flow exhibits significant spatial and temporal variation within the cardiac cycle

## 📝 Future Enhancements

Potential improvements for future versions:

1. **Advanced Solvers**: Implement Navier-Stokes solver for more accurate fluid dynamics
2. **3D Visualization**: Extend to three-dimensional flow fields
3. **Multiple Vessels**: Model flow through arteries and capillaries
4. **Pathophysiology**: Simulate diseased states (stenosis, regurgitation, arrhythmias)
5. **Parameter Variation**: Interactive controls to modify heart rate, volume, and other parameters
6. **Data Export**: Save simulation results for statistical analysis
7. **GPU Acceleration**: Use CUDA/OpenCL for real-time high-resolution simulations

## 👥 Contributors

- **MD24B003** (A-b29)
- **MD24B005**

## 📚 References

- Cardiac physiology: Ross, M.H., & Pawlina, W. (2006). *Histology: A Text and Atlas*
- Cardiovascular fluid mechanics: Fung, Y.C. (1997). *Biomechanics: Circulation*
- Blood flow dynamics: Ku, D.N. (1997). Blood flow in arteries. *Annual Review of Fluid Mechanics*

## 📄 Course Information

**Course**: Fluid Mechanics for Medical Scientists  
**Institution**: Medical School  
**Academic Year**: 2026  
**Project Date**: March 2026

## 📦 License

This project is provided for educational purposes.

---

**Note**: This simulation uses simplified models for demonstration. Real cardiovascular systems are significantly more complex, involving multiple chambers, valves, compliance variation, and intricate neural control mechanisms.
