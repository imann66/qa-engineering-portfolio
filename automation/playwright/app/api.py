from flask import Flask, jsonify, request


app = Flask(__name__)


ACCOUNTS = {
    101: {
        "owner": "alice",
        "balance": 5000
    },
    202: {
        "owner": "bob",
        "balance": 3000
    }
}


TOKENS = {
    "alice-token": "alice",
    "bob-token": "bob"
}


@app.route("/api/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):

    token = request.headers.get("Authorization")

    # Authentication
    if not token or token not in TOKENS:
        return jsonify({
            "error": "Unauthorized"
        }), 401

    username = TOKENS[token]

    # Resource existence
    account = ACCOUNTS.get(account_id)

    if account is None:
        return jsonify({
            "error": "Account not found"
        }), 404

    # Authorization
    if account["owner"] != username:
        return jsonify({
            "error": "Forbidden"
        }), 403

    return jsonify({
        "account_id": account_id,
        "owner": account["owner"],
        "balance": account["balance"]
    }), 200