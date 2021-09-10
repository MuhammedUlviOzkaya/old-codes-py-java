contacts = {"contact1" : {"home address" : "atatürk mah no.1",
                         "office address" : "cumhuriyet mah no.10 kat 45",
                         "phone number" : "03758295923",
                          "office number" : "931243254"},
            "contact2" : {"home address" : "cumhuriyet mah no.5 kat 2",
                          "office adress" : "alsancak mah venüs iş hanı kat 10",
                          "phone number" : "0320505425",
                          "office number" : "3243535454"}
            }

wantedPerson = input("Wanted Person: ")
if wantedPerson in contacts:
    flag = True
else:
    flag = False
    print("No person found.")
    quit()

wantedInfo = input("Wanted Information: ")
if flag:
    print(contacts.get(wantedPerson).get(wantedInfo, "No information found."))
