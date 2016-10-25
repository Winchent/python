import random

with open ("Stopwords.txt") as stopwords:
    stopwordsagain = [line.strip() for line in stopwords]

hey = ["Hey there!", "Hellooo!", "Hi there!", "Hello there sir!", "Aloha!", "Hey!", "Oh, Hi!", "Gutentag!", "Hallo!", "Bonjour!", "Hola!", "Ey b0ss!"]
name = ["Do you have a name?", "So what's your name?", "So what's your name, then?", "I didn't catch your name, what was it again?", "Your name?", "So what should I call you?"]
hay = ["How are you today?", "How's your day been?", "Quick, in one word or less, describe your day!", "How goes the day?", "So how is your day?", "What's cooking?"]
nicename = ["I like that name!", "that's a pretty cool name!", "really cool name!", "really nice name!", "that's an interesting name!", "I used to know a guy with that name!", "I know somebody with that name!", "that's a nice name, bet it has an interesting meaning behind it!", "what a lovely name!", "cool name!"]
qintro = ["So, I wanted to ask you, ", "So I was going to ask you, ", "So, can I ask you, ", "I was going to ask you, ", "Right, so can I ask, ", "This question has been on my mind for a while now: ", "I'm curious, "]
qintro2 = ["Can I ask you something else? In your opinion, ", "There's something else I wanted to ask you, ", "If you can remember, ", "I was just curious about something else, ", "Here's another one, ", "If you don't mind me asking you another question, ", "If I could ask you another question, "]

q1 = ["what's your favourite season of the year?", "Spring, Summer, Autumn and Winter: Which do you like the most?", "what season do you prefer the most?", "what season is your favourite?", "what's your favourite season of the year?", "what season is your favourite?"]
q2 = ["what's your earliest memory?", "how far back do you remember? What's your earliest memory?", "what would you say is your very first memory?", "what's the first thing you can remember?", "what's the earliest back you can remember?"]
q3 = ["what was your childhood like?"]
q4 = ["what do you think of the weather?", "how are you finding the weather?", "how's the weather?", "what do you think of the weather today?", "what do you think of "]
q5 = ["who's your favourite actor?", "from all of the films and shows you've seen, which actor did you like the best?", "out of every actor you know, who would you say is your favourite?", "quick, tell me, who is your favourite actor or actress?"]


randomhey = random.choice(hey)
randomname = random.choice(name)
randomhay = random.choice(hay)
randomnicename = random.choice(nicename)
randomqintro = random.choice(qintro)
randomqintro2 = random.choice(qintro2)

randomq1 = random.choice(q1)
randomq2 = random.choice(q2)
randomq3 = random.choice(q3)
randomq4 = random.choice(q4)
randomq5 = random.choice(q5)

response = raw_input(randomhey + " ")
nameresponse = raw_input(randomname + " ")
firresponse = raw_input(nameresponse + ", " + randomnicename + " " + randomhay + " ")
secresponse = raw_input("That's good, " + nameresponse + "! " + randomqintro + randomq1 + " ")
thiresponse = raw_input(secresponse + "? That's really interesting. " + randomqintro2 + q2 + " ")
fouresponse = raw_input()
print("That sounds really nice!")

#query = (q1, q2, q3, q4, q5)

#randomquery = random.choice(query)

#if input is ("bad", "awful", "really bad", "terrible", "not good", "very bad"):
#    badresponse = raw_input("So sorry to hear that, " + nameresponse + ", hopefully it will get better. " + randomqintro + query + " ")
#if input is ("good", "amazing", "really good", "terrific", "not bad", "very good"):

#if query is q1:
#    raw_input("Ah, " + secresponse + ", that's my favourite season too!")
#    elif query is q2:
#    raw_input(secresponse + "? That sounds nice. I wish I could have memories like that.")
    
