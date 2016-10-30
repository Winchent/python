import random

#with open ("Stopwords.txt") as stopwords:
#    stopwordsagain = [line.strip() for line in stopwords]

hey = ["Hey there!", "Hellooo!", "Hi there!", "Hello there sir!", "Aloha!", "Hey!", "Oh, Hi!", "Gutentag!", "Hallo!", "Bonjour!", "Hola!", "Ey b0ss!"]
name = ["Do you have a name?", "So what's your name?", "So what's your name, then?", "I didn't catch your name, what was it again?", "Your name?", "So what should I call you?"]
hay = ["How are you today?", "How's your day been?", "Quick, in one word or less, describe your day!", "How goes the day?", "So how is your day?", "What's cooking?"]
nicename = ["I like that name!", "that's a pretty cool name!", "really cool name!", "really nice name!", "that's an interesting name!", "I used to know a guy with that name!", "I know somebody with that name!", "that's a nice name, bet it has an interesting meaning behind it!", "what a lovely name!", "cool name!"]
qintro = ["So, I wanted to ask you, ", "So I was going to ask you, ", "So, can I ask you, ", "I was going to ask you, ", "Right, so can I ask, ", "This question has been on my mind for a while now: ", "I'm curious, "]
qintro2 = ["Can I ask you something else? In your opinion, ", "There's something else I wanted to ask you, ", "If you can remember, ", "I was just curious about something else, ", "Here's another one, ", "If you don't mind me asking you another question, ", "If I could ask you another question, "]
qintro3 = ["Last question, don't worry about it, but ", "Last question for now, ", "Here's the last question I wanted to ask, ", "Alright, last question, and this one is a doozy! So, ", "Last question, hope you're not too tired! Right, "]
gb = ["Well, thanks so much for talking to me. It's nice to talk to someone so interesting. Hope you have a good day!", "Thank you so much for talking to me, I've had a blast. See ya!", "Sorry for taking up so much of your time with these questions, but I've had a really good time! See you later!", "You certainly powered through those questions! Sorry about the invasiveness, but you're really quite interesting! Hope you have a good day!"]

q1 = ["what's your favourite season of the year?", "Spring, Summer, Autumn and Winter: Which do you like the most?", "what season do you prefer the most?", "what season is your favourite?", "what's your favourite season of the year?", "what season is your favourite?"]
q2 = ["what's your earliest memory?", "how far back do you remember? What's your earliest memory?", "what would you say is your very first memory?", "what's the first thing you can remember?", "what's the earliest back you can remember?"]
q3 = ["what was your childhood like?"]
q4 = ["what do you think of the weather?", "how are you finding the weather?", "how's the weather?", "what do you think of the weather today?", "what do you think of the weather we've been having?", "have you been having good weather? How are you finding it?"]
q5 = ["who's your favourite actor?", "from all of the films and shows you've seen, which actor did you like the best?", "out of every actor you know, who would you say is your favourite?", "quick, tell me, who is your favourite actor or actress?", "do you have a favourite actor or actress?", "which actor or actress do you like the most?", "who's your top actor or actress?"]
q6 = ["what would you say is your favourite animal?", "do you have a favourite animal?", "what's your favourite animal?", "what is your favourite animal, if you have one?", "what's your favourite pet?", "what would be your dream pet?", "what would you say is your dream pet?", "any dream pets?", "any favourite animals?"]
q7 = ["what is your biggest fear?", "what would you say is your biggest fear?", "what would you say scares you the most?", "what is your greatest phobia?", "what scares you the most?", "is there anything that absolutely terrifies you?", "what absolutely terrifies you the most?"]

