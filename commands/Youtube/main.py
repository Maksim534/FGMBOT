from aiogram import Dispatcher, types
from user import BFGuser, BFGconst


async def youtube(message: types.Message):
  
  

def reg(dp: Dispatcher):
  dp.register_message_handler(youtube, lambda message: message.text == 'ютуб')
