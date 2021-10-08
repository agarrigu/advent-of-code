# Day 4 - Parts 1 and 2
import hashlib

key = ''
i = 0 #counter
five_zero_index = six_zero_index =  0

# Loop until criteria met
while True:
  i += 1
  hash = hashlib.md5(key + str(i)).hexdigest()

  if not five_zero_index and hash.startswith('0' * 5):
    five_zero_index = i
  if not six_zero_index and hash.startswith('0' * 6):
    six_zero_index = i

  # exit
  if (five_zero_index and six_zero_index):
    break

# Print answers
print ("Five zero index is:", five_zero_index)
print ("Six zero index is:", six_zero_index)
