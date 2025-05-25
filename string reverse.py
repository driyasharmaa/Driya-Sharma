class StringReverser:
    def __init__(self,text):
        self.text = text
    def reverse_words(self):
        words = self.text.strip().split()
        reversed_words = words[::-1]
        return ''.join(reversed_words)
    
# example usage
s = StringReverser("Hello I'm Driya")
print(s.reverse_words()) 