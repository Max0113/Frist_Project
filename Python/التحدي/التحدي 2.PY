# === Calcul de la moyenne de sélection pour les écoles supérieures (ex: ENSA) ===

# Demander les notes du candidat
national = float(input("Entrez la note du baccalauréat national (/20) : "))
regional = float(input("Entrez la note du baccalauréat régional (/20) : "))

# Calcul de la moyenne de sélection selon le barème : 75% national + 25% régional
moyenne_selection = (national * 0.75) + (regional * 0.25)

# Affichage du résultat
print(f"La moyenne de sélection est : {moyenne_selection:.2f}")


