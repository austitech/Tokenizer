# Tokenizer
This repository contains 3 modules:
+ tokenizer
+ token
+ example

## tokenizer module
class StringTokenizer  
params:
-   text: String to break into tokens
-   tokentypes: Dictionary of token names
-   keyword: Dictionary of reserved names(mostly for programming languages)

the most important method is create_token_generator; builds and returns  
a generator object which yields the tokens when needed.

## token module
class Token  
params:
-   type: Name of token
-   value: token value

represents a token object.

## example module
serves as a pointer for however needs help

# Usage
Before you can successfully use StringTokenizer, you must create a dictionary  
of token types and values example:

```
tokentype = {
    "INT": "INT",
    "FLOAT": "FLOAT",
    "<": "GT"
}
```

or you can import the default in the token module if it matches your use case.


# Complete Example

### make imports

```
from tokenizer import StringTokenizer
from token import tokentype
```

### create instance of StringTokenizer class and dummy text

```
text = """
    names = "Josiah Augustine"
    nick = "Austitech"
    age = 25
    occupation = "Student"
"""

lexer = StringTokenizer(text=text, tokentype=tokentype)
```

### get generator object to yield tokens

```
token_generator = lexer.create_token_generator()
```

### conclusion
Use generator object to yield tokens where needed examples:

```
# get single token
token = next(token_generator)

# using a loop
for token in token_generator:
    print(token)
```

# Contributions
Contribution and suggestion of ways to improve is welcome
