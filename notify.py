def sendTg():
    try:
        content = test
        url = f'https://api.telegram.org/bot2053091895:AAE8t09sW--zV_muyfXpf8Euv_6EunzyMLE/sendMessage?chat_id=549864937&text={content}'     
        session = requests.Session()
        resp = session.post(url)
        print(resp)
    except Exception as e:
        print('Tg通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())
if __name__ == "__main__":
   sendTg()
