import urllib2

response = urllib2.urlopen("http://www.bbc.co.uk/sport/football/tables")
html = response.read()

stats = {}
stopwords = ["about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

lines = html.splitlines()
for line in lines:
    if(line.find("team-name") != -1):
        startIndex = line.rfind("'>") + 2
        teamName = line[startIndex:-9]
        if(teamName.find("scope") == -1):
            print("Creating " + teamName)
            stats[teamName] = [0,0]
    if(line.find("goal-difference") != -1):
        startIndex = line.rfind("\">") + 2 
        difference = line[startIndex:-5]
        if(difference.find("abbr") == -1):
            stats[teamName][0] = int(difference)
            print("Inserting difference " + difference + " into " + teamName)
    if(line.find("points") != -1):
        startIndex = line.rfind("\">") + 2 
        points = line[startIndex:-5]
        if(points.find("abbr") == -1):
            stats[teamName][1] = int(points)
            print("Inserting points " + points + " into " + teamName)
        


def delWords(words):
    if not words:
        sentence = raw_input("What is your name? ")
        words = sentence.split()
    marked = []
    for t in words:
        if t.lower() in stopwords:
            marked.append
            ('')    
        else:
            marked.append(t)
    return marked

input = raw_input("What is your name ?")
justTheName = delWords(input.split())
print("Hello there " + justTheName[0])

input = raw_input("What can I do for you today?")

input = raw_input("And what might that game be?")
game = delWords(input.split())
print(game[0] +  " " + game[1] + " that sounds interesting!")

input = raw_input("How many points are you on ?")

for team in stats:
        if stats[team][1] == 6 and stats[team][0] == -10:
            print("You're in a relegation dog fight " + team)

        
        #change to general conversation insted of guesser (top, middle, bottom teams)
