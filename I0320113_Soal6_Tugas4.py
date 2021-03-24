a = 4
b = 11

# bitwise OR (|)
c = a | b
print('nilai :', a,', binary: ', format(a,'08b'))
print('nilai :', b,', binary: ', format(b,'08b'))
print('nilai : ', c, ', binary :', format(c,'08b'))

# Bitwise right shift (>>)
c = a >> b
print('nilai :', a,', binary: ', format(a,'08b'))
print('nilai :', b,', binary: ', format(b,'08b'))
print('nilai : ', c, ', binary :', format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b
print('nilai :', a,', binary: ', format(a,'08b'))
print('nilai :', b,', binary: ', format(b,'08b'))
print('nilai : ', c, ', binary :', format(c,'08b'))

# bitwise NOT (~)
c = ~a
print('nilai :', a,', binary: ', format(a,'08b'))

print('nilai : ', c, ', binary :', format(c,'08b'))

# Bitwise AND (&)
c = b & a
print('nilai :', b,', binary: ', format(b,'08b'))
print('nilai :', a,', binary: ', format(a,'08b'))
print('nilai : ', c, ', binary :', format(c,'08b'))
