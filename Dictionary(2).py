print(food[1])
print(food[2])
print(Ayaan["Grade"])
print(Ayaan.keys())
print(Ayaan.values())

print("rice" in food)
if "Hobby" in Ayaan :
        print(Ayaan["Hobby"])

for i in Ayaan.keys():
        print(i,Ayaan[i])

Ayaan["Phone Number"]=12345678

print(Ayaan)

del Ayaan["Phone Number"]

print(Ayaan)

Ayaan["House Number"]=7653

print(Ayaan)

Ayaan["Grade"]=12

print(Ayaan)
