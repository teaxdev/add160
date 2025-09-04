def conference_signup(*participants, **contact_details):
    print("Conference Participants and Their Contact Details:")
    print("--------------------------------------------------")
    i = 0
    for email, number in contact_details.items():
        print(f"Name: {participants[i]}\nEmail: {email}\nPhone: {number}")
        print("--------------------------------------------------")
        i+=1
            
participants = ("Alice", "Bob", "Charlie")
contact_details = {"alice@example.com": "123-456-7890", "bob@example.com": "987-654-3210", "charlie@example.com": ""}

conference_signup(*participants, **contact_details)