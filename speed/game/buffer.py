# (AH) Buffer Class will interact with Director Class instead of
#       directly with Input_Service Class for more Loose Coupling.
#       So no need to import InputService.
# from game.input_service import InputService


class Buffer:
    """
    Keeps track of the buffer, which holds all of the keys that are pressed.
    (AH): Each keystroke is appended to a list.

    Attributes:
        (AH: not needed) _buffer: The string filled with what the user has typed.
        buflist: a list of the characters for the buffer
        (AH: not needed) times: how many times keys have been pressed.
                        Used to keep track of where in buflist should be changed.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Buffer): An instance of Buffer.
        """
        self.buflist = []

        # (AH) updating buflist in update_buffer Method.
        # i = 0
        # for i in range(51):
        #     self.buflist.append = '-'
        # self._buffer = flush_buffer(self)
        # self.times = -1

    def update_buffer(self, keystroke):
        """Adds any new keys being pressed to the buffer.
        (AH) Director Class will flush buffer.

        Args:
            self (Buffer): An instance of Buffer.
        """
        self.buflist.append(keystroke)

        # key_pressed = InputService
        # if key_pressed == "":
        #     pass
        # elif key_pressed == "*":
        #     self.flush_buffer(self)
        #     self.times = -1
        # else:
        #     self.times = self.times + 1
        #     self.buflist[self.times + 7] = key_pressed
        #     self._buffer = ""
        #     for letter in self.buflist:
        #         self._buffer = self._buffer + self.bufflist[letter]

    def get_buffer(self):
        """ Retrieves the buffer.
        (AH) Buffer is a list, so convert to string before Returning.

        Args:
            self (Buffer): An instance of Buffer.

        Returns:
            (AH) each keystroke is an element of buflist,
                which is joined into a single string.
        """
        # return self._buffer
        return "".join(self.buflist)

    def flush_buffer(self):
        """ Resets the buffer

        Args:
            self (Buffer): An instance of Buffer.
        """
        # (AH) reinitialize buflist to be an empty list.
        self.buflist = []

        # self._buffer = "Buffer: - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - -"
