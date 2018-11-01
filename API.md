## Quiz Application

### Create Test
#### POST
#### Data Parameters
- /api/test/
`{
  'name': string
  'duration': integer
  'message' : string
  'questions': list of Question objects
    [
      'question': string
      'answers': list of Answer objects
        [
	  {
	    'answer': string
	    'is_correct': boolean
	  },
	],
    ]
}`

### Create Assessment
#### POST
- /api/assessment/
`{
  'fname': string
  'lname': string
  'email': string
  'test_id': id of Test object
}`
### Create Response
##### POST
- /api/response/
#### Data Parameters
`{
  'assessment': id of Assessment object,
  'question': id of Question object,
  'answer' : id of Answer object
}`


