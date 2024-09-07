import json

OK_RESPONSE = {
    "statusCode": 200,
    "headers": {"Content-Type": "application/json"},
    "body": json.dumps({"status": "ok"}),
}
ERROR_RESPONSE = {
    "statusCode": 400,
    "body": json.dumps({"status": "Oops, something went wrong!"}),
}
