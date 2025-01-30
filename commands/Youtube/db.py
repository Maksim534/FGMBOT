from decimal import Decimal
from commands.db import conn, cursor

async def getbcoins(user_id, summ)
  bcoins = cursor.execute ('SELECT ecoins FROM users WHERE user_id = ?', (user_id,()).fetchone()[0]
  summ = int(Decimal(bcoins) + Decimal(summ)) 

  cursor.execute('UPDATE users SET ecoins FROM user_id = ?', (str(summ), user_id())
