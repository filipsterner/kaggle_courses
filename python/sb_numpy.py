import numpy as np
'''

print(x.flags)
print(x.shape)
print(x.strides)
print(x.ndim)
print(x.data)
print(x.size)
print(x.itemsize)
print(x.nbytes)
print(x.base)

print(x.dtype)
print(x.T)
print(x.real)
print(x.imag)
print(x.flat)
for y in x.flat:
    print(y)



print(x.__array_interface__)
print(type(x.__array_struct__))
print(x.ctypes)


print(x.item(3))
print(x.item((1,0)))

print(x.tolist())
print(x.tobytes())
x.tofile('temp.txt', sep='\n', format='%f')
x.tofile('temp.bin', sep='', format='%d')
print('\n')
print(x.dumps())
print('\n')
print(x.astype(np.uint8).dtype)
print(x.astype(np.int16).byteswap(inplace=True))
print(x.view(np.single))
print(x.getfield(np.uint8))
x.setflags(write=False, align=True, uic=False)
print(x.flags)
x.setflags(write=True, align=True, uic=False)
x.fill(1)
print(x)

https://numpy.org/doc/stable/reference/arrays.ndarray.html#shape-manipulation

'''

x = np.array([[1, 2, 3], [4, 5, 1056]], np.int32)

