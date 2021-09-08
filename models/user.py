import sqlite3

class User:
    """SQL model for server user"""

    def add(server_id, discord_user_id):
        """Adds a new user to a discord"""

        conn = sqlite3.connect('cowbot.db')
        c = conn.cursor()

        c.execute("""
            INSERT INTO server (id)
            VALUES (:server_id)
            """, {'server_id': server_id})
        
        conn.commit()
        conn.close()

