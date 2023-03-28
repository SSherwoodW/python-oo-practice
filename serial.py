"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        """Create new generator, starting at start number."""
        self.start = self.nxt = start
        
    def __repr__(self):
        """Represent series(start number and next number)."""
        return f"(SerialGenerator start={self.start}, next={self.nxt})"

    def generate(self):
        """Return the next number in the sequence"""
        self.nxt += 1
        return self.nxt - 1
            
    def reset(self):
        """Reset number to original start number"""
        self.nxt = self.start
