class Email:

    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


data = []

while True:

    command = input().split()

    if command[0] == "Stop":
        command = list(map(int, input().split(", ")))
        for index in range(len(command)):
            data[command[index]].send()
        break
    sender = command[0]
    receiver = command[1]
    message = command[2]
    email = Email(sender, receiver, message)
    data.append(email)

for email in data:
    print(email.get_info())