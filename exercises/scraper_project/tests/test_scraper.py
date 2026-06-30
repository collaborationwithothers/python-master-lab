from scraper import scrape_title

def test_scrape_title():
    # Test with a valid URL
    url = "https://www.google.com"
    title = scrape_title(url)
    assert title is not None and len(title) > 0, f"Expected a non-empty title, but got '{title}'"
    assert isinstance(title, str), f"Expected title to be a string, but got '{type(title)}'"

    # Test with an invalid URL
    invalid_url = "https://www.invalidurl.com"
    error_message = scrape_title(invalid_url)
    assert "Error fetching the URL" in error_message, f"Expected an error message, but got '{error_message}'"

    # Test with a URL that has no title
    no_title_url = "https://httpbin.org/html"
    title_no_title = scrape_title(no_title_url)
    assert title_no_title == "No title found", f"Expected 'No title found', but got '{title_no_title}'"