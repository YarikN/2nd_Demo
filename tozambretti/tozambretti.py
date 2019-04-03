from google.cloud import pubsub_v1
import requests
import base64
import json


def message_from_topic2(request, message, data=None):
    project_id = "glass-memento-235118"
    subscription_name = "topic2"
    # my project ID

    subscriber = pubsub_v1.SubscriberClient()

    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    def callback(message):
        print('Received message: {}'.format(message))
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

    c = request
    b = base64.b64decode(c['data'])
    d = b.decode('utf-8')
    a = json.loads(d)
    print(a, type(a))

    requests.post("https://us-central1-glass-memento-235118.cloudfunctions.net/function-1", json=a)

