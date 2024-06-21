import requests
from task_02_requests import fetch_and_print_posts, fetch_and_save_posts
from test_runner import test_functions


def test_fetch_and_print_posts():
    """Test if posts are fetched and printed."""
    # Redirect stdout to capture print statements
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Run the function and capture its output
    fetch_and_print_posts()
    sys.stdout = sys.__stdout__

    # Checking status code print
    assert "Status Code: 200" in captured_output.getvalue(), "Status code print is missing or incorrect."

    # Check if titles are printed (simple presence check)
    assert "sunt aut facere repellat provident occaecati excepturi optio reprehenderit" in captured_output.getvalue(), "Post titles are not being printed correctly."


def test_fetch_and_save_posts():
    """Test if posts are fetched and saved to CSV."""
    # Ensure the CSV is created
    import os
    import csv
    fetch_and_save_posts()
    assert os.path.exists('posts.csv'), "The CSV file was not created."

    # Check if CSV has content
    with open('posts.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = list(reader)

        # Check headers
        assert headers == ['id', 'title', 'body'], "CSV headers are incorrect."

        # Check if data is not empty
        assert data, "CSV file contains no data."

    # Cleanup
    os.remove('posts.csv')

def test_fetch_fail():
    """Test if fetch fails."""
    # Check for edge case: handle request failure
    original_get = requests.get
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 404
            def json(self):
                return {}
        return MockResponse()

    requests.get = mock_get
    try:
        fetch_and_save_posts()
        with open('posts.csv', newline='', encoding='utf-8') as f:
            # File shouldn't exist
            pass
    except FileNotFoundError:
        pass
    finally:
        requests.get = original_get

if __name__ == "__main__":
    test_functions([test_fetch_and_print_posts, test_fetch_and_save_posts, test_fetch_fail])
