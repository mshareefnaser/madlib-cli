import pytest
from madlib_cli.madlib import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    '''a test to check reading files from specific path function --> read_template(path)'''
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_parse_template():
    '''a test to check the parsing process,
      the function takes a string and return parts which inside curly braces '{}'
      and the string after extracting them '''
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}.")
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# @pytest.mark.skip("pending")
def test_merge():
    ''' a test to check merge function which merge the arguments with the text'''
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():
    ''' a test check the error handling of non existing file path '''
    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
