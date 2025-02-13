import pytest
from src.database import create_tables, store_form

def test_create_tables():
    create_tables()  # Ensure no errors

def test_store_form():
    store_form("data/json_output/sample_output.json")  # Ensure no errors