"""
Aircraft Stability and Trim Analysis

Computational study of longitudinal aircraft stability,
static margin, neutral point, pitching moment, and trim.
"""

import numpy as np
import matplotlib.pyplot as plt


# ==============================
# Aircraft Parameters
# ==============================

MASS = 1200.0              # kg
WING_AREA = 16.2           # m²
MEAN_CHORD = 1.5           # m

CG_LOCATION = 0.30         # x/c
AC_LOCATION = 0.25         # x/c

TAIL_VOLUME = 0.70
TAIL_EFFICIENCY = 0.90

CL_ALPHA = 5.5             # per radian
CM_ALPHA = -0.50           # per radian

G = 9.80665                # m/s²


# ==============================
# Aircraft Weight
# ==============================

WEIGHT = MASS * G


# ==============================
# Neutral Point Analysis
# ==============================

TAIL_EFFECT = TAIL_EFFICIENCY * TAIL_VOLUME * CL_ALPHA

NEUTRAL_POINT = AC_LOCATION + TAIL_EFFECT / CL_ALPHA

STATIC_MARGIN = NEUTRAL_POINT - CG_LOCATION


# ==============================
# Stability Classification
# ==============================

if STATIC_MARGIN > 0:
    STABILITY_STATUS = "Statically Stable"
elif STATIC_MARGIN < 0:
    STABILITY_STATUS = "Statically Unstable"
else:
    STABILITY_STATUS = "Neutral Stability"


# ==============================
# Display Results
# ==============================

print("Aircraft Stability and Trim Analysis")
print("--------------------------------------")

print(f"Aircraft Mass      : {MASS:.1f} kg")
print(f"Aircraft Weight    : {WEIGHT:.2f} N")
print(f"CG Location        : {CG_LOCATION:.3f} c")
print(f"AC Location        : {AC_LOCATION:.3f} c")
print(f"Neutral Point      : {NEUTRAL_POINT:.3f} c")
print(f"Static Margin      : {STATIC_MARGIN:.3f} c")
print(f"Stability Status   : {STABILITY_STATUS}")

