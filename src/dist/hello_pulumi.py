import requests
import pendulum

def lambda_handler(event, context):
    response = requests.get("https://pulumi.com")
    print(response.text)

    now = pendulum.now("Europe/Paris")

    # Changing timezone
    now.in_timezone("America/Toronto")

    # Default support for common datetime formats
    now.to_iso8601_string()

    # Shifting
    now.add(days=2)

    return response.text