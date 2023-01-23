from project import player_choice, replay, full_board_check, free_space_check
from io import StringIO
import pytest

def main():
    test_player_choice()
    test_replay()
    test_full_board_check()
    test_free_space_check()


def test_player_choice(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('1\n'))
    assert player_choice(["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]) == 1
    monkeypatch.setattr('sys.stdin', StringIO('  2\n'))
    assert player_choice(["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]) == 2

def test_replay(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('y\n'))
    assert replay() == True
    monkeypatch.setattr('sys.stdin', StringIO('n\n'))
    assert replay() == False
    monkeypatch.setattr('sys.stdin', StringIO('Yes\n'))
    assert replay() == True
    monkeypatch.setattr('sys.stdin', StringIO('NO\n'))
    assert replay() == False
    monkeypatch.setattr('sys.stdin', StringIO('yes\n'))
    assert replay() == True
    
def test_full_board_check():
    assert full_board_check(["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]) == False
    assert full_board_check(["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]) == True
    assert full_board_check(["#", "X", "O", "X", "O", " ", "X", "O", " ", "X"]) == False
    

def test_free_space_check():
    assert free_space_check(["#", " ", " ", " ", " ", " ", " ", " ", " ", " "], 1) == True
    assert free_space_check(["#", " ", " ", " ", " ", "X", " ", " ", " ", " "], 5) == False
    assert free_space_check(["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"], 8) == False
    assert free_space_check(["#", "X", "O", "X", " ", "X", "O", "X", "O", "X"], 4) == True

