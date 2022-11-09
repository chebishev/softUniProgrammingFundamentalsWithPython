class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:

    command = input().split()

    if command[0] == "Stop":

        break

    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver, content)
    emails.append(email)

indices_list = list(map(int, input().split(", ")))
for index in indices_list:
    emails[index].send()

for email in emails:
    print(email.get_info())

# test inputs:

# Peter John Hi,John
# John Peter Hi,Peter!
# Katy Lilly Hello,Lilly
# Stop
# 0, 2

# Anna, Bella, Hi
# Sam, Dany, Okey
# Felix, Mery, Bye
# Stop
# 0

