notes = []

while True:    
  print("Todo-APP")
  print("[1] Get all notes")
  print("[2] Add note")
  print("[3] Delete note")
  print("[4] Exit")

  choice = input("Choose command: ")
  if choice == "4":
    break
  elif choice == "1":
    for note in notes:
      print(f"{notes.index(note)+1}. {note}")
  elif choice == "2":
    note = input("Add note here: ")
    notes.append(note)
    print("Your note added!")
  elif choice == "3":
    for note in notes:
      print(f"{notes.index(note)+1}. {note}")
    delete = int(input("Enter number of the note: "))
    notes.remove(notes[delete - 1])
    for note in notes:
      print(f"{notes.index(note)+1}. {note}")
    print("Your note succesfuly removed!")
print("Good bye!")

