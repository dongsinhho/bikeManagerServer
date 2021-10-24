import requests
import random
import websocket
import json
import asyncio
import logging

mode = False  #mặc định của khoá xe là luôn đÓng

logging.basicConfig(filename='data.log')

def on_message(ws, message):   #nhận dữ liệu từ websocket báo là khoá xe đã đóng thì thay đổi chế độ
    print(message)
    global mode
    if (message.data.mode != mode): 
        mode = not mode 
        logging.info("--------------Start logging now ---------------------") if mode else logging.info("--------------Stop logging now ---------------------")
        # do something để đÓng khoá xe
        #dừng ghi log
# cần auth khi request tới ws

def on_open(ws):
    json_data = json.dumps({
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    })
    ws.send(json_data)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


async def SendData():
    while True:
        latitude = random.uniform(10.870000,10.880000)
        longtitude = random.uniform(106.780000,106.800000)
        print("hello world")
        
        data = {
                "id": "1",
                "latitude": latitude,
                "longtitude": longtitude
            }
        if not mode:
            requests.post("http://localhost:8000/api/bike/", data=data)
        # else:
        #     await requests.post("localhost:8000/", data=data)
        else: 
            logging.info(data)
        asyncio.sleep(10)
        
    
# nếu mode = True (xe được thuê) thì bắt đầu ghi log 

if __name__ == "__main__":
    asyncio.run(SendData())
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8000/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_open=on_open)
    ws.on_open = on_open
    ws.run_forever()