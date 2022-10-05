teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "

rulergo = "\n123456789012345678901234567890123456789012345678901234567890\n"
rulermid = "000000000111111111122222222223333333333444444444455555555556\n"
rulerend = "....:....!....:....!....:....!....:....!....:....!....:....!\n"
ruler = rulergo + rulermid + rulerend

charx = "'"

countx = (teststring.count(charx))

countx = 5

countxstr = str(countx); countxstr = countxstr.zfill(2)

countxstr = str(countx).zfill(2)

startx =("Sonderzeichen")

startx = startx.ljust(19," ")

footerx = "ist so oft vertreten"
delimitter = ":"

footerx = footerx.center(29, " ")

out = startx + charx + footerx + delimitter + countxstr

print(ruler)

print(out)

columns = 9*"0"+10*"1"+10*"2"+10*"3"+10*"4"+10*"5"+"6"
columns2 = 6*"1234567890"
print("\n" + rulerend + columns + "\n" + columns2)