idades = []

for i in range(6):
    idade = int  (input(" digite uma idade:"))
    idades.append (idade)

print("as digitadas foram:", idades)
print("a maior idade eh:",max(idades))
print("a menor idade eh:", min(idades))
print("a maior idade eh:", sum (idades)/5)
