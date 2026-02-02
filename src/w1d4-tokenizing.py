import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4.1-mini")
tokens = encoding.encode("Hello this is prabin")
print("Tokens:", tokens)

for token_id in tokens: 
    token_text = encoding.decode([token_id])
    print(f"Token ID: {token_id}, Token Text: {token_text}")


print(f"The token 6997 is: {encoding.decode([6997])}")