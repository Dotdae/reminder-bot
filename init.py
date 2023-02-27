import requests
import schedule
import time
import os

def morningReminder():
    
    msg = '¡Buenos días! 🐥☀️⏰\n\nDebes tomar las siguientes pastillas:\n\n' 

    # Presión

    msg = msg + '*PRESIÓN*\n\n'
    msg = msg + '*1* pastilla de *Losartan* 💊👩🏻‍⚕️\n'
    msg = msg + '*1* pastilla de *Metroprolol* 💊👩🏻‍⚕️\n\n'

    # Circulación

    msg = msg + '*CIRCULACIÓN*\n\n'
    msg = msg + '*1* pastilla de *Metroprolol* 💊👩🏻‍⚕️\n\n'

    # Orina

    msg = msg + '*ORINA*\n\n'
    msg = msg + '*1* pastilla de *Hidroclorotiazida* 💊👩🏻‍⚕️\n\n'

   
    # Otras

    msg = msg + '*OTRAS*\n\n'
    msg = msg + '*1* pastilla de *Fluoxetina* 💊👩🏻‍⚕️\n'
    msg = msg + '*1* pastilla de *Complejo B* 💊👩🏻‍⚕️\n'


    sendResponse(msg)

def nightReminder():

    msg = '¡Buenas noches! 🐈🌠⏰\n\nDebes tomar las siguientes pastillas:\n\n' 

    # Presión

    msg = msg + '*PRESIÓN*\n\n'
    msg = msg + '*1* pastilla de *Losartan* 💊👩🏻‍⚕️\n'
    msg = msg + '*1* pastilla de *Metroprolol* 💊👩🏻‍⚕️\n\n'

    # Circulación

    msg = msg + '*CIRCULACIÓN*\n\n'
    msg = msg + '*1* pastilla de *Metroprolol* 💊👩🏻‍⚕️\n'


    sendResponse(msg)


def sendResponse(res):

    token = os.environ.get('token')
    bot_id = '6047169723'
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + bot_id + '&parse_mode=Markdown&text=' + res

    response = requests.get(send_text)


if __name__ == '__main__':

    schedule.every().day.at('16:00').do(morningReminder)
    schedule.every().day.at('04:30').do(nightReminder)
    
    while(True):

        print('Bot running...')
        schedule.run_pending()
        time.sleep(1)
