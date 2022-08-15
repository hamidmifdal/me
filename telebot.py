import requests
def msg():
    TOKEN = "5501495930:AAFdc-5WHgPAhNELTWcRzY_rqmj81x7g3F0"
    chat_id = "1966259244"
    text =  "hello hamid and coffee time hamid"
    url = 'https://api.telegram.org/bot'+ TOKEN +'/sendMessage?chat_id='+ chat_id +'&text='+ text
    
    r = requests.get(url)
    return r.json()

msg()
