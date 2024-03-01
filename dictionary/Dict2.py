''''Given a dictionary x={'k1':'v1',k2':'v2', k3':'v3'), create a dictionary with opposite mapping.'''
dctO={value:key for key,value in dct.items()}
print(dctO)
