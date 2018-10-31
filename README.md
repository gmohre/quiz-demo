## Quiz Application

### Create Test
#### POST 
#### Data Parameters
- /api/test/
{
  'name',
  'duration',
  'questions':
    {
      'question',
      'answers':
        [
	  {
	    'answer',
	    'is_correct'
	  }
    }
}

### Create Assessment
#### POST
- /api/assessment/

### Create Response
##### POST
- /api/assessment/
#### Data Parameters
{
  'fname',
  'lname',
  'email',
  'test_id'
}
