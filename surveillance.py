import subprocess
import re
import notify2

CPU_WARNING=70
MEM_WARNING=247
HD_WARNING=70

#fonction d'alerte
notify2.init("mes alertes")
def alerte(titre, message):
    notification = notify2.Notification(titre, message)
    notification.show()

# calcul de la charge de CPU
cpu_cmd = "top -bn1 | grep 'Cpu(s)'"
cpu_info = subprocess.check_output(cpu_cmd, shell=True, text=True, universal_newlines=True)
cpu_inactivité=re.search(r"(\d,\d) (id)", cpu_info)

#valeur de l'utilisation du cpu en %
cpu_activité = 100 - float(cpu_inactivité.groups()[0].replace(",", "."))

#calcul de la charge RAM
mem_cmd = "free -h | grep 'Mem'"
mem_info = subprocess.check_output(mem_cmd, shell=True, text=True, universal_newlines=True).split()

#valeur de la RAM non utilisée
mem_free = int(mem_info[3].replace("Mi", ""))

#calcul de l'utilisation du disque sda1
HD_cmd = "df -h | grep /dev/sda1"
HD_info = subprocess.check_output(HD_cmd, shell=True, text=True, universal_newlines=True).split()

#utilisation du disque en %
HD_uti = int(HD_info[4].replace("%", ""))

#alertes
if cpu_activité > CPU_WARNING:
    alerte("Utilisation CPU intensive", "Vorte système utilise votre CPU de 80% du temps")

if mem_free < MEM_WARNING:
    alerte("Utilisation RAM intensive", "Vous utiliser plus de 80% de votre RAM")
    
if HD_uti > HD_WARNING:
    alerte("Utilisation Disque intensive", "Vous avez moins de 30% d'espace lirbe sur votre disque dur sda1")

