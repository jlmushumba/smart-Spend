import json
import services.report_service as report_service


def test_total_expenses(tmp_path, monkeypatch):
    file = tmp_path / "expenses.json"

    file.write_text(
        json.dumps([
            {"id": 1, "amount": 100000},
            {"id": 2, "amount": 50000},
            {"id": 3, "amount": 25000}
        ])
    )

    monkeypatch.setattr(
        report_service,
        "expense_file",
        str(file)
    )

    assert report_service.total_expenses() == 175000


def test_total_income(tmp_path, monkeypatch):
    file = tmp_path / "income.json"

    file.write_text(
        json.dumps([
            {"id": 1, "amount": 500000},
            {"id": 2, "amount": 250000}
        ])
    )

    monkeypatch.setattr(
        report_service,
        "income_file",
        str(file)
    )

    assert report_service.total_income() == 750000


def test_number_of_expenses(tmp_path, monkeypatch):
    file = tmp_path / "expenses.json"

    file.write_text(
        json.dumps([
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ])
    )

    monkeypatch.setattr(
        report_service,
        "expense_file",
        str(file)
    )

    assert report_service.number_of_expenses() == 3


def test_number_of_incomes(tmp_path, monkeypatch):
    file = tmp_path / "income.json"

    file.write_text(
        json.dumps([
            {"id": 1},
            {"id": 2}
        ])
    )

    monkeypatch.setattr(
        report_service,
        "income_file",
        str(file)
    )

    assert report_service.number_of_incomes() == 2


def test_highest_expense(tmp_path, monkeypatch):
    file = tmp_path / "expenses.json"

    data = [
        {"id": 1, "amount": 100000},
        {"id": 2, "amount": 450000},
        {"id": 3, "amount": 200000}
    ]

    file.write_text(json.dumps(data))

    monkeypatch.setattr(
        report_service,
        "expense_file",
        str(file)
    )

    result = report_service.highest_expense()

    assert result["id"] == 2
    assert result["amount"] == 450000


def test_highest_income(tmp_path, monkeypatch):
    file = tmp_path / "income.json"

    data = [
        {"id": 1, "amount": 500000},
        {"id": 2, "amount": 1000000},
        {"id": 3, "amount": 250000}
    ]

    file.write_text(json.dumps(data))

    monkeypatch.setattr(
        report_service,
        "income_file",
        str(file)
    )

    result = report_service.highest_income()

    assert result["id"] == 2
    assert result["amount"] == 1000000


def test_balance(tmp_path, monkeypatch):
    income_file = tmp_path / "income.json"
    expense_file = tmp_path / "expenses.json"

    income_file.write_text(
        json.dumps([
            {"id": 1, "amount": 1000000}
        ])
    )

    expense_file.write_text(
        json.dumps([
            {"id": 1, "amount": 300000}
        ])
    )

    monkeypatch.setattr(
        report_service,
        "income_file",
        str(income_file)
    )

    monkeypatch.setattr(
        report_service,
        "expense_file",
        str(expense_file)
    )

    assert report_service.balance() == 700000