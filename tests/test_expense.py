import json

import services.expense_service as expense_service


def test_add_expense(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    expense_file = data_dir / "expenses.json"
    expense_file.write_text("[]")

    monkeypatch.chdir(tmp_path)

    expense_service.add_expense(
        1,
        "Rent",
        450000.0,
        "02/08/2026",
        "Monthly house rent"
    )

    with open(expense_file) as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["id"] == 1
    assert data[0]["category"] == "Rent"
    assert data[0]["amount"] == 450000.0


def test_view_expense(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    expense_file = data_dir / "expenses.json"

    data = [
        {
            "id": 1,
            "category": "Rent",
            "amount": 450000,
            "date": "02/08/2026",
            "description": "Monthly house rent"
        }
    ]

    expense_file.write_text(json.dumps(data))

    monkeypatch.chdir(tmp_path)

    result = expense_service.view_expense()

    assert result == data


def test_delete_expense(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    expense_file = data_dir / "expenses.json"

    data = [
        {
            "id": 1,
            "category": "Rent",
            "amount": 450000
        },
        {
            "id": 2,
            "category": "Food",
            "amount": 50000
        }
    ]

    expense_file.write_text(json.dumps(data))

    monkeypatch.chdir(tmp_path)

    result = expense_service.delete_expense(1)

    assert result is True

    with open(expense_file) as file:
        updated = json.load(file)

    assert len(updated) == 1
    assert updated[0]["id"] == 2


def test_delete_nonexistent_expense(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    expense_file = data_dir / "expenses.json"

    expense_file.write_text(
        json.dumps([
            {
                "id": 1,
                "category": "Food",
                "amount": 50000
            }
        ])
    )

    monkeypatch.chdir(tmp_path)

    result = expense_service.delete_expense(99)

    assert result is False


def test_edit_expense(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    expense_file = data_dir / "expenses.json"

    data = [
        {
            "id": 1,
            "category": "Food",
            "amount": 50000,
            "date": "02/08/2026",
            "description": "Lunch"
        }
    ]

    expense_file.write_text(json.dumps(data))

    monkeypatch.chdir(tmp_path)

    expense_service.edit_expense(
        {
            "category": "Transport",
            "amount": 30000
        },
        1
    )

    with open(expense_file) as file:
        updated = json.load(file)

    assert updated[0]["category"] == "Transport"
    assert updated[0]["amount"] == 30000


def test_recent_id(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    expense_file = data_dir / "expenses.json"

    expense_file.write_text(
        json.dumps([
            {"id": 1},
            {"id": 4},
            {"id": 7}
        ])
    )

    monkeypatch.chdir(tmp_path)

    assert expense_service.recent_id() == 7


def test_recent_id_empty(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    expense_file = data_dir / "expenses.json"
    expense_file.write_text("[]")

    monkeypatch.chdir(tmp_path)

    assert expense_service.recent_id() == 0