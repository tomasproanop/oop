method = input("Geben Sie den Namen einer Methode ein, die Zeichenfolgen ändert, um eine Definition anzuzeigen (z.B. upper): ")

if method == "upper":
    print("Diese Methode wandelt alle Kleinbuchstaben in einem String in Großbuchstaben um und gibt sie zurück.")
elif method ==  "capitalize":
    print("Die Methode capitalize() gibt eine Kopie des ursprünglichen Strings zurück und wandelt das erste Zeichen des Strings in einen Großbuchstaben um, während alle anderen Zeichen des Strings in Kleinbuchstaben umgewandelt werden.")
elif method ==  "swapcase":
    print("Die Methode string swapcase() wandelt alle Großbuchstaben in Kleinbuchstaben und umgekehrt der angegebenen Zeichenfolge um und gibt sie zurück.")
elif method ==  "strip":
    print("Gibt eine Kopie der Zeichenfolge zurück, bei der sowohl führende als auch abschließende Zeichen entfernt wurden, basierend auf dem übergebenen Zeichenfolgenargument.")
elif method ==  "replace":
    print("Gibt eine Kopie der Zeichenfolge zurück, in der alle Vorkommen einer Teilzeichenfolge durch eine andere Teilzeichenfolge ersetzt werden.")
elif method ==  "count":
    print("count() gibt die Anzahl der Vorkommen einer Teilzeichenfolge in der angegebenen Zeichenfolge.")
elif method ==  "isdigit":
    print("Die Methode isdigit() gibt „True“ zurück, wenn alle Zeichen in der Zeichenfolge Ziffern sind, andernfalls gibt sie „False“ zurück. Diese Funktion wird verwendet, um zu prüfen, ob das Argument Ziffern wie 0123456789 enthält.")
elif method ==  "islower":
    print("islower() prüft, ob alle Zeichen in der Zeichenfolge Kleinbuchstaben sind. Wenn die Zeichenfolge mindestens einen Großbuchstaben enthält, wird False zurückgegeben.")
else:
    print("Das ist nicht eine Methode.")

    
# Cindy Sanchez und Tomas Proano
# Das Programm gibt die Definition ab, wenn man einen gültigen Namen einer Methode eingibt. 
