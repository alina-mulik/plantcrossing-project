from utils import to_bytes


# def test_normalize_path():
#     test = {
#         "123": "123/",
#         "hello": "hello/",
#         "hello/": "hello/",
#         "/": "/"
#     }
#
#     for input, expected in test.items():
#         got = normalize_path(input)
#         assert got == expected, f"path '{test} normalized to '{got}, while {expected} expected"


def test_to_bytes():
    input_test_data = ["str", b"bytes"]
    expected_data = [b"str", b"bytes"]
    for c in range(len(input_test_data)):
        input_data = input_test_data[c]
        expected_data_input = expected_data[c]
        output_data = to_bytes(text=input_data)
        assert output_data == expected_data_input, f"data '{input_data} converted to '{output_data}, while {expected_data_input} expected"

# test_data = [
#     "123",
#     "hello",
#     "hello/",
#     "/",
# ]
#
# expected_data = [
#     "123/",
#     "hello/",
#     "hello/",
#     "/",
# ]
# for i in range(4):
#     t = test_data[i]
#     e = expected_data[i]
#     assert normalize_path(t) == e
#
# for i in range(4):
#     t = test_data[i]
#     e = expected_data[i]
#     g = normalize_path(t)
#     assert e == g, f"mismatch: for {t} expected {e}, got {g}"
