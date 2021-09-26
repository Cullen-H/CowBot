import sqlite3

class ChatTimer:
    """SQL model for tracking user chat times"""

    def update(server_id, channel_id, user_id, time):
        """Adds a new user time"""
        
        conn = sqlite3.connect('cowbot.db')
        c = conn.cursor()

        c.execute("""
                INSERT INTO chat_timer (server_id, channel_id, user_id, time)
                VALUES (:server_id, :channel_id, :user_id, :time)
                ON CONFLICT  (server_id, channel_id, user_id) DO_UPDATE SET time = time + :time
                """, {'server_id': server_id,
                      'channel_id': channel_id,
                      'user_id': user_id,
                      'time': time})

        conn.commit()
        conn.close()

    def get_channel_time(channel_id, user_id):
        """Retrieves a users time in a given channel"""

        conn = sqlite3.connect('cowbot.db')
        c = conn.cursor()

        c.execute("""
                SELECT time FROM chat_timer
                WHERE channel_id = :channel_id
                AND user_id = :user_id
                """, {'channel_id': channel_id, 'user_id': user_id})

        user_time = c.fetchone()[0]

        conn.commit()
        conn.close()

        return user_time

    def get_total_time(server_id, user_id):
        """Returns a users total time in a servers voice channels"""

        conn = sqlite3.connect('cowbot.db')
        c = conn.cursor()

        c.execute("""
                SELECT SUM (time) FROM chat_timer
                WHERE server_id = :server_id
                AND user_id = :user_id
                """, {'server_id': server_id, 'channel_id': channel_id})
        
        total_time = c.fetchone()[0]

        conn.commit()
        conn.close()

        return total_time

    def get_top_ten(server_id, channel_id=None):
        """Returns a 'leaderboard' containing a servers top
            ten most active voice channel users and their times.
            Optionally, a channel_id can be passed to return top ten
            for a specific channel"""
        
        if channel_id:
            c.execute("""
                    SELECT TOP 10 user_id, time FROM chat_timer
                    WHERE server_id = :server_id
                    AND channel_id = :channel_id
                    ORDER BY time DESC
                    """, {'server_id': server_id, 'channel_id': channel_id})
        else:
            c.execute("""
                    SELECT TOP 10 user_id, time FROM chat_timer
                    WHERE server_id = :server_id
                    ORDER BY time DESC
                    """)

        top_ten = c.fetchall()

        conn.commit()
        conn.close()

        return top_ten
