errors = {
    "account": {
        "email-exist": "Account with this email already exists",
        "username-exist": "Account with this username already exists",
        "activated": "Account already activated",
        "not-activated": "Account not activated yet",
        "not-found": "Account not found",
        "login-failed": "Login failed",
        "reset-cooldown": "Password reset cooldown"
    },
    "general": {
        "token-invalid": "Invalid token",
        "token-invalid-type": "Invalid token type",
        "pagination-error": "Pagination is out of range",
        "empty-required": "Required field can't be empty",
        "something-bad": "Something very bad happened",
        "missing-field": "Required field is missing",
        "bad-regex": "Parameter don't match regex",
        "method-not-allowed": "Method not allowed",
        "too-many-requests": "Too many requests",
        "invalid-email": "Invalid email",
        "empty-string": "Empty string",
        "bad-request": "Bad request",
        "not-found": "Not found"
    }
}

def abort(scope, message):
    try:
        error_message = errors[scope][message]
    except Exception:
        error_message = "Unknown error"

    return {
        "error": error_message,
        "data": {}
    }
