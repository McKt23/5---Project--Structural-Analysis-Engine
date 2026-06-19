# Prota Structural Engine v7.0

A professional structural analysis software using the **Direct Stiffness Method (DSM)** for 2D and 3D Frame/Truss systems.

**Author:** Muratcan Kilictepe (2511657)  
**Course:** CE 4011 — Structural Analysis  
**University:** Middle East Technical University (METU)  
**Date:** June 2025

---

## Features

### Core Solver
- 2D analysis (3 DOF/node: Ux, Uy, Rz)
- 3D analysis (6 DOF/node: Ux, Uy, Uz, Rx, Ry, Rz)
- Frame and Truss element types
- Penalty method for boundary conditions (10^12)
- Support settlements
- Nodal loads (forces and moments)
- Member loads (point and distributed)
- Thermal effects (uniform temperature + gradient through depth)
- Internal hinge releases (static condensation)
- Exact reaction calculation via sub-matrix approach
- Global equilibrium verification

### Advanced Analysis
- **P-Delta Analysis**: Geometric nonlinearity via geometric stiffness matrix, iterative solution
- **Modal Analysis**: Free vibration eigenvalue problem, natural frequencies and mode shapes
- **Buckling Analysis**: Linear stability eigenvalue, critical load factors

### Visualization
- Internal force diagrams (N, V, M) with filled polygons
- Deformed shape overlay (Hermitian cubic interpolation)
- Support symbols (fixed, pin, roller)
- Nodal load arrows and member load visualization
- Hover tooltips with displacement and reaction data
- Zoom/Pan/Fit

### GUI & UX
- Modern dark/light mode (CustomTkinter)
- Interactive CAD mode (click-to-create nodes and elements)
- Excel-like data grids with debounced sync
- Template generator (multi-story frames, trusses)
- Undo/Redo system with hash deduplication
- Non-blocking analysis (threading)
- Design checks (stress capacity)

### I/O
- Excel import/export (pandas + openpyxl)
- PDF report generation (FPDF)

---

## Requirements

- Python 3.9+
- NumPy
- SciPy
- Matplotlib
- CustomTkinter
- Pandas + openpyxl (for Excel I/O)
- FPDF (for PDF reports)

### Installation

```bash
pip install numpy scipy matplotlib customtkinter pandas openpyxl fpdf
```

---

## How to Run

```bash
python main.py
```

---

## Project Structure

```
prota_engine/
├── main.py                  # Entry point
├── core/                    # Model + Engine (MVC: Model)
│   ├── models.py            # Node, Element, MemberLoad, Structure
│   ├── solver.py            # LinearSolver (DSM engine)
│   ├── stabilizer.py        # Auto-stabilization
│   └── advanced.py          # P-Delta, Modal, Buckling
├── gui/                     # Interface (MVC: View + Controller)
│   ├── app.py               # Main application window
│   ├── canvas.py            # Matplotlib visualization
│   └── grids.py             # Data grid panels
├── utils/                   # I/O Utilities
│   ├── excel_io.py          # Excel import/export
│   └── pdf_report.py        # PDF report generation
└── README.md
```

### Architecture: MVC Pattern

| Layer | Module | Responsibility |
|-------|--------|----------------|
| **Model** | `core/models.py` | Data classes (Node, Element, etc.) |
| **Model** | `core/solver.py` | Linear DSM solver |
| **Model** | `core/advanced.py` | P-Delta, Modal, Buckling |
| **Model** | `core/stabilizer.py` | Auto-stabilization |
| **View** | `gui/canvas.py` | Matplotlib visualization |
| **View** | `gui/grids.py` | Data input grids |
| **Controller** | `gui/app.py` | Event handling, layout |

---

## Verification

Results were validated against:
1. Assignment 4 hand-calculated examples
2. Built-in equilibrium check (Sum(Fx)=0, Sum(Fy)=0, Sum(M)=0)
3. Known structural mechanics principles

### Example Verification

For a simple portal frame with 10 kN vertical load:
- Sum(Fy) ≈ -1.78e-15 kN (machine precision zero)
- Sum(M) ≈ -3.55e-15 kNm (machine precision zero)
- Design status: All elements OK

---

## Known Limitations

1. 3D internal force diagrams not yet implemented (analysis works, visualization is 2D)
2. Load combinations UI exists but backend not fully integrated
3. Consistent mass matrix not implemented (uses lumped mass)
4. No code-specific design checks (uses generic yield stress)
5. Member loads only in transverse direction (no axial member loads)

---

## Key Algorithms

### Direct Stiffness Method
1. Build element local stiffness matrices (6x6 for 2D, 12x12 for 3D)
2. Transform to global coordinates using rotation matrices
3. Assemble into global stiffness matrix K
4. Apply boundary conditions via penalty method
5. Solve K·U = F using numpy.linalg.solve
6. Back-calculate reactions and internal forces

### Static Condensation (Hinge Releases)
Eliminates moment DOFs at specified ends by modifying the stiffness matrix:
```
K_new[i,j] -= K[i,r] * K[r,j] / K[r,r]
```

### Thermal Effects
- Axial: P_thermal = E * A * alpha * dT_avg
- Bending: M_thermal = E * I * alpha * dT_grad / h

### Hermitian Shape Functions (Deformed Shape)
- N1 = 1 - 3ξ² + 2ξ³
- N2 = x(1 - 2ξ + ξ²)
- N3 = 3ξ² - 2ξ³
- N4 = x(ξ² - ξ)

---

## License

Academic project — CE 4011 Term Project, METU, 2025.
