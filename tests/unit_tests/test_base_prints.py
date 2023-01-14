import pytest
from py_common.sp_base import m_print

def test_print_line_separator_with_title(capsys):
	'''Main path test to assert if custom separator print function prints separator'''
	m_print.print_line_separator_with_title(" Text ", "-", 10)
	out, err = capsys.readouterr()
	assert out.strip() == "-- Text --"

def test_hello_world_separator_length_more_than_1():
	'''Alternate path test to assert if custom separator returns exception if separator is longer than 1 sign'''
	with pytest.raises(Exception) as exc_info:
		m_print.print_line_separator_with_title(" Text ", "--", 10)
	assert exc_info.type == Exception
	assert exc_info.value.args[0] == 'Separator length not equal to 1'

def test_hello_world_separator_title_longer_than_separator_length():
	'''Alternate path test to assert if custom separator returns exception if title is longer than defined separator length'''
	with pytest.raises(Exception) as exc_info:
		m_print.print_line_separator_with_title(" Text ", "-", 3)
	assert exc_info.type == Exception
	assert exc_info.value.args[0] == 'Title length greater than line_length'