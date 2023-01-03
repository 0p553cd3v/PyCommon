from py_common.base import hello_world 

def test_hello_world(capsys):
	'''Simple test to assert if custom hello world print function prints hello world'''
	hello_world.print_hello_world()
	out, err = capsys.readouterr()
	assert out.strip() == "Hello world"

