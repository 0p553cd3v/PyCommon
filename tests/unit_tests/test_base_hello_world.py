import os
import pytest
from base import hello_world 

@pytest.mark.unit
def test_hello_world(capsys):
	hello_world.print_hello_world()
	out, err = capsys.readouterr()
	assert out.strip() == "Hello world"

