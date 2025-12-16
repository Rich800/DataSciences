import requests

BASE_URL = "http://localhost:8000"  

def test_status():
    response = requests.get(f"{BASE_URL}/status")
    assert response.status_code == 200
    assert response.json() == 1  # L'API doit renvoyer 1 si elle fonctionne

def test_permissions_valid_user():
    response = requests.get(f"{BASE_URL}/permissions", auth=("valid_user", "password"))
    assert response.status_code == 200
    # S'ssurer que la réponse contient bien les informations sur les permissions
    assert "permissions" in response.json()

def test_sentiment_v1_valid():
    response = requests.post(f"{BASE_URL}/v1/sentiment", json={"text": "I love this!"}, auth=("valid_user", "password"))
    assert response.status_code == 200
    sentiment_score = response.json().get("score")
    assert sentiment_score == 1  # Le sentiment "I love this!" devrait être positif

def test_sentiment_v2_valid():
    response = requests.post(f"{BASE_URL}/v2/sentiment", json={"text": "I hate this!"}, auth=("valid_user", "password"))
    assert response.status_code == 200
    sentiment_score = response.json().get("score")
    assert sentiment_score == -1  # Le sentiment "I hate this!" devrait être négatif

