# -*- coding: utf-8 -*-
import os
lista_caractere='ă,î,â,ș,ț,Ă,Î,Â,Ș,Ț'

cale = "C:\\Users\\aion\\Documents\\Python\\For me\\Duplicate file finder\\fisiere de proba"

for (path,folders,files) in os.walk(cale):
        for folder in folders:
            print folder
        for file in files:
            string = file.decode("Latin-1")
            temp=repr(string)
            if '\\xe2' in temp:
                print string
                print temp
                temp = temp.replace('\\xe2','a')
                print temp
                print os.path.isfile(os.path.join(cale,string.decode("Latin-1")))
                print '\n'                
##                os.rename(os.path.join(cale,),os.path.join(cale,temp))














            
##            print os.path.getsize(os.path.join(path,file))


##string = unicode("café", 'utf8')
##
##print string
##
##string_for_output = string.encode('utf8')
##
##print (string_for_output)
##
##print string


##caractere romanesti CP852


##string = file.replace("ă","a").replace("î","i").replace("â","a").replace("ș","s").replace("ț","t").replace("Ă","A").replace("Î","I").replace("Â","A").replace("Ș","S").replace("Ț","T") AM INCERCAT, NU MERGE!!!
