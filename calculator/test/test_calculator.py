import pytest
from click.testing import CliRunner
from calculator.calculator import math


def test_addition():
    runner = CliRunner()
    result = runner.invoke(math, ["add", "2", "3"])
    assert result.exit_code == 0
    assert result.output.strip() == "Result of addition: 5.0"


def test_subtraction():
    runner = CliRunner()
    result = runner.invoke(math, ["subtract", "5", "2"])
    assert result.exit_code == 0
    assert result.output.strip() == "Result of subtraction: 3.0"


def test_multiplication():
    runner = CliRunner()
    result = runner.invoke(math, ["multiply", "3", "4"])
    assert result.exit_code == 0
    assert result.output.strip() == "Result of multiplication: 12.0"


def test_division():
    runner = CliRunner()
    result = runner.invoke
