import click


# A function becomes a Click command line tool by decorating it through click.command().
# At its simplest, just decorating a function with this decorator will make it into a callable script:


@click.command()
@click.argument("argument")
@click.option("--another_arg", prompt="Another Arguement")
def main(argument, another_arg):
    """
    This is just check Function run it via giving one arguement
    e.g python click-learning.py 'arguement name'
    """
    print(
        f"Click is working fine and this is the arguement passed : {argument} and {another_arg}"
    )


if __name__ == "__main__":
    main()


# import click

# @click.command()
# @click.option("--count", default=1, help="Number of greetings.")
# @click.option("--name", prompt="Your name", help="The person to greet.")
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for _ in range(count):
#         click.echo(f"Hello, {name}!")

# if __name__ == '__main__':
#     hello()
