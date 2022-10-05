#M#K# - Milestone5 TestJoin.py
#OK     

#Zeichenlinieal fuer 60 Zeichen mit Folienueberschrift 1er=. 5er=: 10er=!
rulergo = "\n123456789012345678901234567890123456789012345678901234567890\n"
rulerend = "....:....!....:....!....:....!....:....!....:....!....:....!\n"
ruler = rulergo + rulerend

print(rulergo + rulerend)

#<milestone5-06-join.ppt #4>
#<->str = trennzeichen.join(Aufzählung)
#<--
#<--wortliste = ['Axel', 'Elke', 'Martin']
#<--trennzeichen = '#'
#<--ergebnis = trennzeichen.join(wortliste)
#<--print(ergebnis)
#<--
#-->Axel#Elke#Martin
#</milestone5-06-join.ppt #4>

wortliste = ['Axel', 'Elke', 'Martin']
trennzeichen = '#'
ergebnis = trennzeichen.join(wortliste)
print(ergebnis)

print(ruler)

#<milestone5-06-join.ppt #5>
#<--
#<--zeichenkette = "abcd"
#<--trennzeichen = '#'
#<--ergebnis = trennzeichen.join(zeichenkette)
#<--print(ergebnis)
#<--
#-->a#b#c#d
#</milestone5-06-join.ppt #5>

zeichenkette = "abcd"
trennzeichen = '#'
ergebnis = trennzeichen.join(zeichenkette)
print(ergebnis)

print(ruler)

#<milestone5-06-join.ppt #6>
#<--
#<--wortliste = ['Axel', 'Elke', 'Martin']
#<--trennzeichen = ' #123# '
#<--ergebnis = trennzeichen.join(wortliste)
#<--print(ergebnis)
#<--
#-->Axel #123# Elke #123# Martin
#</milestone5-06-join.ppt #6>

wortliste = ['Axel', 'Elke', 'Martin']
trennzeichen = ' #123# '
ergebnis = trennzeichen.join(wortliste)
print(ergebnis)

print(ruler)

#<milestone5-06-join.ppt #7>
#<--
#<--deutschenglisch = { 'null': 'zero', 'eins': 'one' }
#<--trennzeichen = '#'
#<--print(trennzeichen.join(deutschenglisch))
#<--
#-->null#eins
#</milestone5-06-join.ppt #7>

deutschenglisch = { 'null': 'zero', 'eins': 'one' }
trennzeichen = '#'
print(trennzeichen.join(deutschenglisch))

###Achtung in diesem Block folgt eine FM
#print("\nEs folgt eine Fehlermeldung weil der Inhalt numerisch ist:")
#print("FM: TypeError: sequence item 0:")
#woerterbuch = {0: 'null', 1: 'eins' }
#trennzeichen = '#'
#print(trennzeichen.join(woerterbuch))

print(ruler)

#M#K# Eigenes Beispiel
domainip = { 'Only4Demo.de': '10.0.0.0', 'cloud4Demo.de': '192.168.0.0' }
delim = '<-->'
print(delim.join(domainip))

print(ruler)