q1ans = ["That's really interesting. It's one of my favourites too.", "I like that season too.", "Oh yeah, definitely one of my favourites!", "That has to be my favourite as well.", "Well, I'm a bit iffy on that one.", "Ehhhh...wouldn't call it one of my favourites.", "Nah, not too fond of that one, to be honest.", "Hmm...I don't really like that one too much. Oh well, to each their own!", "I'm afraid I'm not too fond of that season.", "Sorry, I don't really like that one. To each their own, of course!"]
q2ans = ["That's really lovely. I wish I could remember that far back."]
q3ans = ["That sounds really nice. My childhood was rather quiet."]
q4ans = ["I feel the same way."]
q5ans = ["They're my favourite too!", "Oh, I like them!", "Yeah, they're the best.", "Huh, I didn't think about them.", "They're alright.", "They're pretty good. Not the best, but they're up there.", "Eh, they've always been a bit naff in my opinion.", "Can't really say I care for some of the movies they've been in.", "Oh no! So sorry, but I just can't stand them! Sorry about that!", "*vomits slightly* Oh God, I'm so sorry, it's just...the mere mention of their name makes me sick!"]
q6ans = ["Oh they're adorable! I love those!", "Oh they're the best! One of my favourites too!", "Oh yes, that's definitely my favourite!", "Yeah, they're pretty cool.", "Ah yes, those are nice.", "They're pretty cool, but I wouldn't call them my favourite.", "Oh, those are alright. Not my favourite, but they're alright.", "Err...no. Sorry, I've always found them a bit creepy. But...whatever!", "Ew no! I've always found those to be a bit creepy!", "Those terrify me! Sorry.", "I used to have one of those when I was younger!"]
q7ans = ["That's one of my biggest fears too.", "Eww yeah! That terrifies me!", "Yeah, that's too creepy for me.", "Really? I never found that too scary to be honest.", "Oh, I always found that quite endearing.", "I didn't know you could be afraid of something like that!", "Oh yeah, don't worry about that. Thousands of people share that fear."]

randomhey = random.choice(hey)
randomname = random.choice(name)
randomhay = random.choice(hay)
randomnicename = random.choice(nicename)
randomqintro = random.choice(qintro)
randomqintro2 = random.choice(qintro2)
randomqintro3 = random.choice(qintro2)
randomqintro4 = random.choice(qintro2)
randomqintro5 = random.choice(qintro2)
randomqintro6 = random.choice(qintro2)
randomqintro7 = random.choice(qintro3)
randomgb = random.choice(gb)

randomq1 = random.choice(q1)
randomq2 = random.choice(q2)
randomq3 = random.choice(q3)
randomq4 = random.choice(q4)
randomq5 = random.choice(q5)
randomq6 = random.choice(q6)
randomq7 = random.choice(q7)

randomq1ans = random.choice(q1ans)
randomq2ans = random.choice(q2ans)
randomq3ans = random.choice(q3ans)
randomq4ans = random.choice(q4ans)
randomq5ans = random.choice(q5ans)
randomq6ans = random.choice(q6ans)

response = raw_input(randomhey + " ")
nameresponse = raw_input(randomname + " ")
firresponse = raw_input(nameresponse + ", " + randomnicename + " " + randomhay + " ")
secresponse = raw_input("That's good, " + nameresponse + "! " + randomqintro + randomq1 + " ")
thiresponse = raw_input(secresponse + "? " + randomq1ans + " " + randomqintro2 + randomq2 + " ")
fouresponse = raw_input(thiresponse + "? " + randomq2ans + " " + randomqintro3 + randomq3 + " ")
fivresponse = raw_input(fouresponse + "? " + randomq3ans + " " + randomqintro4 + randomq4 + " ")
sixresponse = raw_input(fivresponse + "? " + randomq4ans + " " + randomqintro5 + randomq5 + " ")
sevresponse = raw_input(sixresponse + "? " + randomq5ans + " " + randomqintro6 + randomq6 + " ")
eigresponse = raw_input(sevresponse + "? " + randomq5ans + " " + randomqintro7 + randomq7 + " ")
print(eigresponse + "? " + randomq6ans + " I hope that didn't bring up too many bad memories. " + randomgb)

#query = (q1, q2, q3, q4, q5)

#randomquery = random.choice(query)

#if input is ("bad", "awful", "really bad", "terrible", "not good", "very bad"):
#    badresponse = raw_input("So sorry to hear that, " + nameresponse + ", hopefully it will get better. " + randomqintro + query + " ")
#if input is ("good", "amazing", "really good", "terrific", "not bad", "very good"):

#if query is q1:
#    raw_input("Ah, " + secresponse + ", that's my favourite season too!")
#    elif query is q2:
#    raw_input(secresponse + "? That sounds nice. I wish I could have memories like that.")
    
