import click


@click.group()
def math():
    """Mathematical operations."""


@math.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def add(a, b):
    """Add two numbers."""
    result = a + b
    click.echo(f"Result of addition: {result}")


@math.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract(a, b):
    """Subtract two numbers."""
    result = a - b
    click.echo(f"Result of subtraction: {result}")


@math.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply(a, b):
    """Multiply two numbers."""
    result = a * b
    click.echo(f"Result of multiplication: {result}")


@math.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def division(a, b):
    """Multiply two numbers."""
    try:
        result = a / b
    except ZeroDivisionError as error:
        print(f"Zero Division Error : {error}")

    click.echo(f"Result of multiplication: {result}")


if __name__ == "__main__":
    math()
