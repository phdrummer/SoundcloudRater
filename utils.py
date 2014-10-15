'''
Input: None
Output: Return a dictionary of words and their values from the textfile
''' 
def getWordValues():
        infile = open("wordValues.txt","r")
        wordValues = {} 
        for line in infile:
                splitline = line.split()
                wordValues[splitline[0]] = splitline[1]
        return wordValues

'''
Input: A Track
Output: The rating of a track
'''
def trackRating(track):
        tweetText = track['post']

'''
Input: Takes the expanded Soundcloud URL
Output: Returns whether or not link is valid
Put logic for the checking of whether the link is valid here
TODO: Make a regular expression to ensure link is to a track and not an artist
'''
def checkEntry(entry):


        #Simpler Check w/o regex
        if "//soundcloud.com/" in entry["expanded_url"]:
                return True
        return False
'''
        soundcloudRegex = re.compile("(soundcloud.com\/\S+\/\S+)")
        print (str(entry["expanded_url"]) + str( re.match(soundcloudRegex,str(entry["expanded_url"]))))
        return  re.match(soundcloudRegex,str(entry["expanded_url"])):
'''


'''
Input: Takes a twitter post string
Output: Sanitizes the post to only be printable characters removing emojis and other chars 
'''     
def sanitizeEntry(entry):
        return str(entry.encode('ascii',errors='ignore'))[1:]

