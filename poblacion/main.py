# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import R1, R2, R3, R4, R5    

if __name__ == "__main__": 
    datos = R1.R1() 
    r2 = R2.R2(datos) 
    R3.R3(r2) 
    r4 = R4.R4(r2) 
    R5.R5(r2, r4) 
