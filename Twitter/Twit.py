import twitter
user = 791975463782608896

file = open("twitter.txt")
creds = file.read().split('\n')
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
statuses = api.GetUserTimeline(user)

print (statuses[0].text)