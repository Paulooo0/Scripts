name=input("whats your name? ").strip().title()
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("WHO?")