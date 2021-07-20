from requests import post
from bs4 import BeautifulSoup
from os import system
from webbrowser import open

def getRandemail(jml):
    url = f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={jml}"
    source = post(url=url)
    soup = BeautifulSoup(source.text, "html.parser")
    soup1 = soup.text
    soup1 = soup1[1:-1]
    soup1 = soup1.split(',')
    for i in range(len(soup1)):
        print(f"{i+1}. {soup1[i][1:-1]}")

def daftarDomain():
    url = f"https://www.1secmail.com/api/v1/?action=getDomainList"
    source = post(url=url)
    soup = BeautifulSoup(source.text, "html.parser")
    soup1 = soup.text
    soup1 = eval(soup1)
    return soup1

def fetchingMail(username,domain,id):
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={id}"
    source = post(url=url)
    soup = BeautifulSoup(source.text, "html.parser")
    soup = soup.text
    isi = eval(soup)
    kunci = ['id','from','subject','date','textBody']
    print('='*25)
    for i in kunci:
        print(f'{i} : {[isi[i]]}')
    if isi['attachments'] != []:
        print("attachments".upper)
        for idx,nilai in enumerate (isi['attachments']):
            print(f'{idx+1}. {nilai}')
    else:
        print('tidak ada attachments')
    print('='*25,'\n')

def downloadAttachments(username, domain, id, namefile):
    url = f"https://www.1secmail.com/api/v1/?action=download&login={username}&domain={domain}&id={id}&file={namefile}"
    source = open(url)

def checkMailbox(username, domain):
    while True:
        if username == '0':
            break
        else:
            print(f"{5*'='}Check MailBox{5*'='}")
            url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}"
            source = post(url=url)
            soup = BeautifulSoup(source.text, "html.parser")
            soup = soup.text
            if soup == '':
                print("Tidak ada email")
                break
            else:
                soup = eval(soup)
                jum = len(soup)
                for soup1 in soup:
                    print(f"Email: {jum}\nfrom: {soup1['from']}\ndate: {soup1['date']}")
                    jum -= 1
                choice = int(input("Choose your choice (Tekan 0 untuk kembali): "))
                if choice == 0:
                    break
                else:
                    system('clear')
                    fetchingMail(username, domain, (soup[choice-1]['id']))

if __name__ == "__main__":
    menus = ['Get random mail','list domain','Check mailBox','Exit']
    while True:
        system('clear')
        print(f"{5*'='}MENUS{5*'='}")
        for i, n in enumerate(menus):
            print(f'{i+1}. {n}')
        choice = int(input("Silahkan pilih menu: "))
        if choice == 1:
            system('clear')
            print(f"{5*'='}Random Email{5*'='}")
            jml = int(input("Masukkan jumlah yang diinginkan: "))
            getRandemail(jml)
            input()
        elif choice == 2:
            system('clear')
            dom = daftarDomain()
            print(f"{5*'='}Daftar Domain{5*'='}")
            for i in range(len(dom)):
                print(f"{i+1}. {dom[i]}")
            input()
        elif choice == 3:
            system('clear')
            print(f"{5*'='}Check MailBox{5*'='}")
            username = str(input("Masukkan username anda (Tekan 0 untuk kembali): "))
            dom = daftarDomain()
            print('Pilih domain ke berapa:')
            for i in range(len(dom)):
                print(f"{i+1}. {dom[i]}")
            domain = str(input("Input domain (Tekan enter skip, default = esiix.com): "))
            if domain == '':
                domain = 'esiix.com'
            else:
                domain = dom[(int(domain)-1)]
            system('clear')
            checkMailbox(username=username, domain=domain)
        elif choice == 4:
            system('clear')
            break