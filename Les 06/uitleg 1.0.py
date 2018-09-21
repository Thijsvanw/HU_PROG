getallenrij = [2, 4, 6, 8, 10, 9, 7]
zoekgetal=eval(input('geefgetal'))
gevonden = False
for getal in getallenrij:
    if getal == zoekgetal:
        gevonden=True
if gevonden == True:
    print(gevonden)