from decimal import Decimal
from commands.db import conn, cursor


async def getbcoins(user_id: int, summ):
    ecoins = cursor.execute('SELECT ecoins FROM users WHERE user_id = ?', (user_id,)).fetchone()[0]
    summ = int(Decimal(ecoins) + Decimal(summ))

    cursor.execute(f"UPDATE users SET ecoins = ? WHERE user_id = ?", (str(summ), user_id))
    conn.commit()

async def createkanal(user_id: int, num):
    createkanal = cursor.execute(f"UPDATE users SET youtubekanal = ? WHERE user_id = ?", (0, user_id))
    conn.commit()
