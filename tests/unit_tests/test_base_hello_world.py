from py_common.sp_base import m_hello_world 

def test_hello_world(capsys):
	'''Main path test to assert if custom hello world print function prints hello world'''
	m_hello_world.print_hello_world()
	out, err = capsys.readouterr()
	assert out.strip() == "Hello world"

