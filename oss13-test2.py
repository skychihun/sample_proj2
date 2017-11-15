words = ["cat", "mouse", "tiger", "lion"]
shortest = words[0]
for i in range(1,len(words)):
    if(len(shortest) > len(words[i])):
        shortest = words[i]
print("Shortest word is ", shortest)
