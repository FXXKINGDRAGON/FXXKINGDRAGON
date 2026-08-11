from fxxkingdragon import greet


def test_greet_uses_provided_name() -> None:
    assert greet("Codex") == "Hello, Codex!"


def test_greet_uses_default_name() -> None:
    assert greet() == "Hello, world!"
