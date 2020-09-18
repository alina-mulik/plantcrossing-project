import pytest


def test(chrome):
    chrome.get("http://localhost:8000/")
    assert "PlantCrossing" in chrome.title
    assert "Welcome to PlantCrossing" in chrome.page_source
