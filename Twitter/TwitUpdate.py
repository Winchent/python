import twitter, datetime, sqlite3, time

while True:
    console = sqlite3.connect("/Users/swheeler3/Library/Application Support/Google/Chrome/Default/History")
    cursor = console.cursor()

    cursor.execute("SELECT urls.title FROM urls")

    rows = cursor.fetchall()
    site = []

    for row in rows: site.append(row)
    MRSite = str(site[-1])
    PageUrl = MRSite[3:-3]
    console.close()

    file = open("twitter.txt")
    creds = file.read().split('\n')
    api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

    #timestamp = datetime.datetime.utcnow()

    response = api.PostUpdate("I recently viewed " + PageUrl)

    print("Status updated to: " + response.text)
    
    time.sleep(30)