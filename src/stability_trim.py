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

CG_LOCATION = 0.30        # x/c
AC_LOCATION = 0.25        # x/c

TAIL_VOLUME = 0.70
TAIL_EFFICIENCY = 0.90

CL_ALPHA = 5.5             # per radian
CM_ALPHA = -0.50           # per radian

G = 9.80665                 # m/s²


# ==============================
# Aircraft Weight
# ==============================

WEIGHT = MASS * G


# ==============================
# Static Margin
# ==============================

STATIC_MARGIN = AC_LOCATION - CG_LOCATION


# ==============================
# Display Results
# ==============================

print("Aircraft Stability and Trim Analysis")
print("--------------------------------------")

print(f"Aircraft Mass      : {MASS:.1f} kg")
print(f"Aircraft Weight    : {WEIGHT:.2f} N")
print(f"CG Location        : {CG_LOCATION:.2f} c")
print(f"AC Location        : {AC_LOCATION:.2f} c")
print(f"Static Margin      : {STATIC_MARGIN:.2f} c")

if STATIC_MARGIN > 0:
    print("Stability Status   : Statistically stable")
elif STATIC_MARGIN < 0:
    print("Stability Status   : Statistically unstable")
else:
    print("Stability Status   : Neutral")
