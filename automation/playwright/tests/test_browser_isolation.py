
def test_browser_context_isolation(browser):

    # Create two independent browser contexts
    alice_context = browser.new_context()
    bob_context = browser.new_context()

    # Create one page for each user
    alice_page = alice_context.new_page()
    bob_page = bob_context.new_page()

    # Simulate Alice's authentication cookie
    alice_context.add_cookies([
        {
            "name": "session",
            "value": "alice_authenticated",
            "domain": "example.com",
            "path": "/",
        }
    ])

    # Retrieve cookies from both contexts
    alice_cookies = alice_context.cookies()
    bob_cookies = bob_context.cookies()

    # Verify Alice has her session cookie
    assert len(alice_cookies) == 1
    assert alice_cookies[0]["value"] == "alice_authenticated"

    # Verify Bob does not have Alice's session cookie
    assert len(bob_cookies) == 0

    print("TEST PASSED: Browser contexts are isolated!")

    # Cleanup
    alice_page.close()
    bob_page.close()

    alice_context.close()
    bob_context.close()
