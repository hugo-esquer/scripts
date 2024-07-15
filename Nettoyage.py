import os

def nettoyage_systeme():
    commandes = [
        "sudo rm -rf /tmp/*",
        "sudo rm -rf /var/tmp/*",
        "sudo rm -rf /var/cache/*",
        "rm -rf /home/hugo/.cache/*"
        "sudo apt clean",
        "sudo apt autoremove -y",
        "sudo journalctl --vacuum-time=1d"
    ]

    for commande in commandes:
        try:
            print(f"Exécution de la commande : {commande}")
            os.system(commande)
        except Exception as e:
            print(f"Erreur de la commande {commande} : {e}" )

if __name__ == "__main__":
    nettoyage_systeme()
            