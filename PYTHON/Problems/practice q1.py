# secrete code language
import random
print("Encoding the message...")
def encode_message(message):
    l=len(message)
    if l<=3:
        m= message[::-1]
        # adding 3 random characters to the end of the message and 3 random characters to the beginning of the message
        for _ in range(3):            
            m= random.choice('abcdefghijklmnopqrstuvwxyz') + m + random.choice('abcdefghijklmnopqrstuvwxyz')
        return m
    elif l>3:
        # adding first two characters to the end of the message
        m= message[2:] + message[:2]
        # adding 3 random characters to the end of the message and 3 random characters to beginning of the message
        for _ in range(3):            
            m= random.choice('abcdefghijklmnopqrstuvwxyz') + m + random.choice('abcdefghijklmnopqrstuvwxyz')
        return m
# testing the function
message = "hello"
encoded_message = encode_message(message)
print(encoded_message)

#decoding the message
print("\nDecoding the message...")
def decode_message(encoded_message):
    # removing the random characters from the beginning and end of the message
    m = encoded_message[3:-3]
    l = len(m)
    if l<=3:
        # reversing the message to get the original message
        return m[::-1]
    elif l>3:
        # moving the last two characters to the beginning of the message to get the original message
        return m[-2:] + m[:-2]

decoded_message = decode_message(encoded_message)
print(decoded_message)