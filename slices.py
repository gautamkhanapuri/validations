import sys
a = 'abcdefghij'

def slicesarr(a, step=None):
  if step:
    print("String: %s, length: %d, with step=%d" % (a, len(a), step))
  else:
    print("String: %s, length: %d" % (a, len(a)))
  print(" " + '+---' * len(a)+ '+')
  print(' ' + ''.join([ '| ' + c + ' ' for c in a]) + '|')
  print(" " + '+---' * len(a)+ '+')
  print(' ' + ''.join([ '%-4d' % c for c in range(len(a)+1)]))
  print('' + ''.join([ '%-4d' % c for c in range(-1 * len(a), 0)]))
  print()

if len(sys.argv) > 1:
  a = sys.argv[1]

print("#" * 60)
slicesarr(a, step=-1)

print("When Start is given >=0, and step is -1 and end is not given")
for i in range(len(a)+2):
  print("slice: a[%d::-1] ==> %s" % (i, a[i::-1]))
print("Conclusion: It will go backwards from the given positive index till start of string")
print("*" * 50)

print("When Start is given <0 , and step is -1 and end is not given")
print("First element with negative index is len(a) * -1 = %d * -1 = %d" % (len(a), len(a)*-1))
for i in range(len(a)+2, 0, -1):
  print("slice: a[-%d::-1] ==>\t%s" % (i, a[-i::-1]))
print("Conclusion: It will go backwards from the negative index till start of string")
print("*" * 50)

print("When End is given >=0, and step is -1 and start is not given")
for i in range(len(a)+2):
  print("slice: a[:%d:-1] ==>\t%s" % (i, a[:i:-1]))
print("Conclusion: It will go backwards from the negative index -1 till the given positive index of string")
print("*" * 50)

print("When End is given <0 , and step is -1 and start is not given")
print("First element with negative index is len(a) * -1 = %d * -1 = %d" % (len(a), len(a)*-1))
for i in range(len(a)+2, 0, -1):
  print("slice: a[:-%d:-1] ==>\t%s" % (i, a[:-i:-1]))
print("Conclusion: It will go backwards from the negative index -1 till the given negative index of string")
print("*" * 50)


print("#" * 60)
slicesarr(a, step=1)

print("When Start is given >=0, and step is 1 and end is not given")
for i in range(len(a)+2):
  print("slice: a[%d::1] ==> %s" % (i, a[i::1]))
print("Conclusion: It will go forward from the given positive index till end of string")
print("*" * 50)

print("When Start is given <0 , and step is 1 and end is not given")
print("First element with negative index is len(a) * -1 = %d * -1 = %d" % (len(a), len(a)*-1))
for i in range(len(a)+2, 0, -1):
  print("slice: a[-%d::1] ==>\t%s" % (i, a[-i::1]))
print("Conclusion: It will go forward from the negative index till end of string")
print("*" * 50)

print("When End is given >=0, and step is 1 and start is not given")
for i in range(len(a)+2,-1,-1):
  print("slice: a[:%d:1] ==>\t%s" % (i, a[:i:1]))
print("Conclusion: It will go forward from start of string to the given positive index of string")
print("*" * 50)

print("When End is given <0 , and step is 1 and start is not given")
print("First element with negative index is len(a) * -1 = %d * -1 = %d" % (len(a), len(a)*-1))
for i in range(1,len(a)+2):
  print("slice: a[:-%d:1] ==>\t%s" % (i, a[:-i:1]))
print("Conclusion: It will go forward from start of string to the given negative index of string")
print("*" * 50)

print("#" * 60)
print("Observe these ")
slicesarr(a)

for i in range(1,len(a)+4):
  print("slice: a[%d:-%d:1] ==>\t%s" % (i, i, a[i:-i:1]))

print("*" * 50)
slicesarr(a)

for i in range(1,len(a)+4):
  print("slice: a[-%d:%d:1] ==>\t%s" % (i, i, a[-i:i:1]))

print("#" * 60)
print("Observe these ")
slicesarr(a)

for i in range(1,len(a)+4):
  print("slice: a[%d:-%d:-1] ==>\t%s" % (i, i, a[i:-i:-1]))

print("*" * 50)
slicesarr(a)

for i in range(1,len(a)+4):
  print("slice: a[-%d:%d:-1] ==>\t%s" % (i, i, a[-i:i:-1]))

print("*" * 50)
slicesarr(a)

print("Reversing by slices..")
print("Reverse: a[len(a)-1::-1]  ==> a[%d::-1] ==> %s" % (len(a)-1, a[len(a)-1::-1]))
print("Reverse: a[len(a)::-1]  ==> a[%d::-1] ==> %s" % (len(a), a[len(a)::-1]))
print("Reverse: a[len(a)+1::-1]  ==> a[%d::-1] ==> %s" % (len(a)+1, a[len(a)+1::-1]))
print("Reverse: a[-1::-1]  ==> a[%d::-1] ==> %s" % (-1, a[-1::-1]))
print("Reverse: a[:-1*len(a)-1:-1]  ==> a[:%d:-1] ==> %s" % (-1*len(a)-1, a[:-1*len(a)-1:-1]))
print("Reverse: a[:-1*len(a)-2:-1]  ==> a[:%d:-1] ==> %s" % (-1*len(a)-2, a[:-1*len(a)-2:-1]))
print("Reverse: Extended Slice --- a[::-1]  ==> a[::-1] ==> %s" %  a[::-1])
