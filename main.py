#!/usr/bin/env python3
"""
Structural Engine — Main Entry Point

A professional structural analysis software using the Direct Stiffness Method (DSM)
for 2D and 3D Frame/Truss systems.

Features:
  - 2D and 3D linear static analysis
  - P-Delta (geometric nonlinearity) analysis
  - Modal (free vibration) analysis
  - Buckling (stability) analysis
  - Modern GUI with CustomTkinter
  - Interactive Matplotlib visualization
  - CAD mode for click-to-create modeling
  - Internal force diagrams (N, V, M)
  - Deformed shape visualization (Hermitian interpolation)
  - Excel import/export
  - PDF report generation
  - Auto-stabilization for numerical safety
  - Undo/Redo system
  - Design checks (stress capacity)

Author: Muratcan Kilictepe (2511657)
Course: CE 4011 — Structural Analysis
University: Middle East Technical University (METU)
Date: June 2025
"""

import sys
import os
import customtkinter as ctk

# Add project root to path so imports work correctly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Monkey-patch CTkScrollableFrame to prevent 'str object has no attribute master' error
_original_check = ctk.windows.widgets.ctk_scrollable_frame.CTkScrollableFrame.check_if_master_is_canvas
def _safe_check(self, widget):
    if isinstance(widget, str):
        try:
            widget = self.nametowidget(widget)
        except Exception:
            return False
    if not hasattr(widget, 'master'):
        return False
    return _original_check(self, widget)
ctk.windows.widgets.ctk_scrollable_frame.CTkScrollableFrame.check_if_master_is_canvas = _safe_check

from gui.app import App


def main():
    """Launch the Structural Engine application."""
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
