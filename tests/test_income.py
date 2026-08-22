import json
import os

import services.income_service as income_service


def test_add_income(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    income_file = data_dir / "income.json"
    income_file.write_text("[]")

    monkeypatch.chdir(tmp_path)

    income_service.add_income(
        1,
        "Salary",
        850000.0,
        "01/08/2026",
        "August salary"
    )

    with open(income_file) as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["id"] == 1
    assert data[0]["source"] == "Salary"
    assert data[0]["amount"] == 850000.0


def test_view_income(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    income_file = data_dir / "income.json"

    data = [
        {
            "id": 1,
            "source": "Salary",
            "amount": 850000.0,
            "date": "01/08/2026",
            "description": "August salary"
        }
    ]

    income_file.write_text(json.dumps(data))

    monkeypatch.chdir(tmp_path)

    result = income_service.view_income()

    assert result == data


def test_view_income_missing_file(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    monkeypatch.chdir(tmp_path)

    result = income_service.view_income()

    assert result is None


def test_delete_income(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    income_file = data_dir / "income.json"

    data = [
        {"id": 1, "source": "Salary", "amount": 850000},
        {"id": 2, "source": "Rent", "amount": 1000000}
    ]

    income_file.write_text(json.dumps(data))

    monkeypatch.chdir(tmp_path)

    result = income_service.delete_income(1)

    assert result is True

    with open(income_file) as file:
        updated = json.load(file)

    assert len(updated) == 1
    assert updated[0]["id"] == 2


def test_delete_nonexistent_income(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    income_file = data_dir / "income.json"

    income_file.write_text(
        json.dumps([
            {
                "id": 1,
                "source": "Salary",
                "amount": 850000
            }
        ])
    )

    monkeypatch.chdir(tmp_path)

    result = income_service.delete_income(99)

    assert result is False


def test_edit_income(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    income_file = data_dir / "income.json"

    data = [
        {
            "id": 1,
            "source": "Salary",
            "amount": 850000,
            "date": "01/08/2026",
            "description": "Salary"
        }
    ]

    income_file.write_text(json.dumps(data))

    monkeypatch.chdir(tmp_path)

    income_service.edit_income(
        {
            "source": "Freelance",
            "description": "Freelance work"
        },
        1
    )

    with open(income_file) as file:
        updated = json.load(file)

    assert updated[0]["source"] == "Freelance"
    assert updated[0]["description"] == "Freelance work"
    assert updated[0]["amount"] == 850000


def test_recent_id(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    income_file = data_dir / "income.json"

    income_file.write_text(
        json.dumps([
            {"id": 1},
            {"id": 2},
            {"id": 5}
        ])
    )

    monkeypatch.chdir(tmp_path)

    assert income_service.recent_id() == 5


def test_recent_id_empty_file(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    income_file = data_dir / "income.json"
    income_file.write_text("[]")

    monkeypatch.chdir(tmp_path)

    assert income_service.recent_id() == 0


def test_recent_id_invalid_json(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    income_file = data_dir / "income.json"
    income_file.write_text("INVALID JSON")

    monkeypatch.chdir(tmp_path)

    assert income_service.recent_id() == 0