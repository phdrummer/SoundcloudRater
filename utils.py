import logging
import re
import requests
import os
idfilename = 'ids.txt'
entriesfilename = 'entries.txt'
logging.basicConfig(level= logging.INFO, filename='messages.log')

'''
Input: None
Output: Return a dictionary of words and their values from the textfile
''' 


def getWordValues():
        infile = open("wordValues.txt", "r")
        wordValues = {} 
        for line in infile:
                splitline = line.split()
                wordValues[splitline[0]] = splitline[1]
        infile.close()
        return wordValues


'''Input: AllEntries
Return list with top 10 songs
TODO
'''
def getTopTen(allEntries):
    for entry in allEntries:
        pass

'''Input: A Track
The rating of a track
TODO: Implement All
'''


def rate(track):
    payload = track['post']
#    (payload.replace(word,"") for word in track['title'].split())  # Removes all song title from post
#    for word in track['title'].split:
#        payload.replace(word,"")
    url = 'http://text-processing.com/api/sentiment/'
    request = eval(requests.post("http://text-processing.com/api/sentiment/", {"text":payload}).text)
    if(abs(float(request['probability']['pos']) - float(request['probability']['neg']) ) > 0.05):
        return request['label']  # If the difference is greater than a tolerance return result
    return 'neutral'  # Otherwise return neutral

#   return 10 * (rateEntry['probability']['pos'] - rateEntry['probability']['neg']) + 5
# ^^ Above returns a number between 1 and 10 ^^


'''Input: Takes the expanded Soundcloud URL
Returns whether or not link is valid
Put logic for the checking of whether the link is valid here
'''

regex = re.compile("((http|https)://soundcloud.com\/\S+\/\S+)")
def checkEntry(entry):
    if type(entry) is str:
        return bool(regex.match(entry)) and 'sets' not in entry
    return False


'''Input: Takes a twitter post string
Sanitizes the post to only be printable characters removing emojis and other chars 
'''


def sanitizeEntry(entry):
        return str(entry.encode('ascii',errors='ignore'))[1:].replace('/m.s','/s') #Accounts for mobile links

'''Input: None
Returns a list with all ids in ids.txt
'''
def readinIDs():
        idlist = list()
        infile = open(idfilename,'r')
        for line in infile:
                idlist.append(line)
        infile.close()  
        return idlist

'''Input: entries and the filename to output to
Outputs all the IDs to a file to avoid duplicate results
'''


def outputIDsToFile(entries):
        infile = open(idfilename,"a")
        for entry in entries:
                infile.write(str(entry['id'])+'\n')
        infile.close
                                

'''Input: entries and the filename to output to
Outputs all the IDs to a file to avoid duplicate results
'''


def outputEntriesToFile(entries):
        infile =  open(entriesfilename,"r+") 
        oldEntries= readInEntries()
        if os.stat(entriesfilename)[6] != 0: #  If content in file
            try:
                if oldEntries:
                    infile.seek(0)  # Seek to the beginning in order to overwrite not append
                    infile.write(str(oldEntries + entries))  # Append if something exists
                    logging.info("Outputted entries to  %s succesfully" % entriesfilename)
                else:
                    logging.info("No old files")
                    infile.seek(0)
                    infile.write(str(entries))  # If empty then create
                infile.close()
                    
            except:
                logging.warning("Unable to output entries to file %s " % entriesfilename)
        
'''Input:None
Returns dictionary externally stored
'''


def readInEntries():
    with open(entriesfilename,'r') as infile:
        if os.stat(entriesfilename)[6] != 0: #  If content in file
            try:
                currentLine = eval(infile.read())
                return currentLine
            except TypeError:
                logging.warning('Cant parse entry at %s' % infile.read())
        return []

'''Input: Track
Checks to see if song already exists in database
TODO: Add logic to find if song already exists
whether by identical URL or similar Artist / Track
'''


def songExists():
    return False
    #return (song in database)
        
