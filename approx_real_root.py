def approx_real_root(coeffs, interval):
    a0, a1, a2, a3 = coeffs
    b, c = interval
    
    def P(x):
        return a0 + a1*x + a2*x**2 + a3*x**3 
    fb = P(b)
    fc = P(c)
    
    if fb == 0:
        return float(b)
    if fc == 0:
        return float(c)
    
    while c - b > 1e-9:
        m = (b+c)/2 
        fm = P(m)
        
        if fb * fm < 0:
            c = m
            fc = fm
        else:
            b = m
            fb = fm
            
    return (b+c)/2

coeffs = [1,-4,0,1]
interval = (0.0, 1.0)

root = approx_real_root(coeffs, interval)
print(root)

        
     
     
     

     
    
