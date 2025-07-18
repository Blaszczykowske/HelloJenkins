from main import say_hello

def test_say_hello(capfd):
    say_hello()
    out, _ = capfd.readouterr()
    assert "Hello from Python" in out