from fuzzy_swagger.fuzz_generator import fuzz_boolean


def test_generate_random_boolean() -> None:
    assert type(fuzz_boolean(None)) is bool
