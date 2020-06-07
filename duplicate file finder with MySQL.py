import os, time, xlsxwriter, pymysql

folders_list = []
files_list = []
lista_ignorare = []
DB_connected = False
cur = ''
db = ''

class Folders:
    folders_total = 1

    def __init__(self, folder, path):
        global folders_list
        self.index = Folders.folders_total
        self.folder = folder
        self.path = path
        folders_list.append(self)
        Folders.folders_total += 1


class Files:
    files_total = 1

    def __init__(self, file, path):
        global files_list
        self.index = Files.files_total
        self.nume_fisier = file
        self.nume_fisier_trunchiat = file[0:len(file) - 4]
        self.path = path.replace('\\','\\\\')
        self.size = ""
        self.size = os.path.getsize(os.path.join(path, self.nume_fisier))
        self.creation_date = time.ctime(os.path.getctime(os.path.join(path, self.nume_fisier)))
        self.modify_date = time.ctime(os.path.getmtime(os.path.join(path, self.nume_fisier)))
        files_list.append(self)
        Files.files_total += 1


def Import(cale):
    global lista_ignorare, files_list
    if DB_connected:
        for (path, folders, files) in os.walk(cale):
            for folder in folders:
                if folder not in lista_ignorare:
                    obiect = len(globals())
                    globals()[obiect] = Folders(folder, path)
            for file in files:
                if path not in lista_ignorare:
                    obiect = len(globals())
                    try:
                        globals()[obiect] = Files(file, path)
                    except Exception as error:
                        print ('A aparut eroarea: ' + str(error))
    scriere_log(str(time.ctime()) + ": Din " + str(cale) + " s-au importat " + str(len(folders_list)) + " foldere")
    scriere_log(str(time.ctime()) + ": Din " + str(cale) + " s-au importat " + str(len(files_list)) + " fisiere")


def remove(cale):
    global lista_ignorare
    lista_ignorare.append(cale)


def incarcare_fisiere():
    remove('F:\\Deea\\back-up andreea\\documente\\proiecte andreea\\FACULTATE\\licenta\\licenta cd')
    remove('F:\\Deea\\back-up andreea\\Foldere de pe desktop\\mesaje 24.05.2010\\inbox all')
    remove('F:\\Deea\\back-up andreea\\kmy\\diverse\\')
    remove('F:\\Deea\\back-up andreea\\documente\\proiecte andreea\\FACULTATE\\an II sem I\\proiect tp sampoane')
    remove('F:\\Deea\\back-up andreea\\documente\\proiecte andreea\\FACULTATE\\an III sem II\\b2b individual')
    remove('F:\\Deea\\back-up andreea\\Foldere de pe desktop\\mesaje 24.05.2010\\outbox all\\2')
    remove('F:\\Deea\\back-up andreea\\Foldere de pe desktop\\mesaje 24.05.2010\\outbox all\\1')
    remove('F:\\Deea\\back-up andreea\\poze bumb\\ionut')
    remove('F:\\Deea\\back-up andreea\\2009 - 2\\sf mihail 2009')
    remove("F:\\Deea\\back-up andreea\\D\\poze\\2009\\2009 - 1")
    remove("F:\\Deea\\back-up andreea\\2009 - 2\\")
    remove("F:\\Deea\\back-up andreea\\2009 - 1\\herastrau noi2009")
    remove("F:\\Deea\\back-up andreea\\D\\poze\\2009\\2009 - 1\\herastrau noi2009")
    remove("F:\\Deea\\back-up andreea\\D\\poze\\2009\\2009 - 1\\21noi2009")
    remove("F:\\Deea\\back-up andreea\\2009 - 1\\luminite 2009")
    remove("F:\\Deea\\back-up andreea\\2009 - 1\\moieciu 19-20 dec 2009")
    remove("F:\\Deea\\back-up andreea\\D\\deskt\\rent a car")
    remove("F:\\Deea\\back-up andreea\\D\\Foldere de pe desktop\\mesaje 24.05.2010\\inbox all")
    remove("F:\\Deea\\back-up andreea\\D\\Foldere de pe desktop\\mesaje 24.05.2010\\outbox all\\1")
    remove("F:\\Deea\\back-up andreea\\D\\Foldere de pe desktop\\mesaje 24.05.2010\\outbox all\\2")
    remove("F:\\Deea\\back-up andreea\\D\\Foldere de pe desktop\\muzica 2012")
    remove("F:\\Deea\\back-up andreea\\D\\Foldere de pe desktop\\Poze album, puzzle\\Poze album Mickey")
    remove("F:\\Deea\\back-up andreea\\D\\ionut- camy\\poze\\bumbu,tzuti moieciu 01,05-08\\Imagini")
    remove("F:\\Deea\\back-up andreea\\D\\ionut- camy\\radoi\\muzica")
    remove("F:\\Deea\\back-up andreea\\D\\poze\\2008\\moeciu 1-5 aug2008\\tel")
    remove("F:\\Deea\\back-up andreea\\Foldere de pe desktop\\mesaje 24.05.2010")
    remove("F:\\Deea\\back-up andreea\\kmy\\poze servici kmy")
    remove("F:\\Deea\\back-up andreea\\2009 - 1\\Padure călugăreni")
    remove('')
    remove('')
    remove('')
    remove('')
    remove('')
    remove('')
    Import("F:\\")


def scriere_log(mesaj):
##    LogFile = open("LogFileDuplicateFileFinder.txt", "a")
##    LogFile.write(mesaj + "\n")
    print (mesaj)
##    LogFile.close()


