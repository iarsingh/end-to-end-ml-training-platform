from fastapi.testclient import TestClient
from mltrain.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'dataset': 's3://data', 'trainer': 'train.py', 'evaluator': 'eval.py'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'dataset': 's3://data', 'trainer': 'train.py'}).json()
    assert bad["passed"] is False
    assert "missing_evaluator" in bad["failed"]
