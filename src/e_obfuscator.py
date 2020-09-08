import click

@click.group()
def cli():
    pass

@cli.command(name = "obfuscator")
@click.argument("value", type = click.STRING)
def obfuscator(value):
    value = list(value)
    # print(ord(text[0])) return 101
    # ord sama seperti charCodeAt di js untuk dapetin code numbernya
    print(''.join(list(map(lambda char: f"&#{ord(char)};", value))))


if __name__ == '__main__':
    cli()

# How To Run in Terminal
# ON FOLDER PROJECT/
# python3 e_obfuscator.py obfuscator "email@example.com"


# Contoh waktu di Javascript gunain charCodeAt
# program
#     /** 1.Add */
#     .command('obfuscate', 'obfuscate a string')
#     .argument('<word>')
#     .action(({
#         logger,
#         args
#     }) => {
#         logger.info(args.word.split('').map(char => `&#${char.charCodeAt(0)};`).join(''))
#     })

# program.run()