def conectare_db():
    global DB_connected, cur, db
    try:
        db = pymysql.connect(host="127.0.0.1",
                             user="root",
                             passwd="",
                             db="duplicate_file_finder")
        cur = db.cursor()
        DB_connected = True
        print ('Conectat la DB')
    except Exception as error:
        print (str(error))


def query_without_reply(query):
    global cur, db
    try:
        cur.execute(query)
        db.commit()
    except Exception as error:
        print ('A aparut eroarea: ' + str(error))
        print ('Query-ul incercat a fost: ' + query)


def query_with_reply(query):
    global cur, db
    try:
        cur.execute(query)
        db.commit()
        return cur.fetchall()
    except Exception as error:
        print ('A aparut eroarea: ' + str(error))
        print ('Query-ul incercat a fost: ' + query)


def inserare_fisiere_DB():
    global DB_connected, folders_list, files_list, cur, db
    if DB_connected:
        for obiect in files_list:
            if obiect.nume_fisier != "Thumbs.db":
                try:
                    query = 'INSERT INTO fisier VALUES (default,"{0}","{1}","{2}","{3}","{4}","{5}")'.format(
                        obiect.nume_fisier, obiect.nume_fisier_trunchiat, obiect.path, obiect.size,
                        obiect.creation_date, obiect.modify_date)
                    query_without_reply(query)
                except Exception as error:
                    print ('A aparut eroarea: ' + str(error))
        folders_list = []
        files_list = []


def main():
    conectare_db()
    incarcare_fisiere() #Se ruleaza o singura data!!!
    inserare_fisiere_DB() #Se ruleaza o singura data!!!
    parcurgere_lista_DB()
    query = 'SELECT SUM(run_time) FROM run_times'
    total_time = round (query_with_reply(query)[0][0] / 60)
    print ('Verificarea fisierelor a durat {0} minute'.format(total_time))

def parcurgere_lista_DB():
    global DB_connected

    primul_timp = time.time()

    if DB_connected:
        query = "SELECT max(id_fisier) FROM fisier"
        limit = query_with_reply(query)[0][0] + 1

        query = "SELECT min(id_fisier) FROM fisier"
        cel_mai_mic_id = query_with_reply(query)[0][0]


        for iteratie1 in range(cel_mai_mic_id, limit):
            query = "SELECT * FROM fisier where id_fisier={0}".format(iteratie1)
            temp = query_with_reply(query)[0]
            nume_fisier1 = temp[1]
            path1 = temp[3]
            size1 = temp[4]
            creation_date1 = temp[5]
            modify_date1 = temp[6]
            print ("Suntem la iteratia1: {0} {1}".format(iteratie1, nume_fisier1))

            for iteratie2 in range(iteratie1 + 1, limit):
                query = "SELECT * FROM fisier where id_fisier={0}".format(iteratie2)
                temp = query_with_reply(query)[0]
                nume_fisier2 = temp[1]
                path2 = temp[3]
                size2 = temp[4]
                creation_date2 = temp[5]
                modify_date2 = temp[6]
                Verificare(nume_fisier1, path1, size1, creation_date1, modify_date1, nume_fisier2, path2, size2, creation_date2, modify_date2)

            query = "DELETE FROM fisier WHERE id_fisier = {0}".format(iteratie1)
            query_without_reply(query)

            timp_doi = time.time() #resetare parametru final
            diferenta_timp = timp_doi - primul_timp
            primul_timp = time.time() #resetare parametru initial
            query = 'INSERT INTO run_times values (default,"{0}")'.format(diferenta_timp)
            query_without_reply(query)
            
            

    
    
    print ("Executia a durat: " + str(diferenta_timp) + " secunde")


def Verificare(nume_fisier1, path1, size1, creation_date1, modify_date1, nume_fisier2, path2, size2, creation_date2, modify_date2):
    if nume_fisier1 == nume_fisier2 and size1 == size2:
        query = 'INSERT INTO duplicates VALUES (default,"{0}","{1}","{2}")'.format(path1.replace('\\','\\\\') + '\\\\' + nume_fisier1, path2.replace('\\','\\\\') + '\\\\' + nume_fisier2, 'fisiere identice')
        query_without_reply(query)
        scriere_log(str(time.ctime()) + ": S-au gasit 2 fisiere identice: " + nume_fisier1)
        scriere_log(path1 + '\\' + nume_fisier1)
        scriere_log(path2 + '\\' + nume_fisier2 + "\n")

    elif creation_date1 == creation_date2 and size1 == size2:
        query = 'INSERT INTO duplicates VALUES (default,"{0}","{1}","{2}")'.format(path1.replace('\\','\\\\') + '\\\\' + nume_fisier1, path2.replace('\\','\\\\') + '\\\\' + nume_fisier2, 'fisierele au aceeasi data de creare')
        query_without_reply(query)
        scriere_log(str(time.ctime()) + ": S-au gasit 2 fisiere care au aceeasi data de creare: ")
        scriere_log(path1 + '\\' + nume_fisier1)
        scriere_log(path2 + '\\' + nume_fisier2 + "\n")

    elif modify_date1 == modify_date2 and size1 == size2:
        query = 'INSERT INTO duplicates VALUES (default,"{0}","{1}","{2}")'.format(path1.replace('\\','\\\\') + '\\\\' + nume_fisier1, path2.replace('\\','\\\\') + '\\\\' + nume_fisier2, 'fisierele au aceeasi data de modificare')
        query_without_reply(query)
        scriere_log(str(time.ctime()) + ": S-au gasit 2 fisiere care au aceeasi data de modificare: " + nume_fisier1)
        scriere_log(path1 + '\\' + nume_fisier1)
        scriere_log(path2 + '\\' + nume_fisier2 + "\n")


main()
db.close()
input("Apasa <enter> pentru a iesi")
