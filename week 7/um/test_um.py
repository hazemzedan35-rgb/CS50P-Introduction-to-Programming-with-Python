from um import count


def test_single_um():
    assert count("um") == 1

def test_connected_um():
    assert count("Um, thanks for the album.") == 1
    assert count("Um? Mum? Is that you?") == 1

def test_more_one_um():
    assert count("Um, thanks, um") == 2
    assert count("um, thanks, um, for the help") == 2 

def test_bounderies():
    assert count("um....") == 1
    assert count("um... um.... um...") == 3
