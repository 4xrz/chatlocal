from flask import Flask
from kvsqlite.sync import Client
import random
from time import sleep

c = Client("chats.hex")
accs = Client("accounts.hex")

app = Flask('app')

@app.route('/setmessage/<fr>/<messagee>')
def setm(fr,messagee):
    ss='qwertyuiopasdfghjklzxcvbnm'
    sss='1234567890'
    if fr:
        gt = c.get('dmj')
        #mg = f'رسالة من : {fr}\nالرسالة : {messagee}'
        jj = f'{gt}\n\n{f'رسالة من : {fr}\nالرسالة : {messagee}'}'
        if c.get('dmj') ==None:
            c.set('dmj',f'رسالة من : {fr}\nالرسالة : {messagee}')
            return 'Done !'
        else:
            c.set('dmj',jj)
            return 'Done !'


@app.route('/getmessage/v1')
def sgtm():
    return c.get('dmj')

@app.route('/del')
def de():
    if c.get('dmj') ==None:
        return 'انت غبي؟ ماكو شي بالداتا بيس! غبي'
    else:
        c.delete('dmj')
        return 'The Del Was Done :) '

app.run(host='0.0.0.0', port=8080)
