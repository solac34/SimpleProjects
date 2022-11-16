import random
import string
import pyperclip

def take_url():
    url = str(input("url:"))
    return url #takes url from user

def shortener(url):
    short_part = str()
    i = 0
    alphabet_list=[]
    while i<6:
        lonom = random.randint(0,3)
        short_url = str()
        if lonom == 0:
            short_part+= str(random.randint(0,9))
        elif lonom==1:
            short_part += string.ascii_lowercase[random.randint(0,25)]
        elif lonom==2:
            short_part += string.ascii_uppercase[random.randint(0,25)]
        i+=1
    short_url = f'ac.tech/s{short_part}'

    with open("shortener_db",'r',encoding='utf-8') as file:
        print(file.readlines())
        for line in file:
            line = line.strip('\n')
            item, url_auth = line.split(",",1)
            if item == short_url:
                shortener(take_url())
            my_list = url_auth
            if url_auth == url:
                print(f"""
This url is already in use!
shortener version of this url: {item}""")
                shortener(take_url())
    with open('shortener_db','a',encoding='utf-8') as f2:
        f2.write(short_url)
        f2.write(',')
        f2.write(url)
        f2.write('\n')
        return short_url
def quit_func():
    quit_ask = str(input("Would you shorten new url?(type y for creating new):"))
    if quit_ask.lower() == 'y':
        app()
    else:
        return 'quit'

def app():
    while True:
        shortened_url = shortener(take_url())
        ask_copy = str(input("type 'c' or 'copy' to copy the shortened version."))
        if ask_copy.lower() == 'c' or ask_copy.lower() == 'copy':
            pyperclip.copy(shortened_url)
        quit_or_print = str(input('Would you like to print database,create a new password or quit?:(p to print-c to new):'))
        if quit_or_print.lower() == 'p':
            with open("shortener_db", 'r', encoding='utf-8', ) as f3:
                step = 1
                for item in f3:
                    item = item.strip('\n')
                    short_ver, normal = item.split(',', 1)
                    print(f"Url-{step}:{normal}")
                    print(f"Shorter Url - {step}:{short_ver}")
                    step += 1
        elif quit_or_print != 'c':
            break
        if quit_func() == 'quit':
            break
app()




