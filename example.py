from tokenizer import StringTokenizer
from token import tokentype


text = open('test.ex', 'r').read()

t = StringTokenizer(text=text, tokentype=tokentype)

token_list = t.generate_token_list()

print(token_list)
