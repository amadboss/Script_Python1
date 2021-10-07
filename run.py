import os, sys, platform
import netifaces as ni

a_file = open("/etc/os-release")
lines_print = [1, 3, 6] #tableau qui me permet de prendre les ligne concerné de /etc/os-release
print("Os is :", platform.system()) #print de l'OS

for i, line in enumerate(a_file): #Pour chaque ligne dans a_file

  if ( i in lines_print):   #print des information system en fonction du tableau lines_print 

    print(line)
a_file.close()

os.system('touch interface')
if os.path.isfile('interface'):
    os.remove('interface')  # Si le fichier interface existe deja on le supprime
print("La liste des interface reseau est :", os.listdir('/sys/class/net')) #liste les interface dans /sys/class/net

i_file = open("interface", 'a') #ouverture du fichier interface pour ecrire dedant 

for i in os.listdir('/sys/class/net'):
    try: #Recupére les adresse ip et mac des interface et les ecrit dans un fichier (interface)
        ip = ni.ifaddresses("%s"%i)[ni.AF_INET][0]['addr']
        mac = ni.ifaddresses("%s"%i)[17][0]['addr']
        i_file.write("interface %s ip : %s and mac address is %s \r\n" %(i, ip, mac))
        print("interface '%s' ip : %s and mac address is %s" %(i, ip, mac))
    except KeyError: #Si une interface n'a pas d'ip on passe ici pour ignoré l'erreur "KeyError:2" 
        mac = ni.ifaddresses("%s"%i)[17][0]['addr']
        i_file.write("interface %s pas d'ip. L'adresse mac est: %s \r\n" %(i,mac))
        print("%s n'a pas d'adresse ip mais la mac est %s: "%(i, mac))
i_file.close() #fermeture du ficier interface

print("\n\rLs du repertoir courant : ")
os.system('ls .')
print("\n\rcontenue de du fichier interface crée : ")
os.system('cat interface')
