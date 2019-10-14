datoteka = open("besedilo.txt")
vsebina_datoteke = datoteka.read()

print('To je vsebina datoteke:')
print('"' + vsebina_datoteke + '"')

datoteka.close()


datoteka = open("besedilo.txt", "a")
datoteka.write("To je nova vsebina datoteke\n")
datoteka.close()