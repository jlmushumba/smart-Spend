import json
import services.budget_service as budget_service


def test_add_budget(tmp_path, monkeypatch):
    file = tmp_path / "budgets.json"
    file.write_text("[]")

    monkeypatch.setattr(
        budget_service,
        "file_path",
        str(file)
    )

    budget_service.add_budget(
        1,
        "Food",
        100000,
        "08/2026"
    )

    with open(file) as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["id"] == 1


def test_view_budget(tmp_path, monkeypatch):
    file = tmp_path / "budgets.json"

    data = [
        {
            "id": 1,
            "category": "Food",
            "monthly_limit": 100000,
            "month_year": "08/2026"
        }
    ]

    file.write_text(json.dumps(data))

    monkeypatch.setattr(
        budget_service,
        "file_path",
        str(file)
    )

    assert budget_service.view_budget() == data


def test_edit_budget(tmp_path, monkeypatch):
    file = tmp_path / "budgets.json"

    data = [
        {
            "id": 1,
            "category": "Food",
            "monthly_limit": 100000,
            "month_year": "08/2026"
        }
    ]

    file.write_text(json.dumps(data))

    monkeypatch.setattr(
        budget_service,
        "file_path",
        str(file)
    )

    budget_service.edit_budget(
        {"monthly_limit": 150000},
        1
    )

    with open(file) as f:
        updated = json.load(f)

    assert updated[0]["monthly_limit"] == 150000


def test_delete_budget(tmp_path, monkeypatch):
    file = tmp_path / "budgets.json"

    data = [
        {"id": 1, "category": "Food"},
        {"id": 2, "category": "Transport"}
    ]

    file.write_text(json.dumps(data))

    monkeypatch.setattr(
        budget_service,
        "file_path",
        str(file)
    )

    assert budget_service.delete_budget(1) is True

    with open(file) as f:
        updated = json.load(f)

    assert len(updated) == 1
    assert updated[0]["id"] == 2


def test_delete_nonexistent_budget(tmp_path, monkeypatch):
    file = tmp_path / "budgets.json"

    file.write_text(
        json.dumps([
            {"id": 1, "category": "Food"}
        ])
    )

    monkeypatch.setattr(
        budget_service,
        "file_path",
        str(file)
    )

    assert budget_service.delete_budget(99) is False