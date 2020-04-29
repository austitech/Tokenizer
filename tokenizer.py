
from token import Token, tokentype


class StringTokenizer:
    def __init__(self, text=''):
        self.text = text
        self.pos = 0  # act as a cursor within self.text
        self.current_char = self.text[self.pos]

    def advance(self):
        """
            increment self.pos by 1.
            if self.pos is greater than length of self.text
                set self.current_char to character on index
                self.pos in self.text
            else
                set self.current_char to None
        """
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        """Skips spaces in the text that are not quoted"""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_integer(self):
        """returns an integer when called"""
        string = ''
        while self.current_char is not None and self.current_char.isdigit():
            string += self.current_char
            self.advance()
        return int(string)

    def number(self):
        """recognizes and returns an integer or float token"""
        integer = self.get_integer()
        if self.current_char == '.':
            self.advance()
            floating = float(str(integer) + str(self.get_integer()))
            return Token(tokentype['FLOAT'], floating)
        return Token(tokentype['INT'], integer)

    def identifier(self):
        """recognizes and returns an identifier token"""
        _id = ''
        while self.current_char is not None and self.current_char.isalpha():
            # inner loop to get alphanumeric characters
            while self.current_char is not None and\
                    self.current_char.isalnum():
                        _id += self.current_char
                        self.advance()
        return Token(tokentype['ID'], _id)

    def string(self):
        """recognizes and returns a string token"""
        _string = ''
        while self.current_char != '"':
            _string += self.current_char
            self.advance()
        # return CHARACTER token if length of string is less than 2
        if len(_string) == 1:
            return Token(tokentype['CHAR'], _string)
        return Token(tokentype['STRING'], _string)

    def generic_token(self, character):
        """returns single character tokens"""
        return Token(tokentype[character], character)

    def generate_token_list(self):
        """
            move through the text and generates a list of tokens
            return token_list:list
        """
        token_list = []
        while self.current_char is not None:
            # handle whitespaces
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # handle integer and float numbers
            if self.current_char.isdigit():
                token_list.append(self.number())
                continue

            # handle identifiers e.g variable names
            if self.current_char.isalpha():
                token_list.append(self.identifier())
                continue

            # handle strings e.g "Hello, World"
            if self.current_char == '"':
                self.advance()  # skip opening quote
                token_list.append(self.string())
                self.advance()  # skip closing quote
                continue

            # handle single characters e.g symbols
            if self.current_char in tokentype.keys():
                char = self.current_char
                self.advance()
                token_list.append(self.generic_token(char))
                continue
        # add token to indicate end of file (EOF)
        token_list.append(Token(tokentype['EOF'], None))

        return token_list
