from py_common.base import hello_world 

def test_hello_world(capsys):
	hello_world.print_hello_world()
	out, err = capsys.readouterr()
	assert out.strip() == "Hello world"

