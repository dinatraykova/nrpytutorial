# Generating C code for plane wave initial
#  data for the scalar wave equation in
#  ***Cartesian*** coordinates, in up to
#  *three* spatial dimensions
#
# Author: Zachariah B. Etienne
#         zachetie **at** gmail **dot* com
#
# License: BSD 2-Clause

# COMPLETE DOCUMENTATION (JUPYTER NOTEBOOKS):
# START PAGE (start here!):  ../NRPy+_Tutorial.ipynb
# THIS MODULE: ../Tutorial-Scalarwave.ipynb

# Step P1: Import needed NRPy+ core modules:
#from outputC import * # Needed for lhrh() named tuple
import grid as gri
import NRPy_param_funcs as par
import numpy as np
import sympy as sp

thismodule = __name__
uu_in = par.Cparameters("REAL", thismodule, "uu_in")
vv_in = par.Cparameters("REAL", thismodule, "vv_in")

def ID_array_scalar():
    # Step 1: Set parameters defined in other modules
    DIM = par.parval_from_str("grid::DIM")
    xx = gri.xx
    scalar_posn = par.Cparameters("REAL", thismodule, ["scalar_posn_x","scalar_posn_y","scalar_posn_z"])
    
    scalar_r2 = sp.sympify(0)
    for i in range(DIM):
        scalar_r2 += (xx[i] - scalar_posn[i])**2
    scalar_r = sp.sqrt(scalar_r2)
    
    Pi_in = np.loadtxt('InitialData/Pi001.csv')
    r_in = np.arange(0,1000.02,0.01)
    # Step 5: Set initial data for uu and vv, where vv_ID = \partial_t uu_ID.
    global uu_ID,vv_ID
    uu_ID = uu_in
    vv_ID = vv_in