# Stap B en Stap C in 1
voetbalclub = input("Wat is de naam van de voetbalclub? ")

# Stap D en Stap E in 1 je laat zien dat het een integer is en dat de input word overuled door de integer
oppervlakte = int(
  input("\n" + "Wat is de oppervlakte van het grasveld in vierkante meter? "))

# Stap F rekensom voor foot
oppervlakteInSquareFoot = oppervlakte * 10.76

# Stap G oppervlakte, voetbalclub en oppervlakte bij elkaar
print("\n" + "De oppervlakte van", voetbalclub, "is", oppervlakte,
      "vierkante meter, dit is", oppervlakteInSquareFoot, "\n"
      "square foot.")

# Stap H van foot naar euro
kosten = oppervlakteInSquareFoot * 0.30

# Stap I de functie round word gebruikt om de kosten af te ronden op 2 decimalen word meteen geprint
print("\n" + "De kosten zijn", round(kosten, 2), "euro.")