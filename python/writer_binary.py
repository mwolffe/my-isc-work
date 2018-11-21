import struct

bin_data = struct.pack("bbbb", 123, 12, 45, 34)

#write bin_data as a binary
with open('mybinary.dat', 'wb') as writer:
    writer.write(bin_data)

with open('mybinary.dat', 'rb') as reader:
    bin_data2 = reader.read()
    
data = struct.unpack("bbbb", bin_data2)

print(data)
