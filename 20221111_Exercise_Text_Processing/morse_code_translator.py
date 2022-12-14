decode = {".-": "A",
          "-...": "B",
          "-.-.": "C",
          "-..": "D",
          ".": "E",
          "..-.": "F",
          "--.": "G",
          "....": "H",
          "..": "I",
          ".---": "J",
          "-.-": "K",
          ".-..": "L",
          "--": "M",
          "-.": "N",
          "---": "O",
          ".--.": "P",
          "--.-": "Q",
          ".-.": "R",
          "...": "S",
          "-": "T",
          "..-": "U",
          "...-": "V",
          ".--": "W",
          "-..-": "X",
          "-.--": "Y",
          "--..": "Z"}
morse_code = input().split(" | ")
decoded_message = []
for word in range(len(morse_code)):
    current_word = morse_code[word].split()
    decoded_word = ""
    for letter in current_word:
        decoded_word += decode[letter]
    decoded_message.append(decoded_word)
print(" ".join(decoded_message))

# test inputs:

# .. | -- .- -.. . |  -.-- --- ..- | .-- .-. .. - . | .- | .-.. --- -. --. | -.-. --- -.. .

# .. | .... --- .--. . | -.-- --- ..- | .- .-. . | -. --- - | -- .- -..
