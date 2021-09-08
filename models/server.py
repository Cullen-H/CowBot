import sqlite3

class Server:
    """SQL model for discord server"""

    def add(server_id):
        """Adds a new discord server to database."""
        
        conn = sqlite3.connect('cowbot.db')
        c = conn.cursor()

        c.execute("""
            INSERT INTO server (id)
            VALUES (:server_id)
            """, {'server_id': server_id})
        
        conn.commit()
        conn.close()

    def delete(server_id):
        """Deletes the server with a given id from the database"""

        conn = sqlite3.connect('cowbot.db')
        c = conn.cursor()

        c.execute("""
            DELETE FROM server
            WHERE id = :server_id
            """, {'server_id': server_id})
        
        conn.commit()
        conn.close()
