import click

@click.group()
def cli():
    pass

@cli.command(name = "palindrome")
@click.argument("value", type = click.STRING)
def is_palindrome(value):
    value = value.lower()
    value = ''.join(char for char in value if char.isalpha())
    is_val = value == value[::-1] # check condition true or false
    val = "Yes" if is_val == True else "No"
    print(f'\nString: {value} \nIs palindrome? {val}\n')

if __name__ == '__main__':
    cli()

# Checking for char.isalpha() lets you ignore everything that's not a letter
# (when combined with the n = n.lower(), it basically checks for only lowercase letters)
# That way, you ignore all the punctuation and whitespace

# How To Run in Terminal
# ON FOLDER PROJECT/
# python3 d_palindrome.py palindrome "Saya ingin pergi ke pasar"
# python3 d_palindrome.py palindrome "Kasur ini rusak"
# python3 d_palindrome.py palindrome "Ibu Ratna antar ubi"
# python3 d_palindrome.py palindrome "Aku suka rajawali, bapak. Apabila wajar, aku suka."
