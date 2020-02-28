from collections import Counter
class Codec:
    d = {}
    i = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # s = [char for char in longUrl if s not in "!?#.,;:"]
        # for i in range(len(longUrl)):
        self.d[self.i] = longUrl
        return "http://tinyurl.com/" + str(self.i)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[int(shortUrl[19:])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))