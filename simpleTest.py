import unittest
import requests

class TestTaskAPI(unittest.TestCase):

    def test_1_post_task(self):
        url = "http://localhost:5000/tasks"
        data = {"name": "Homework", "status": "Incomplete"}
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=data, headers=headers)
        print("POST Response:", response.text)
        self.assertEqual('Success', response.text)

    def test_2_get_tasks(self):
        url = "http://localhost:5000/tasks"

        response = requests.get(url)
        print("GET Response:", response.text)
        self.assertIn("Homework: Incomplete", response.text)

if __name__ == '__main__':
    unittest.main()
