import netCDF4
import numpy as np

#read the names of all the variables
ds = netCDF4.Dataset("ggas2014121200_00-18.nc")

#print the header of a variable
sst = ds.variables["SSTK"]

#slice sst and store in arr
arr = sst[1, 0, 10:20, 30:35]
print(type(arr))

vars = ds.variables
arr_time = vars["time"][1]
arr_level = vars["surface"][0]
arr_lats = vars["latitude"][10:20]
arr_lons = vars["longitude"][30:35]

for vals in (arr_time, arr_level, arr_lats, arr_lons):
    print(vals)

metadata = {}
for attr in sst.ncattrs():
    metadata[attr] = getattr(sst, attr)

print(metadata)
