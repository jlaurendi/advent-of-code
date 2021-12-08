import math
n = int(raw_input("Input n: "))
k = math.ceil((math.sqrt(n)-1)/2)*2+1
j = math.floor(k/2)
i = (k**2-(k-2)**2)/4

print("n: "+str(n))
print("k: "+str(k))
print("j: "+str(j))
print("i: "+str(i))
possible_distances_to_corner = [
  math.fabs(k**2 - n),
  math.fabs(k**2 - n - i),
  math.fabs(k**2 - n - 2*i),
  math.fabs(k**2 - n - 3*i),
  math.fabs(k**2 - n - 4*i) 
]
cd = min(possible_distances_to_corner)
print(possible_distances_to_corner)
print(cd)
distance = j + math.floor(i/2) - cd

print(distance) 
