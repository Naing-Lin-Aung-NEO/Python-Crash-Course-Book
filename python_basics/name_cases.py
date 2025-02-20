name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

name = "jhon eric"
print(name.title(),name.upper(),name.lower())

name = "Albert Einstein"
quote = '"A person who never made a mistake never tried anything new."'
name_quote = f"{name} once said, {quote}"
print(name_quote)

famous_name = "G.Clooney"
message = '"The only failure is not to Try!"'
message = f"{famous_name} once said, {message}"
print(message)

beautiful_name = "Beautiful Names:\nLin\nLet\nAung"
beautiful_name = "Beautiful Names:\n\tLin\n\tLet\n\tAung"
beautiful_name = " Lin "
print(beautiful_name.__len__())
# beautiful_name = beautiful_name.lstrip()
# print(beautiful_name.__len__())
# beautiful_name = beautiful_name.rstrip()
# print(beautiful_name.__len__())
beautiful_name = beautiful_name.strip()
print(beautiful_name.__len__())

file_name = "python_notes.txt"
file_name = file_name.removesuffix(".txt")
print(file_name)

website = "https://neo.com"
website = website.removeprefix("https://")
print(website)




