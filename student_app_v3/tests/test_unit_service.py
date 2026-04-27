import pytest
from unittest.mock import patch

from student_app_v3.app.service import (
    add_student,
    ServiceAppLogicError,
    get_student
)


@pytest.mark.jira_key("SAV-1")
@patch("student_app_v3.app.service.db.get_student",
       return_value={"id": 101, "name": "Eldar", "age": 35})
def test_sav_1_get_student_positive(mock_get_student):
    student = get_student(101)

    assert student["id"] == 101
    assert student["name"] == "Eldar"
    assert student["age"] == 35


@pytest.mark.jira_key("SAV-1")
@patch("student_app_v3.app.service.db.add_student",
       side_effect=ServiceAppLogicError("Student age is out of range"))
def test_sav_1_add_student_underage_fail(mock_add_student):
    invalid_student = {"name": "Eldar", "age": 17}

    with pytest.raises(ServiceAppLogicError) as excinfo:
        add_student(invalid_student)

    assert "Student age is out of range" in str(excinfo.value)

