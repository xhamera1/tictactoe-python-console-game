from project import check_win, convert_slot, mark, change_player
import pytest

def test_check_win():
    game = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]
    game[0][0] = "O"
    game[0][1] = "X"
    game[1][1] = "O"
    game[1][0] = "X"
    assert check_win(game) == False
    game[2][2] = "O"
    assert check_win(game) == True

def test_convert_slot():
    assert convert_slot("5") == (1,1)
    assert convert_slot("1") == (0,0)
    assert convert_slot("cat") == (-1,-1)
    assert convert_slot("4") == (1,0)
    assert convert_slot("0") == (-1,-1)
    assert convert_slot("13") == (-1,-1)

def test_change_player():
    assert change_player("X") == "O"
    assert change_player("O") == "X"

def test_mark():
    game = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]
    mark("X", "1", game) 
    assert game[0][0] == "X"
    mark("O", "5", game) 
    assert game[1][1] == "O"
    with pytest.raises(ValueError):
        mark("X", "10", game)