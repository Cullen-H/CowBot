import sqlite3

conn = sqlite3.connect('../cowbot.db')
c = conn.cursor()

c.execute(""" 
CREATE TABLE server (
  id INTEGER PRIMARY KEY
)
""")

c.execute("""
CREATE TABLE user (
  id INTEGER PRIMARY KEY,
  discord_user_id INTEGER,
  server_id INTEGER NOT NULL UNIQUE,
  FOREIGN KEY (server_id) REFERENCES Server(id)
    ON DELETE CASCADE
)
""")

c.execute("""
CREATE TABLE chat_time (
  id INTEGER PRIMARY KEY,
  total_time,
  user_id,
  FOREIGN KEY (user_id) REFERENCES user(id)
    ON DELETE CASCADE
)
""")

c.execute("""
CREATE TABLE roster_channel (
  id INTEGER PRIMARY KEY,
  channel_id,
  server_id INTEGER NOT NULL UNIQUE,
  FOREIGN KEY (server_id) REFERENCES server(id)
    ON DELETE CASCADE
)
""")

conn.commit()
conn.close()
