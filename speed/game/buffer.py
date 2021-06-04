from game.input_service import InputService

class Buffer:
    """
    Keeps track of the buffer, which holds all of the keys that are pressed.

    Attributes:
        _buffer: The string filled with what the user has typed.
        buflist: a list of the characters for the buffer
        times: how many times keys have been pressed. Used to keep track of where in buflist should be changed.

    """
    def flush_buffer(self):
        """ Resets the buffer
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        self._buffer = "Buffer: - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - -"

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        self.buflist = []
        i = 0
        for i in range(51):
            self.buflist.append = '-'
        self._buffer = flush_buffer(self)
        self.times = -1

    def get_buffer(self):
        """ Retreives the buffer
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        return self._buffer

   
    
    def update_buffer(self):
        """ Adds any new keys being pressed to the buffer or decides the buffer needs to be flushed.
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        key_pressed = InputService.get_letter(self)
        
        if key_pressed == "":
            pass
        elif key_pressed == "*":
            self.flush_buffer(self)
            self.times = -1
        
        else: 
            self.times = self.times + 1
            self.buflist[self.times + 7] = key_pressed
            self._buffer = ""
            for letter in self.buflist:
                self._buffer = self._buffer + self.bufflist[letter]