
def divi(x, y, fr=True):
  # if divsor = 0
  if y == 0:
    raise ZeroDivisionError("Cannot divide by 0")

  if x == 0:
    return 0, 0
  q = 0
  # fractional
  if abs(x) < abs(y) and fr == True:
    x *= 10
    if x*y > 0:
      if x < 0:
        x *= -1
        y *= -1
        while x >= y:
          x -= y
          q += 1
        return q, -x
      while x >= y:
        x -= y
        q += 1
      return q, x
    else:
      if x <0:
        x *= -1
        while x >= y:
          x -= y
          q += 1
        return -q, -x
      else:
        y *= -1
        while x >= y:
          x -= y
          q += 1
        return -q, x
  else:
    if x*y > 0:
      if x < 0:
        x *= -1
        y *= -1
        while x >= y:
          x -= y
          q += 1
        return q, -x
      while x >= y:
        x -= y
        q += 1
      return q, x
    else:
      if x <0:
        x *= -1
        while x >= y:
          x -= y
          q += 1
        return -q, -x
      else:
        y *= -1
        while x >= y:
          x -= y
          q += 1
        return -q, x

# def plain_divide(x, y, digits=10):
#   if x == 0 or y == 0:
#     return 0.0, 0
#   ipart, x = divi(x,y,False)
#   if x == 0:
#     return float(str(ipart) + '.0'), x
#   fpart = '.'
#   while digits > 0:
#     fr, x = divi(x, y, True)
#     # print(fr)
#     fpart += str(fr)
#     # print(fpart)
#     # print(digits)
#     # print('#' * 10)
#     if x == 0:
#       break
#     digits -= 1
#   return float(str(ipart) + fpart), x


def plain_divide(x, y, digits=10):
  digits = int(digits)
  if digits < 0:
    digits *= -1
    print("Digits cannot be a negative number")
  if digits > 15:
    digits = 15
    print("Maximum of 15 decimal place are allowed after the decimal point.")
  ipart, x = divi(x, y, False)
  if digits == 0:
    return ipart, x
  if x == 0:
    if ipart == 0:
      return 0.0, 0
    return float(str(ipart) + '.0'), x
  fpart = '.'
  while digits > 0:
    x = abs(x)
    fr, x = divi(x, y, True)
    # print(fr)
    fr = abs(fr)
    fpart += str(fr)
    # print(fpart)
    # print(digits)
    # print('#' * 10)
    # if x == 0:
    #   break
    digits -= 1
  return float(str(ipart) + fpart), x

print(plain_divide(1222, 9964, 10))
print()
def find_recurring(a):
  recur = None
  for i in range(0,len(a)-1):
    for j in range(i+1, len(a)-1):
      orig = a[i:j]
      cnt = 0
      for k in range(j, len(a)-1,len(orig)):
        mat = a[k:k+len(orig)]
        if orig == mat:
          # print("i=", i, ", ", orig, "==>", mat, ",k=", k)
          cnt += 1
        else:
          break
      else:
        if cnt > 0:
          recur = orig
          # print("i=", i, ", ", orig, "==>", mat, ",cnt=", cnt)
          # print('#' * 10)
          break
    if recur:
      break
  return recur


if __name__ == '__main__':
  import sys
  x = 22
  y = 7
  d = 5
  if len(sys.argv) > 2:
    x = int(sys.argv[1])
    y = float(sys.argv[2])
  if len(sys.argv) > 3:
    d = int(sys.argv[3])
  res,remainder = plain_divide(x, y, d)
  print(res)
  if remainder:
    res = str(res)
    recur = find_recurring(res[res.index('.')+1:])
    print(recur)
