import pytest
from tests.functional.utils import screenshot_on_failure


@pytest.mark.functional
@screenshot_on_failure
def test(chrome):
    chrome.get("http://localhost:8000/")
    assert "PlantCrossing" in chrome.title
    assert "Welcome to PlantCrossing" in chrome.page_source
