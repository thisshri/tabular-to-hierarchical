import pandas
from pprint import pprint


Reportees = {}
HierarchyTree = None

for row in pandas.read_excel('./hierarchy case/data.xlsx').to_numpy():
    manager_id = row[5]
    data = {
        'employeeId': row[1],
        'name': row[4],
    }

    if not isinstance(manager_id, str):
        HierarchyTree = data
        continue

    if manager_id in Reportees.keys():
        Reportees[manager_id].append(data)
    else:
        Reportees[manager_id] = [data]


def populate_reportees(reportees_data):
    for reportees in reportees_data:
        if reportees['employeeId'] in Reportees.keys():
            reportees['reportees'] = Reportees.pop(reportees['employeeId'])
            populate_reportees(reportees['reportees'])
        else:
            reportees['reportees'] = []


HierarchyTree['reportees'] = Reportees.pop(HierarchyTree['employeeId'])
populate_reportees(HierarchyTree['reportees'])

pprint(HierarchyTree)
