vals = list('tfzbwlyzljylawhzzdvyk')
new_vals = []
new_vals2 = []
for i in vals:
    new_vals.append(ord(i) - 7)
    
for i in new_vals:
    if i < ord('a'):
        new_vals2.append(chr(i + 26))
    else:
        new_vals2.append(chr(i))
        


    
print(''.join(new_vals2))

# import sys

# def main():
#     if len(sys.argv) != 2:
#         print ('Invalid args')
#         return
#     password = sys.argv[1]
#     counter = 0
#     vals = list('tfzbwlyzljylawhzzdvyk')
#     if len(password) != len(vals):
#         print ('incorrect')
#         return
#     while counter < len(password):
#         x = ord(password[counter]) + 7
#         if x > ord('z'):
#             x -= 26
#         if chr(x) != vals[counter]:
#             print ('incorrect')
#             return
#         counter += 1

#     print ('correct')
    
# if __name__ == '__main__':
#     main()  