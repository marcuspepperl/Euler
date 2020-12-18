k=1
for i in range(1,301):
  for j in range(i+1,501):
      k=1000-i-j
      if i**2+j**2==k**2:
        print(i*j*k)
        break
print('Done')
