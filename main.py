'''
To clarify - you need not create an image - just need a dictionary style representing this tree: e.g. output format
    {employeeID: xx, name: yy, reportees: [
        {employeeID: xx1, name: yy1, reportees: [
            {employeeID: xx11, name: yy22}}
        ], {employeeID xx2, name: yy2, reportees: []}
    ],}
'''
import pandas
from pprint import pprint


td = pandas.read_excel('./hierarchy case/data.xlsx').to_numpy()


def get_manager_id(employee):
    return employee[5]


Reportees = {}
Root = None


num = 1
for row in td:
    manager_id = get_manager_id(row)
    if not isinstance(manager_id, str):
        Root = row
        continue

    if manager_id in Reportees.keys():
        Reportees[manager_id].append(
            {
                'employeeId': row[1],
                'name': row[4],
            }
        )
    else:
        Reportees[manager_id] = [{
            'employeeId': row[1],
            'name': row[4],
        }]



Tree = {
    'employeeId': Root[1],
    'name': Root[4],
}

print("Len of reportees", len(Reportees.keys()))

foo = Reportees.pop(Tree['employeeId'])
Tree['reportees'] = foo
print("Len of reportees", len(Reportees.keys()))

pprint(Tree, indent=2)