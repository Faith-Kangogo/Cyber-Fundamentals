password = input("Create a new password: ")

# len() counts the letters
if len(password) < 6:
    print("❌ Too short! This is a weak password.")
else:
    print("✅ Strong password. Good job!")
