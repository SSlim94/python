import urllib2    #importing library for url 
import twitter, datetime  #importing twitter library + date and time 

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
        lastURL = line[startIndex:endIndex]  #finding where the // is in html code and splitting it
    
print(lastURL)  #priniting shorter url 
    
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

timestamp = datetime.datetime.utcnow()

response = api.PostUpdate("I'm really liking this website " + lastURL + "and this was tweeted at " + str(timestamp))
                         
print("Status updated to: " + response.text)                        