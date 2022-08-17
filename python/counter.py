googel = []
len = 10

for i in range(len):
  googel.append(0)

while googel[0] != 9:
  for i in range(len-1,-1,-1):
    if googel[i] != 9:
      googel[i] += 1
      break
    googel[i] = 0