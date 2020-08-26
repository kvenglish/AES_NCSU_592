import numpy as np

roundkeys = ("000102030405060708090a0b0c0d0e0f",
             "d6aa74fdd2af72fadaa678f1d6ab76fe",
             "b692cf0b643dbdf1be9bc5006830b3fe",
             "b6ff744ed2c2c9bf6c590cbf0469bf41",
             "47f7f7bc95353e03f96c32bcfd058dfd",
             "3caaa3e8a99f9deb50f3af57adf622aa",
             "5e390f7df7a69296a7553dc10aa31f6b",
             "14f9701ae35fe28c440adf4d4ea9c026",
             "47438735a41c65b9e016baf4aebf7ad2",
             "549932d1f08557681093ed9cbe2c974e",
             "13111d7fe3944a17f307a78b4d2b30c5")

plaintext = "00112233445566778899aabbccddeeff"

sbox = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
            0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
            0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
            0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
            0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
            0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
            0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
            0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
            0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
            0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
            0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
            0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
            0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
            0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
            0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
            0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
            0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
            0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
            0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
            0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
            0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
            0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
            0x54, 0xbb, 0x16]

mix_array = ([0x02, 0x03, 0x01, 0x01], [0x01, 0x02, 0x03, 0x01], [0x01, 0x01, 0x02, 0x03], [0x03, 0x01, 0x01, 0x02])

#create dictionary to hold each round's outputs for assignment
round = [{'s':0, 'sub':0,'shift':0,'mix':0} for x in range(11)]

#changes given state into 4x4 numpy matrix with proper formatting
def matrify(state):
    # puts state into numpy array
    array = np.array(state)

    # shapes numpy array into proper 4x4 format with columns/rows correct
    array = array.reshape(4, 4)
    array = np.rot90(array)
    array = np.flipud(array)
    return array

#returns given numpy matrix to 1d bytearray format
def dematrify(self):
    # returns matrix to original 1d format
    self = np.flipud(self)
    self = np.rot90(self, 3)
    self = self.reshape(1, 16)

    # returns numpy array to list
    self = self.tolist()

    # returns self to bytearray
    array = bytearray()
    for i in range(16):
        array.append(self[0][i])

    return array

#performs the left shift, left shift and xor, or none as required for the matrix multiplication in mix columns
def mix_math(row, col):

    #array holding individual values to be added at end
    a = [0] * 4
    for i in range(4):
        mix_val = row[i]
        if mix_val == 1:
            a[i] = col[i]
        elif mix_val == 2:
            a[i] = col[i] << 1
            if a[i] > 255:
                a[i]= a[i] ^ 0b100011011
        else:
            a[i] = (col[i] << 1)
            if a[i] > 255:
                a[i]= a[i] ^ 0b100011011
            a[i] = a[i] ^ col[i]
    b = a[0] ^ a[1] ^ a[2] ^ a[3]
    if b > 255: print(b)
    return b

#takes the current state (in this case the 's' or the round) and generates an array for sbox substituion. DOES NOT
#perform operation in place, to facilitate saving of each step for assignment
def sub_bytes(state):
    array = bytearray(16) #empty array to divide individual bytes into

    #finds substitution in sbox
    for i in range(16):
        array[i] = sbox[state[i]]
    #returns new bytearray
    return array

def shift_row(state):
    state_matrix = matrify(state)

    #rolls each row to the left 0,1,2, or 3 based on iteration
    for i in range(4):
        state_matrix[i] = np.roll(state_matrix[i],-i)

    shifted = dematrify(state_matrix)
    return shifted

def mix_col(state):

    state_matrix = matrify(state)
    mixed_row = np.array([0, 0, 0, 0])
    mixed = np.empty((4,4), dtype=int)
    for i in range(4):
        for j in range(4):
            #print(mix_array[i])
            #print(state_matrix[:,j])
            mixed_row[j] = mix_math(mix_array[i],state_matrix[:,j])
        mixed[i]=mixed_row
        #print(mixed_row)
    #print(mixed)
    mixed = dematrify(mixed)
    return mixed

#adds key by XOR key against state
def add_key(state, round):
    current_key = bytearray.fromhex(roundkeys[round])  # current key to bytes
    added = bytearray()
    for a, b in zip(current_key, state):
        temp = a ^ b
        added.append(temp)

    return added


#Round 0 addroundkey to initialize

round[1]['s'] = bytearray() # initialize dict entry to byte array

round[1]['s'] = add_key(bytearray.fromhex(plaintext),0)
#print(round[1]['s'].hex())

for i in range(1,11):
    print(i)
    round[i]['sub'] = sub_bytes(round[i]['s'])
    round[i]['shift'] = shift_row(round[i]['sub'])
    if i < 10:
        round[i]['mix'] = mix_col(round[i]['shift'])
        round[i+1]['s'] = add_key(round[i]['mix'],i)
        #print(round[i+1]['s'].hex())
    else:
        cipher = add_key(round[10]['shift'],i)

print("Cipher: "+cipher.hex())

print("Round 10 State: "+ round[10]['s'].hex())
print("Round 2 Start: "+ round[2]['s'].hex())
print("Round 1 Shift: " + round[1]['shift'].hex())
print("Round 1 Mix: " + round[1]['mix'].hex())
print("Round 1 Sub: " + round[1]['sub'].hex())
print("Round 1 Start: " + round[1]['s'].hex())
