{
   /* 
    * NRPy+ Finite Difference Code Generation, Step 1 of 1: Evaluate SymPy expressions and write to main memory:
    */
   /*
    *  Original SymPy expressions:
    *  "[in_gfs[IDX4(UUGF, i0, i1, i2)] = uu_in,
    *    in_gfs[IDX4(VVGF, i0, i1, i2)] = vv_in]"
    */
   in_gfs[IDX4(UUGF, i0, i1, i2)] = uu_in;
   in_gfs[IDX4(VVGF, i0, i1, i2)] = vv_in;
}

