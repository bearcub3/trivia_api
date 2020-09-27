# API Testing

**Why test an API?**    

- To confirm expected request handling behavior
- To confirm success-response structure is correct
- To confirm expected errors are handled appropriately
- To confirm CRUD operations persist

If bugs are discovered while in development, they cost next to nothing to fix and don't have any negative impact on business outcomes or client experience. But if bugs make it to production, their cost can be quite large—they can impact performance, and fixing bugs can take large amounts of time for big, production applications.
The order of operations for app development should always be:

1. Development
2. Unit Testing
3. Quality Assurance
4. Production    

Step 2 is essential to ensuring the application is production-ready and time-to-production is used efficiently.

## Unittest Flask Key Structures

As we just saw, all of your Flask application tests will follow the same format:

1. Define the `test case class` for the application (or section of the application, for larger applications).
2. Define and implement the `setUp function`. It will be executed before each test and is where you should initialize the app and test client, as well as any other context your tests will need. The Flask library provides a test client for the application, accessed as shown below.
3. Define the `tearDown method`, which is implemented after each test. It will run as long as setUp executes successfully, regardless of test success.
4. Define your `tests`. All should `begin with "test_"` and include a doc string about the purpose of the test. In defining the tests, you will need to:
    1. Get the response by having the client make a request
    2. Use self.assertEqual to check the status code and all other relevant operations.
5. Run the test suite, by running `python test_file_name.py` from the command line.

```
class AppNameTestCase(unittest.TestCase):
    """This class represents the ___ test case"""

    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""
        self.client = app.test_client
        pass

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_given_behavior(self):
        """Test _____________ """
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
unittest.main()
```

## Test-Driven Development (TDD) for APIs

**Test-Driven Development (or TDD)** is a software development paradigm used very commonly in production.
It is based on a short, rapid development cycle in which tests are written before the executable code and constantly iterated on.

1. Write test for specific application behavior.
2. Run the tests and watch them fail.
3. Write code to execute the required behavior.
4. Test the code and rewrite as necessary to pass the test
5. Refactor your code.
6. Repeat - write your next test.

Often while pair programming, one partner will write the test and the other will write the executable code, after which the partner will switch. This process is helpful for checking assumptions about behavior and making sure all expected behavior is captured.
