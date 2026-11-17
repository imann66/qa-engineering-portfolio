import pytest

from app.api import app


@pytest.fixture
def client():
    return app.test_client()


# ==========================================
# POSITIVE AUTHORIZATION TESTS
# ==========================================

@pytest.mark.parametrize(
    "token, account_id, expected_owner",
    [
        ("alice-token", 101, "alice"),
        ("bob-token", 202, "bob"),
    ]
)
def test_user_can_access_own_account(
    client,
    token,
    account_id,
    expected_owner
):

    response = client.get(
        f"/api/accounts/{account_id}",
        headers={
            "Authorization": token
        }
    )

    assert response.status_code == 200
    assert response.json["owner"] == expected_owner


# ==========================================
# NEGATIVE AUTHORIZATION TESTS
# ==========================================

@pytest.mark.parametrize(
    "token, account_id",
    [
        ("alice-token", 202),
        ("bob-token", 101),
    ]
)
def test_user_cannot_access_other_users_account(
    client,
    token,
    account_id
):

    response = client.get(
        f"/api/accounts/{account_id}",
        headers={
            "Authorization": token
        }
    )

    assert response.status_code == 403
    assert response.json["error"] == "Forbidden"

    # Verify sensitive information is not exposed
    assert "balance" not in response.json
    assert "owner" not in response.json
    assert "account_id" not in response.json


# ==========================================
# AUTHENTICATION TESTS
# ==========================================

@pytest.mark.parametrize(
    "headers",
    [
        {},
        {"Authorization": ""},
        {"Authorization": "invalid-token"},
        {"Authorization": "unknown-user-token"},
    ]
)
def test_invalid_authentication_is_rejected(
    client,
    headers
):

    response = client.get(
        "/api/accounts/101",
        headers=headers
    )

    assert response.status_code == 401
    assert response.json["error"] == "Unauthorized"


# ==========================================
# RESOURCE EXISTENCE TESTS
# ==========================================

def test_nonexistent_account_returns_404(client):

    response = client.get(
        "/api/accounts/999",
        headers={
            "Authorization": "alice-token"
        }
    )

    assert response.status_code == 404
    assert response.json["error"] == "Account not found"


# ==========================================
# INVALID INPUT TESTS
# ==========================================

@pytest.mark.parametrize(
    "account_id",
    [
        "abc",
        "invalid",
        "12abc",
    ]
)
def test_invalid_account_id_format_returns_404(
    client,
    account_id
):

    response = client.get(
        f"/api/accounts/{account_id}",
        headers={
            "Authorization": "alice-token"
        }
    )

    assert response.status_code == 404


# ==========================================
# Case-sensitive and Whitespace token
# ==========================================

@pytest.mark.parametrize(
    "token",
    [
        "Alice-token",
        " alice-token ",
    ]
)
def test_case_sensitive_and_whitespace_token(client, token):

    response = client.get(
        "/api/accounts/101",
        headers={
            "Authorization": token
        }
    )

    assert response.status_code == 401
    assert response.json["error"] == "Unauthorized"


# ==========================================
# Negative and Zero account ID
# ==========================================

@pytest.mark.parametrize(
    "account_id",
    [
        "-101",
        "0",
    ]
)
def test_negative_and_zero_account_id(
    client,
    account_id
):

    response = client.get(
        f"/api/accounts/{account_id}",
        headers={
            "Authorization": "alice-token"
        }
    )

    assert response.status_code == 404