name = input("What's your name ? ")

# if name == "Harry" or name == "Hermine" or name =="Ron":
#     print("Gryffindor")
# # elif name == "Hermione":
# #     print("Gryffindor")
# # elif name =="Ron":
# #     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

match name :
    case "Harry" | "Hermine" | "Ron":
        print("Gryffindor")
    # case 'hermine':
    #     print("Gryffindor")
    # case "Ron":
    #     print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
            print("Who?")