import urllib2
import twitter, datetime

file = open("twitterCreds.txt")
creds = file.readline().strip().split(',')

#response = urllib2.urlopen("http://")
#html = response.read()

currentSession=open("/Users/sslim/Library/Application Support/Google/Chrome/Default/Current Session")
rawtext = currentSession.read()
lines = rawtext.splitlines()

lastURL = ""
for line in lines:
    if(line.find("//") != -1):
        startIndex = line.rfind("//") + 2
        endIndex = line.rfind("/")
        lastURL = line[startIndex:endIndex]
    
print(lastURL)
    
#api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

#timestamp = datetime.datetime.utcnow()

#response = api.PostUpdate("Tweeted at " + str(timestamp))
                         
#print("Status updated to: " + response.text)                        