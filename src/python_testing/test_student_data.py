from src.python_testing.student_data import StudentDB

def setup_module(module):
    print("------SetUp------")
    global db
    db=StudentDB()
    db.connect('src/python_testing/data.json')

def teardown_module(module):
    print("------TearDown------")
    db.close()
def test_scott_data():

    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark_data():
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
