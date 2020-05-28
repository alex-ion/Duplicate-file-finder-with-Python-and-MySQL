import os, time, xlsxwriter, MySQLdb

folders_list=[]
files_list=[]
lista_ignorare=[]
DB_connected = False


class Folders():
    global folders_list
    folders_total=1
    def __init__(self,folder,path):
        global folders_list
        self.index=Folders.folders_total
        self.folder=folder
        self.path=path
        folders_list.append(self)
        Folders.folders_total+=1


class Files():
    global files_list
    files_total=1
    def __init__(self,file,path):
        global files_list
        self.index=Files.files_total
        self.nume_fisier=file
        self.nume_fisier_trunchiat=file[0:len(file)-4]
        self.path=path
        self.size=""
        self.size=os.path.getsize(os.path.join(path,self.nume_fisier))
        self.creation_date = time.ctime(os.path.getctime(os.path.join(path,self.nume_fisier)))
        self.modify_date = time.ctime(os.path.getmtime(os.path.join(path,self.nume_fisier)))
        files_list.append(self)
        Files.files_total+=1


def Import(cale):
    global lista_ignorare, files_list
    for (path,folders,files) in os.walk(cale):
        for folder in folders:
            if folder not in lista_ignorare:
                obiect =len(globals())
                globals()[obiect]=Folders(folder,path)
        for file in files:
            if path not in lista_ignorare:
                obiect =len(globals())
                try:
                    globals()[obiect]=Files(file,path)
                except(Exception) as error:
                    print 'A aparut eroarea ' + str(error)    
    scriere_log(str(time.ctime())+": Din "+str(cale)+" s-au importat "+str(len(folders_list))+" foldere")
    scriere_log(str(time.ctime())+": Din "+str(cale)+" s-au importat "+str(len(files_list))+" fisiere")


def Remove(cale):
    global lista_ignorare
    lista_ignorare.append(cale)

    
def incarcare_fisiere():
    Remove('F:\\Deea\\back-up andreea\\documente\\proiecte andreea\\FACULTATE\\licenta\\licenta cd')
    Remove('F:\\Deea\\back-up andreea\\Foldere de pe desktop\\mesaje 24.05.2010\\inbox all')
    Remove('F:\\Deea\\back-up andreea\\kmy\\diverse\\')
    Remove('F:\\Deea\\back-up andreea\\documente\\proiecte andreea\\FACULTATE\\an II sem I\\proiect tp sampoane')
    Remove('F:\\Deea\\back-up andreea\\documente\\proiecte andreea\\FACULTATE\\an III sem II\\b2b individual')
    Remove('F:\\Deea\\back-up andreea\\Foldere de pe desktop\\mesaje 24.05.2010\\outbox all\\2')
    Remove('F:\\Deea\\back-up andreea\\Foldere de pe desktop\\mesaje 24.05.2010\\outbox all\\1')
    Remove('F:\\Deea\\back-up andreea\\poze bumb\\ionut')
    Remove('F:\\Deea\\back-up andreea\\2009 - 2\\sf mihail 2009')
    Remove("F:\\Deea\\back-up andreea\\D\\poze\\2009\\2009 - 1")
    Remove("F:\\Deea\\back-up andreea\\2009 - 2\\")
    Remove("F:\\Deea\\back-up andreea\\2009 - 1\\herastrau noi2009")
    Remove("F:\\Deea\\back-up andreea\\D\\poze\\2009\\2009 - 1\\herastrau noi2009")
    Remove("F:\\Deea\\back-up andreea\\D\\poze\\2009\\2009 - 1\\21noi2009")
    Remove("F:\\Deea\\back-up andreea\\2009 - 1\\luminite 2009")
    Remove("F:\\Deea\\back-up andreea\\2009 - 1\\moieciu 19-20 dec 2009")
    Remove("F:\\Deea\\back-up andreea\\D\\deskt\\rent a car")
    Remove("F:\\Deea\\back-up andreea\\D\\Foldere de pe desktop\\mesaje 24.05.2010\\inbox all")
    Remove("F:\\Deea\\back-up andreea\\D\\Foldere de pe desktop\\mesaje 24.05.2010\\outbox all\\1")
    Remove("F:\\Deea\\back-up andreea\\D\\Foldere de pe desktop\\mesaje 24.05.2010\\outbox all\\2")
    Remove("F:\\Deea\\back-up andreea\\D\\Foldere de pe desktop\\muzica 2012")
    Remove("F:\\Deea\\back-up andreea\\D\\Foldere de pe desktop\\Poze album, puzzle\\Poze album Mickey")
    Remove("F:\\Deea\\back-up andreea\\D\\ionut- camy\\poze\\bumbu,tzuti moieciu 01,05-08\\Imagini")
    Remove("F:\\Deea\\back-up andreea\\D\\ionut- camy\\radoi\\muzica")
    Remove("F:\\Deea\\back-up andreea\\D\\poze\\2008\\moeciu 1-5 aug2008\\tel")
    Remove("F:\\Deea\\back-up andreea\\Foldere de pe desktop\\mesaje 24.05.2010")
    Remove("F:\\Deea\\back-up andreea\\kmy\\poze servici kmy")
    Remove('')
    Remove('')
    Remove('')
    Remove('')
    Remove('')
    Remove('')
    Import("F:\\")


def scriere_log(mesaj,):
    global workbook, worksheet, row
    LogFile=open("LogFileDuplicateFileFinder.txt","a")
    LogFile.write(mesaj+"\n")
    print mesaj
    LogFile.close()   


