dinner_guests = ['atarah', 'elisheba', 'shem','pat', 'walter']

for guest in dinner_guests:
    print("Hello " + guest.title() + " you are invited to dinner!")

print("Pat is not going to be able to make it.")
dinner_guests.remove("pat")
for guest in dinner_guests:
    print("Hello " + guest.title() + ", you are invited to dinner.")

dinner_guests.insert(0,"gam")
dinner_guests.insert(3, "obie")
dinner_guests.append("riri")
print(dinner_guests)

for guest in dinner_guests:
    print("Hello " + guest.title() + ", you are invited to dinner.")

print("\n")

print("Unfortunately I can only invite 2 people.")
#Remove all but 2 guests using pop()

#Have to use len because > cannot be applied to a string
while len(dinner_guests) > 2:
    print("Sorry " + dinner_guests.pop().title() + " but I will have to reschedule dinner.")

#send invites to remaining 2 guests
for guest in dinner_guests:
    print(guest.title() + ", you are still invited to dinner!")

del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)
