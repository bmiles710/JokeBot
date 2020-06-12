"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""
import pytest
from my_module.functions import remove_punctuation, prepare_text, is_question, remove_punctuation, prepare_text, is_question, end_chat, detect_knock_knock, detect_walk_into_bar, detect_what_do_you_call, detect_how_are_you, detect_appreciate


# import functions
#from functions import remove_punctuation, prepare_text, is_question, end_chat, detect_knock_knock, detect_walk_into_bar, detect_what_do_you_call, detect_how_are_you, detect_appreciate

#from functions import end_chat, detect_knock_knock, detect_walk_into_bar, detect_what_do_you_call, detect_how_are_you, detect_appreciate

#!pytest Desktop/ProjectTemplate/my_module/test_functions.py

    
input_rp = "Hello!"

def test_remove_punctuation(monkeypatch):
    monkeypatch.setattr('sys.stdin', input_rp)
    assert remove_punctuation(input_rp) == "Hello"

input_pt = "Hello! I am JokeBot"

def test_prepare_text(monkeypatch):
    monkeypatch.setattr('sys.stdin', input_pt)
    assert prepare_text(input_pt) == ["hello", "i", "am", "jokebot"]    
    
input_iq = "Am I JokeBot?"

def test_is_question(monkeypatch):
    monkeypatch.setattr('sys.stdin', input_iq)
    assert is_question(input_iq) == True
    
    
input_ec = "quit"

def test_end_chat(monkeypatch):
    monkeypatch.setattr('sys.stdin', input_ec)
    assert end_chat(input_ec) == True
   
    
input_dkk = "knock"

def test_detect_knock_knock(monkeypatch):
    monkeypatch.setattr('sys.stdin', input_dkk)
    assert detect_knock_knock(input_dkk) == True
    
input_dwib = "bar"

def test_detect_walk_into_bar(monkeypatch):
    monkeypatch.setattr('sys.stdin', input_dwib)
    assert detect_walk_into_bar(input_dwib) == True

    
input_dwdyc = "what do you call"

def test_detect_what_do_you_call(monkeypatch):
    monkeypatch.setattr('sys.stdin', input_dwdyc)
    assert detect_what_do_you_call(input_dwdyc) == True
    
    
input_dhay = ["how", "are", "you"]

def test_detect_how_are_you(monkeypatch):
    monkeypatch.setattr('sys.stdin', input_dhay)
    assert detect_how_are_you(input_dhay) == True
    
    
input_da = ["thank", "you"]

def test_detect_appreciate(monkeypatch):
    monkeypatch.setattr('sys.stdin', input_da)
    assert detect_appreciate(input_da) == True
