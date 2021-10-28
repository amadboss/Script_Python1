import os, sys, platform, subprocess, re

parser = argparse.ArgumentParser(description='Just run the programme Python3 Run.py',
                                add_help=True)
parser.add_argument("-q", action ="store", dest='argument',
                    help="First argument")
output = parser.parse_args()

if (platform.system()in ['Windows']):
  tab = []

  #afficher les info systeme
  print(platform.platform()) 
  print(platform.machine())
  input("Appuyer sur entrée pour continuer")

  #Recuperation des internfaces
  data = subprocess.check_output(['ipconfig','/all']).decode('ISO-8859-1').split('\n')

  #ouverture / création du ficher 
  with open('windows_interface.txt', 'w') as f: 
    for item in data:
      tab.append(item)
      #print(item, file=f)
      #affiche les info de ipconfig de maniére ordonner
      print(item.split('\r')[:-1], file=f)
  #print(tab) 
  print('DOSSIER DANS LE REPERTOIR COURANT :', os.listdir())
  
  #affichage du fichier windows_interface.txt
  fichier = open("windows_interface.txt", "r")
  print (fichier.read())
  fichier.close()#fermeture du fichier interface
  input("Appuyer sur entrée pour continuer")
  #for i in range(50):
   # print(tab[i])
  for i in range(50):
    if re.match("Carte ", tab[i]):
      print(tab[i])
    if re.match("   Adresse IPv4", tab[i]):

      #print(tab[i-10])
      print(tab[i])
  

else :
  
  import netifaces as ni
  a_file = open("/etc/os-release")
  lines_print = [1, 3, 6] #tableau qui me permet de prendre les ligne concerné de /etc/os-release
  print("L'Os est :", platform.system()) #print de l'OS

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

  i_file.close() #fermeture du fichier interface
  print("\n\rFichier présent dans repertoir courant : ")
  #print du repertoir courant et affichage du fichier interface
  os.system('ls .') 
  print("\n\rcontenue de du fichier interface crée : ")
  os.system('cat interface')
