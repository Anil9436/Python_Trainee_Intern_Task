import pytest
from flask import Flask
from app import app

def client():
    client=app.test_client()
    return client


