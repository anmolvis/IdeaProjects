

ip = input("Enter the ip")
ip += '.'
seg_length = 0
segment = 0
for char in ip:
    if char == '.':
        segment += 1
        print("Segment {0} is of length {1}".format(segment, seg_length))
        seg_length = 0
    else:
        seg_length += 1
