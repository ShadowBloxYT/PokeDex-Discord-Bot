import requests
import re
from html.parser import HTMLParser
from collections import defaultdict

class MyHTMLParser(HTMLParser):

    _parseHeader = False
    _targetHeader = "h3"
    _targetRow = "tr" 
    _appendRow = False

    def __init__(self, pat):
        super().__init__()
        self.pattern = re.compile(pat)
        self._results = []
    
    def handle_starttag(self, tag, attrs):
        if self._targetHeader == tag:
            self._parseHeader = True

        if self._targetRow == tag and attrs:
            self._appendRow = True

    def handle_endtag(self, tag):
        if self._parseHeader and self._targetHeader == tag:
            self._parseHeader = False

        if self._appendRow and self._targetRow == tag:
            self._appendRow = False
    
    def handle_data(self, data):
        if self._appendRow and data.isdigit():
            self._results.append(data)

    def return_results(self):
        return self._results

class LeaderboardData:

    def __init__(self, values, names):
        self._arr = values
        self._names = names

    def get_printable_string(self):
        result = ""
        x = 0
        try:
            for i in range(len(self._arr)//2):
                x = i
                result += "{} Ranking\n".format(self._names[i])
                result += "    Rank: {}\n".format(self._arr[i*2])
                result += "    Value: {}\n\n".format(self._arr[i*2+1])
        except IndexError:
            error = 1

        return result if result != "" else "No leaderboard data found"

    def get_dict(self):
        result = defaultdict(int)
        for i in range(len(self._names)):
            result[self._names[i]] = self._arr[i]
            
        return result

def get_data(board, username, names):
    r = requests.get("https://heroesandgenerals.com/leaderboard/{}/?gamertag={}".format(board, username))
    parser = MyHTMLParser(username)
    parser.feed(r.text)
    data = LeaderboardData(parser.return_results(), names)
    return data.get_printable_string()

if __name__ == "__main__":
    target = "Mr._Pig"
    board = "overall"
    data = get_data(board, target, ["Score", "Kills", "Headshots"])

    print(data)

    target = "Zxzzxz2"
    board = "overall"
    data = get_data(board, target, ["Score", "Kills", "Headshots"])
    
    print(data)
