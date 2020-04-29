from tokenizer import StringTokenizer
from token import tokentype


text = open('test.ex', 'r').read()

t = StringTokenizer(text=text, tokentype=tokentype)

token_generator = t.create_token_generator()

print(token_generator)
