import json
from datetime import datetime
from faker import Faker
import time
import boto3

client = boto3.client('sns')
faker_instance = Faker()

def get_data():
    lat, lng, region, country, timezone = faker_instance.location_on_land()
    created_datetime = datetime.utcnow()
    return dict(
        created_at=f"{datetime.utcnow()}",
        updated_at=f"{datetime.utcnow()}",
        customer_id=faker_instance.uuid4(),
        name=faker_instance.name(),
        region=region,
        country=country,
        lat=lat,
        lng=lng,
        email=faker_instance.ascii_free_email(),
        phone=faker_instance.phone_number()
    )

while True:
    data = get_data()
    client.publish(
        TopicArn='arn:aws:sns:us-east-1:************:consumidor-criado',
        Message= json.dumps(data)
    )
    print(data)
    time.sleep(1)