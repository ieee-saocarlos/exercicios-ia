i, sum = 0, 0

for i in range (0, 1000):
 if (i%3==0 or i%5==0):
  sum += i
print("A soma dos múltiplos de 3 e 5 até 1000 é:")
print(f"-->{sum}<--.")
