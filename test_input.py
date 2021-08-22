from test import client
from flask import json
def test_wrong_http_request(client):
    response=client.get('/v1/sanitized/input/')
    assert response.status_code==405

def test_input_sanitized(client):
    response=client.post('/v1/sanitized/input/',data=dict(payload="normal input does not produce risk"))
    assert response.status_code==200
    assert b'sanitized' in response.get_data()


def test_input_unsanitized_dash(client):
    response=client.post('/v1/sanitized/input/',data=dict(payload="this input --  willproduce risk"))
    assert response.status_code==400
    assert b'unsanitized' in response.get_data()
        

def test_input_unsanitized_quote(client):
    response=client.post('/v1/sanitized/input/',data=dict(payload="this input '  will produce risk"))
    assert response.status_code==400
    assert b'unsanitized' in response.get_data()



        
def test_input_unsanitized_comment(client):
    response=client.post('/v1/sanitized/input/',data=dict(payload="this input */  will produce risk"))
    assert response.status_code==400
    assert b'unsanitized' in response.get_data()


def test_input_unsanitized_one_line_comment(client):
    response=client.post('/v1/sanitized/input/',data=dict(payload="this input /* will  produce risk"))
    assert response.status_code==400
    assert b'unsanitized' in response.get_data()


def test_input_unsanitized_semicolon(client):
    response=client.post('/v1/sanitized/input/',data=dict(payload="this input ;  can produce risk"))
    assert response.status_code==400
    assert b'unsanitized' in response.get_data()

def test_input_unsanitized_hashtag(client):
    response=client.post('/v1/sanitized/input/',data=dict(payload="this input #  can produce risk"))
    assert response.status_code==400
    assert b'unsanitized' in response.get_data()

def test_input_unsanitized_or(client):
    response=client.post('/v1/sanitized/input/',data=dict(payload="this input OR 1=1 can have risk"))
    assert response.status_code==400
    assert b'unsanitized' in response.get_data()