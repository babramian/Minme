from math import floor

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Encode a positive integer to Base 62
# Arguments: 
# --- num: Integer to encode
# --- b: Keeps base conversion rate at 62
def encode62(num, b = 62):
  #if num == 0:
  #  return BASE62[0]

  rem = num % b
  res = BASE62[rem]
  q = floor(num/b)

  while q:
    rem = q % b
    q = floor(q / b)
    res = BASE62[rem] + res

  return res

# Decode a Base 62 numeral to a positive Base 10 integer
# Arguments:
# --- string: String variable containing Base 62 numeral to decode
# --- b: Keeps base conversion rate at 62
def decode62(num, b = 62):

    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + BASE62.find(num[i])
    return res