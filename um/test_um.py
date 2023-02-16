from um import count

def main():
    test_upper_lower_case()
    test_words_with_um()
    test_surrouned_by_spaces()

def test_upper_lower_case():
    assert count('Um, thanks for the album.') == 1
    assert count('Um,thanks um...') == 2

def test_words_with_um():
    assert count('yummi') == 0

def test_surrouned_by_spaces():
    assert count('Hello, um world') == 1
    assert count('um?') == 1


if __name__ == "__main__":
    main()