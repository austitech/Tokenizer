from tokenizer import StringTokenizer


text = open('test.ex', 'r').read()

t = StringTokenizer(text)

token_list = t.generate_token_list()

print(token_list)
