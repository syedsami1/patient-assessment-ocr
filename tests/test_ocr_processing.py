import pytest
from src.ocr_processing import extract_text, extract_data

def test_extract_text():
    text = extract_text("data/sample_forms/sample_form.jpg")
    assert isinstance(text, str)
    assert len(text) > 0

def test_extract_data():
    sample_text = "Patient Name: John Doe\nDate of Birth: 01/01/1990"
    data = extract_data(sample_text)
    assert data["patient_name"] == "John Doe"
    assert data["dob"] == "01/01/1990"