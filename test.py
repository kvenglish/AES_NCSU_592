# import numpy as np
#
# key = "d6aa74fdd2af72fadaa678f1d6ab76fe"
#
# array = bytearray.fromhex(key)
# print(array.hex())
#
# array_hex = array.hex()
# print(array_hex)
#
# i=0
# new_array = [0] * 16
# for x in array:
#     new_array[i]=hex(x)
#     i+=1
#
# print(new_array)
# print(new_array[0])
#
# print(0x4f^0x73)
# print(hex(60))
#
#
# array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# nparray = np.array(array)
# nparray = nparray.reshape(4,4)
# print(nparray)
# nparray = np.rot90(nparray)
# nparray = np.flipud(nparray)
# print(nparray)
#
# print(0x02 * 0x63)
#
# a = 47
# b = (a<<1)^a
#
# print(b)
#
# print(b)
# print(a^b)

a = [0] * 4
row = [1,2,3,1]
col = [0xa0, 0xc0, 0x30, 0x2b]
for i in range(4):
    mix_val = row[i]
    if mix_val == 1:
        a[i] = col[i]
    elif mix_val == 2:
        a[i] = col[i]<<1
        if a[i] > 255:
            a[i] = a[i] ^ 0b100011011
        print(a[i])
    else:
        a[i] = (col[i]<<1)
        if a[i] > 255:
            a[i] = a[i] ^ 0b100011011
        a[i] = a[i]^col[i]

        print(a[i])



print(a)
b = a[0]^a[1]^a[2]^a[3]
print(b)
print(b&0b11111111)

