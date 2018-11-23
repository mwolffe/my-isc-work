import netCDF4

#read the names of all the variables
ds = netCDF4.Dataset("ggas2014121200_00-18.nc")
for v in ds.variables:
    print(v)

#print the header of a variable
sst = ds.variables["SSTK"]
print(sst)

#gives the dimensions with names
for d in sst.dimensions:
    print(d, len(ds.variables[d]))

print(sst.shape, sst.size)

for attr in sst.ncattrs():
    print(attr, '=', getattr(sst, attr))
