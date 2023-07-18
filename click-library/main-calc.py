from calculator import calculator
import click


@click.command()
@click.option(
    "--operation",
    "--op",
    type=click.Choice(["add", "subtract", "multiply", "divide"]),
    prompt="Enter the Operation : ",
)
@click.argument("operands", nargs=2, type=float)
def calc_operator(operation, operands):
    """
    This Function is used for performing basic calculator operations.\n
    e.g \n
    python main-calc.py --op add 4 5
    python main-calc.py --op multiply 4 5
    python main-calc.py --op division 4 5
    python main-calc.py --op subtract 4 5
    """

    if operation == "add":
        result = calculator.add(operands[0], operands[1])
    elif operation == "subtract":
        result = calculator.subtract(operands[0], operands[1])
    elif operation == "multiply":
        result = calculator.multiply(operands[0], operands[1])
    else:
        result = calculator.division(operands[0], operands[1])

    click.echo(f"Result : {result}")


if __name__ == "__main__":
    calc_operator()
