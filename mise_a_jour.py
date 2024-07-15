import subprocess

def run_command(command):
    try:
        result=subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erreur dans la commande {command}")
        print(e.stderr)
        return None
try:
    print("Mise a jour en cours...")
    run_command(["sudo", "apt", "update"])

    noyau_disponible = run_command(["sudo", "apt", "list", "--upgradable"])

    if "linux-image" in noyau_disponible:
        print("Mise à jour du Noyau disponible, mise à jour en cours...")
        run_command(["sudo", "apt", "upgrade", "-y", "linux-image_generic"])

        print("Redémarage nécessaire ...")
        run_command(["sudo", "reboot"])

    else:
        print("Pas de mise à jour du noyau disponible")

    print("Mise à jour des paquets")
    run_command(["sudo", "apt", "upgrade", "-y"])

    print("Mise à ajour terminé.")

except:
    print("Erreur dans la mise à jour")


# cmd_maj = "sudo apt update && sudo apt upgrade -y"
# try:
#     maj = subprocess.run(cmd_maj, shell=True, check=True, text=True, capture_output=True)
# except subprocess.CalledProcessError as e:
#     print("Erreur de la mise à jour")
#     print(e.stderr)

# if "linux-image-amd64" in noyau_disponible.stdout:
#     print("mise à jour disponible")
# else:
#     print("pas de mise à jour")