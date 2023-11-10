import base64

def lire_et_decoder_fichier(input_file, output_file):
    with open(input_file, 'r') as fichier_entree:
        lignes = fichier_entree.readlines()

    resultats = []

    for ligne in lignes:
        elements = ligne.split()
        if len(elements) >= 3:
            contenu_base64 = elements[2]
            contenu_decode = base64.b64decode(contenu_base64).decode('utf-8')
            resultats.append(contenu_decode)

    with open(output_file, 'w') as fichier_sortie:
        fichier_sortie.write('\n'.join(resultats))

# Utilisation de la fonction avec les noms de fichiers d'entrée et de sortie
fichier_entree = "input_file.txt"
fichier_sortie = "output_file.txt"

lire_et_decoder_fichier(fichier_entree, fichier_sortie)
