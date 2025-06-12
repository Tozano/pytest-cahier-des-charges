import json

def test_ping(client):
    r = client.get('/ping')
    assert r.status_code == 200
    assert r.get_json() == {"message": "pong"}

def test_analyse_valide(client):
    payload = {"x": [0,1,2], "y": [0,2,4]}
    r = client.post('/analyse', data=json.dumps(payload),
                    content_type='application/json')
    assert r.status_code == 200
    data = r.get_json()
    assert round(data["a"],3) == 2.0
    assert round(data["b"],3) == 0.0

def test_analyse_erreur(client):
    r = client.post('/analyse', json={"x": [], "y": []})
    assert r.status_code == 400
    assert "error" in r.get_json()