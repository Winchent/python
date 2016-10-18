import random

with open ("Stopwords.txt") as stopwords:
    stopwordsagain = [line.strip() for line in stopwords]

hey = ["Hey there!", "Hellooo!", "Hi there!", "Hello there sir!", "Aloha!", "Hey!", "Oh, Hi!"]
name = ["Do you have a name?", "So what's your name?", "So what's your name, then?", "I didn't catch your name, what was it again?", "Your name?", "So what should I call you?"]
hay = ["How are you today?", "How's your day been?", "Quick, in one word or less, describe your day!", "How goes the day?", "So how is your day?", "What's cooking?"]
nicename = ["I like that name!", "that's a pretty cool name!", "really cool name!", "really nice name!", "that's an interesting name!", "I used to know a guy with that name!", "I know somebody with that name!", "that's a nice name, bet it has an interesting meaning behind it!", "what a lovely name!", "cool name!"]
qintro = ["So, I wanted to ask you, ", "So I was going to ask you, ", "So, can I ask you, ", "I was going to ask you, ", "Right, so can I ask, ", "This question has been on my mind for a while now: ", "I'm curious, "]

q1 = ["what's your favourite season of the year?"]
q2 = ("what's your earliest memory?")
q3 = ("what was your childhood like?")
q4 = ("what do you think of the weather?")
q5 = ("who's your favourite actor?")
query = (q1, q2, q3, q4, q5)

randomhey = random.choice(hey)
randomname = random.choice(name)
randomhay = random.choice(hay)
randomnicename = random.choice(nicename)
randomqintro = random.choice(qintro)
randomquery = random.choice(query)

response = raw_input(randomhey + " ")
nameresponse = raw_input(randomname + " ")
firresponse = raw_input(nameresponse + ", " + randomnicename + " " + randomhay + " ")
if input is ("bad", "awful", "really bad", "terrible", "not good", "very bad"):
    badresponse = raw_input("So sorry to hear that, " + nameresponse + ", hopefully it will get better. " + randomqintro + query + " ")
if input is ("good", "amazing", "really good", "terrific", "not bad", "very good"):
    secresponse = raw_input("That's good, " + nameresponse + "! " + randomqintro + query + " ")
#if query is q1:
#    raw_input("Ah, " + secresponse + ", that's my favourite season too!")
#    elif query is q2:
#    raw_input(secresponse + "? That sounds nice. I wish I could have memories like that.")
    
thiresponse = raw_input(secresponse + "? That's really interesting. " + randomquery + " ")
print("That sounds really nice!")