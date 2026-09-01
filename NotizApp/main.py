notes = [
    {"title": "Einkauf", "text": "Milch, Brot, Eier"},
    {"title": "Arbeit", "text": "Backendcall um 11"},
]

a = "test"
b = "test2"
c = 1

def show_notes():
    for note in notes:
        print(f"Title: {note['title']}, Text: {note['text']}")

def add_note(a, b):
    notes.append({"title": a, "text": b})

def delete_note():
    notes.pop() 

def update_note(c):
    notes[c].title = "moin"
    notes[c].text = "tschüss"

# add_note()

# delete_note()
# update_note()
show_notes()