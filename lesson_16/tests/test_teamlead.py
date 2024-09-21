from ..home_work_16_1 import TeamLead
import pytest


@pytest.mark.success
def test_teamlead_class_atributes():
    team_lead = TeamLead("Igor", 600, "IT", "Python", 7)

    assert hasattr(team_lead, 'name'), "Class TeamLead does't have 'name' attribute!"
    assert hasattr(team_lead, 'salary'), "Class TeamLead does't have 'salary' attribute!"
    assert hasattr(team_lead, 'department'), "Class TeamLead does't have 'department' attribute!"
    assert hasattr(team_lead, 'programming_language'), "Class TeamLead does't have 'programming_language' attribute!"
    assert hasattr(team_lead, 'team_size'), "Class TeamLead does't have 'team_size' attribute!"
