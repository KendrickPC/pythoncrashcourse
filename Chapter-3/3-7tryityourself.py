# 3-4 Guest List
guest_list = ['Barack Obama', 'Xi Jing Ping', 'Stephen Curry']
print("\nDear " + guest_list[0] +"," + "\n\tPlease come and join me for coffee and a chat?")
print("\nDear " + guest_list[1] +"," + "\n\tPlease bring your beautiful daughter (the Princess of China) and join me for coffee and a chat?")
print("\nDear " + guest_list[2] +"," + "\n\tPlease come and join me for coffee and a chat?")

# 3-5 Changing Guest List
print("\nI offer my condolences as " + guest_list[2] + " will be unable to join us for coffee due to the 2018 NBA Finals.")

flakers = guest_list.pop(2)
print(flakers + "'s list data has been popped.")

guest_list.append('LeBron James')
# print(guest_list)

print("\nDear " + guest_list[0] +"," + "\n\tPlease come and join me for coffee and a chat?")
print("\nDear " + guest_list[1] +"," + "\n\tPlease bring your beautiful daughter (the Princess of China) and join me for coffee and a chat?")
print("\nDear " + guest_list[2] +"," + "\n\tPlease come and join me for coffee and a chat?")

# 3-6 More Guests
print("\nDear " + guest_list[0] +"," + "\n\tWe have acquired a bigger coffee table so please account for three more new guests. Thank you for your consideration.")
print("\nDear " + guest_list[1] +"," + "\n\tWe have acquired a bigger coffee table so please account for three more new guests. Thank you for your consideration.")
print("\nDear " + guest_list[2] +"," + "\n\tWe have acquired a bigger coffee table so please account for three more new guests. Thank you for your consideration.")


guest_list.insert(0, 'Donald Trump')
guest_list.insert(2, 'Angela Merkel')
guest_list.append('Kim Jong-un')

print("\nDear " + guest_list[0] +"," + "\n\tPlease come and join me for coffee and a chat?")
print("\nDear " + guest_list[1] +"," + "\n\tPlease bring your beautiful daughter (the Princess of China) and join me for coffee and a chat?")
print("\nDear " + guest_list[2] +"," + "\n\tPlease come and join me for coffee and a chat?")
print("\nDear " + guest_list[3] +"," + "\n\tPlease come and join me for coffee and a chat?")
print("\nDear " + guest_list[4] +"," + "\n\tPlease come and join me for coffee and a chat?")
print("\nDear " + guest_list[5] +"," + "\n\tPlease come and join me for coffee and a chat?")

# 3-7 Shrinking Guest List
print("\nDear beloved guests," + "\n\tThere are only two guest seats available now. Therefore, some of our guests will not be attending our fireside coffee chat. Thank you for your understanding.")
print(guest_list)
# uninvited = guest_list.pop(0)
# uninvited = guest_list.pop(4)
# uninvited = guest_list.pop(3)

uninvited = guest_list.pop(5)
uninvited = guest_list.pop(4)
uninvited = guest_list.pop(0)
uninvited = guest_list.pop(1)

print(guest_list)

message1 = "\nDear " + guest_list[0] + "," + "\n\tPlease note that you are still invited to our fireside coffee chat. Thank you for your time and consideration - see you soon. Cheers."
message2 = "\nDear " + guest_list[1] + "," + "\n\tPlease note that you are still invited to our fireside coffee chat. Thank you for your time and consideration - see you soon. Cheers."
print(message1)
print(message2)

del guest_list[1]
del guest_list[0]

print(guest_list)