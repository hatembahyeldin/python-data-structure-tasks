contacts = {
    "Ali": "01012345678",
    "Sara": "01098765432",
    "Mona": "01011223344"
}

print("Contacts:")
for name in contacts:
    print(name)

search_name = input("Enter a name to search: ")
if search_name in contacts:
    print("Phone number:", contacts[search_name])
else:
    print("Contact not found.")