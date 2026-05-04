def cleanup_sessions_fixed(sessions):
    
    active_users = set()

    for session in sessions[:]: #Fehler war dass aus der originalen Liste gelöscht wurde und Python dadurch einige Elemente übersprungen hat
        if session["expired"] == True:  #Lösung: sessions[:], Python liest aus der kopierten Liste aber löscht aus der Orginalen 
            sessions.remove(session)
        else:
            active_users.add(session["user"])

    return sessions, active_users
sessions = [
    {"user": "alice", "expired": False},
    {"user": "bob", "expired": True},
    {"user": "carol", "expired": True},
    {"user": "dave", "expired": False},
    {"user": "eve", "expired": True},
]
result, active = cleanup_sessions_fixed(sessions)
print(result)
print(active)   