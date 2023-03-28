"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine used to generate a random word from a file 
    >>> wf = WordFinder('simple.txt')
    5 words read

    >>> wf.random_word() in ['blueberry', 'blackberry', 'raspberry', 'starberry', 'strawberry']
    True

    >>> wf.random_word() in ['blueberry', 'blackberry', 'raspberry', 'starberry', 'strawberry']
    True

    >>> wf.random_word() in ['blueberry', 'blackberry', 'raspberry', 'starberry', 'strawberry']
    True

    >>> wf.random_word() in ['blueberry', 'blackberry', 'raspberry', 'starberry', 'strawberry']
    True

    >>> wf.random_word() in ['blueberry', 'blackberry', 'raspberry', 'starberry', 'strawberry']
    True
    
    """
    
    def __init__(self, path):
        """Create new WF instance and print number of words read from file."""
        dict_file = open(path)

        self.words = self.parse(dict_file)

        print (f"{len(self.words)} words read")

    def __repr__(self):
        """Representation of WordFinder."""
        return f"(WordFinder: {self.words})"

    def parse(self, dict_file):
        """Return list of words from words in file"""
        return [w.strip() for w in dict_file]
    
    def random_word(self):
        """From words list, return random word"""
        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder to generate a random word from a file if not 
        empty space or starts with '#'
    >>> swf = SpecialWordFinder('complex.txt')
    4 words read
    >>> swf.random_word() in ["kale", "parsnips", "apple", "mango"]
    True
    >>> swf.random_word() in ["kale", "parsnips", "apple", "mango"]
    True
    >>> swf.random_word() in ["kale", "parsnips", "apple", "mango"]
    True
    >>> swf.random_word() in ["kale", "parsnips", "apple", "mango"]
    True
    """
    def __init__(self, path):
        super().__init__(path)

    def parse(self, dict_file):
        return [w.strip() for w in dict_file 
                if w.strip() and not w.startswith("#")]
