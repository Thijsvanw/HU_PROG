naam = input('wat is jouw naam?')
leeftijd = int(input('hoe oud ben je?'))
if leeftijd < 18:
    print( naam + ',' ' je mag nog niet stemmen')
else: print( naam + "," 'je mag stemmen')