def conectare_db():
    global DB_connected, cur, db
    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="root",
                             passwd="",
                             db="duplicate_file_finder")
        cur = db.cursor()
        DB_connected = True
        print 'Conectat la DB'
    except(Exception) as error:
        print str(error)


def query_without_reply(query):
    global cur,db
    try:
        cur.execute(query)
        db.commit()
    except(Exception) as error:
        print 'A aparut eroarea ' + str(error)
        print 'Query-ul incercat a fost: '+query


def query_with_reply(query):
    global cur,db
    try:
        cur.execute(query)
        db.commit()
        return cur.fetchall()
    except(Exception) as error:
        print 'A aparut eroarea ' + str(error)
        print 'Query-ul incercat a fost: '+query
        

def inserare_fisiere_DB():
    global DB_connected, folders_list, files_list, cur, db
    if DB_connected == True:
        query = ''
        for obiect in files_list:
            if obiect.nume_fisier !="Thumbs.db":
                try:
                    query = 'INSERT INTO fisier VALUES (default,"{0}","{1}","{2}","{3}","{4}","{5}")'.format(obiect.nume_fisier, obiect.nume_fisier_trunchiat, obiect.path, obiect.size, obiect.creation_date, obiect.modify_date)
                    query_without_reply(query)
                except(Exception) as error:
                    print 'A aparut eroarea ' + str(error)                
        folders_list=[]
        files_list=[]

        
def main():
##    incarcare_fisiere() #Se ruleaza o singura data!!!
    conectare_db()
##    inserare_fisiere_DB() #Se ruleaza o singura data!!!
    parcurgere_lista_DB()


def parcurgere_lista_DB():
    query = "SELECT max(id_fisier) FROM fisier"
    limit = query_with_reply(query)[0][0] + 1

    query = "SELECT min(id_fisier) FROM fisier"
    cel_mai_mic_id = query_with_reply(query)[0][0]

    primul_timp=time.time()

    for iteratie1 in range(cel_mai_mic_id,limit):
        query = "SELECT * FROM fisier where id_fisier={0}".format(iteratie1);
        temp = query_with_reply(query)[0]
        id_fisier1 = temp[0]
        nume_fisier1 = temp[1]
        nume_fisier_trunchiat1 = temp[2]
        path1 = temp[3]
        size1 = temp[4]
        creation_date1 = temp[5]
        modify_date1 = temp[6]
        print "Suntem la iteratia1: {0} {1}".format(iteratie1,nume_fisier1)

        for iteratie2 in range(iteratie1 + 1,limit):
##            print "Suntem la iteratia2: {0}".format(iteratie2)
            query = "SELECT * FROM fisier where id_fisier={0}".format(iteratie2);
            temp = query_with_reply(query)[0]
            id_fisier2 = temp[0]
            nume_fisier2 = temp[1]
            nume_fisier_trunchiat2 = temp[2]
            path2 = temp[3]
            size2 = temp[4]
            creation_date2 = temp[5]
            modify_date2 = temp[6]
            Verificare(id_fisier1, nume_fisier1, nume_fisier_trunchiat1, path1, size1, creation_date1, modify_date1, id_fisier2, nume_fisier2, nume_fisier_trunchiat2, path2, size2, creation_date2, modify_date2)
            
        query = "DELETE FROM fisier WHERE id_fisier = {0}".format(iteratie1)
        query_without_reply(query)
        
    timp_doi=time.time()
    diferenta_timp=timp_doi-primul_timp
    print "Executia a durat: " + str(diferenta_timp) + " secunde"

    
def Verificare(id_fisier1, nume_fisier1, nume_fisier_trunchiat1, path1, size1, creation_date1, modify_date1, id_fisier2, nume_fisier2, nume_fisier_trunchiat2, path2, size2, creation_date2, modify_date2):
    if nume_fisier1 == nume_fisier2 and size1 == size2:
        scriere_log(str(time.ctime())+": S-au gasit 2 fisiere identice: "+nume_fisier1)
        scriere_log(path1+'\\'+nume_fisier1)
        scriere_log(path2+'\\'+nume_fisier2+"\n")
        
    elif creation_date1== creation_date2 and size1 == size2:
        scriere_log(str(time.ctime())+": S-au gasit 2 fisiere care au aceeasi data de creare: ")
        scriere_log(path1+'\\'+nume_fisier1)
        scriere_log(path2+'\\'+nume_fisier2+"\n")

    elif modify_date1 == modify_date2 and size1 == size2:
        scriere_log(str(time.ctime())+": S-au gasit 2 fisiere care au aceeasi data de modificare: "+nume_fisier1)
        scriere_log(path1+'\\'+nume_fisier1)
        scriere_log(path2+'\\'+nume_fisier2+"\n")

##    elif nume_fisier_trunchiat1 in nume_fisier_trunchiat2:
##        scriere_log(str(time.ctime())+": S-au gasit 2 fisiere care au aproximativ acelasi nume: "+nume_fisier_trunchiat1)
##        scriere_log(path1+'\\'+nume_fisier1)
##        scriere_log(path2+'\\'+nume_fisier2+"\n")
##        
##    elif nume_fisier_trunchiat2 in nume_fisier_trunchiat1:
##        scriere_log(str(time.ctime())+": S-au gasit 2 fisiere care au aproximativ acelasi nume: "+nume_fisier_trunchiat2)
##        scriere_log(path1+'\\'+nume_fisier1)
##        scriere_log(path2+'\\'+nume_fisier2+"\n")
        

main()
db.close()
