# Module by @DeBotMod
import requests

from telethon import events
from userbot import client


info = {'category': 'chat', 'pattern': '.crypto', 'description': 'курс криптовалюты Вид: .crypto'}


@client.on(events.NewMessage(pattern='.crypto'))
async def handle_crypto(event):
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cdogecoin%2Ctether&vs_currencies=rub")
        data = response.json()

        usdt = f"{data['tether']['rub']}"
        btc = f"{data['bitcoin']['rub']}"
        eth = f"{data['ethereum']['rub']}"
        dogecoin = f"{data['dogecoin']['rub']}"

        crypto_info = f"💰 Курсы криптовалют:\n\nTether: {usdt}₽\n\nBitcoin: {btc}₽\n\nEthereum: {eth}₽\n\nDogcoin: {dogecoin}₽"

        await event.edit(crypto_info)
    except Exception as e:
        await event.respond(f'Произошла ошибка: {str(e)}')
