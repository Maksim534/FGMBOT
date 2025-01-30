from decimal import Decimal
from commands.db import conn, cursor


async def getbcoins(user_id: int, summ):
    ecoins = cursor.execute('SELECT ecoins FROM users WHERE user_id = ?', (user_id,)).fetchone()[0]
    rand = int(Decimal(ecoins) + Decimal(rand))

    cursor.execute(f"UPDATE users SET ecoins = ? WHERE user_id = ?", (str(rand), user_id))
    conn.commit()
