from aiogram import Dispatcher, types
from user import BFGuser, BFGconst
import random
from assets.antispam import antispam
import commands.Youtube.db as db
from assets.transform import transform_int as tr


@antispam
async def youtube(message: types.Message, user: BFGuser):
  if int(user.property.phone) == 0:
      await message.answer('у вас нет телефона чтобы снимать видеоролики')
      return

  summ = random.randint(1, 2)
  photo = ('https://avatars.mds.yandex.net/i?id=a2e825c761e95d922d0df365745526c3014944c0-4902600-images-thumbs&n=13')
  
  await db.getbcoins(user.user_id, summ)
  await bot.send_photo(chat_id=message.id, f'{photo}Вы успешно сняли видеоролик, вы получили {summ}, b-coins')

  
  

def reg(dp: Dispatcher):
  dp.register_message_handler(youtube, lambda message: message.text == 'ютуб')
