import sqlite3

DB_NAME = "memory.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS conversations(
            session_id TEXT,
            role TEXT,
            content TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_message(session_id, role, content):
    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        INSERT INTO conversations
        VALUES (?, ?, ?)
        """,
        (session_id, role, content),
    )

    conn.commit()
    conn.close()


def get_history(session_id, limit=10):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.execute(
        """
        SELECT role, content
        FROM conversations
        WHERE session_id=?
        ORDER BY rowid DESC
        LIMIT ?
        """,
        (session_id, limit),
    )

    rows = cursor.fetchall()

    conn.close()

    rows.reverse()

    return [
        {"role": role, "content": content}
        for role, content in rows
    ]


init_db()