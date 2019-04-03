from google.cloud import pubsub_v1
import json
import requests


def get_data_from_api2(request):
    project_id = "glass-memento-235118"
    topic_name2 = "topic2"

    publisher = pubsub_v1.PublisherClient()

    topic_path2 = publisher.topic_path(project_id, topic_name2)

    list_of_city = [703447, 698740, 702550, 706483, 709930, 707471, 710719, 689558, 703845, 690548]
    apikey = '688bc3704f60250be00b93ccbdbf7c9b'

    for i in list_of_city:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?id={0}&APPID={1}'.format(i, apikey))
        data = json.loads(r.content)
        data_topic2 = json.dumps({"pressure": data['main']['pressure'], "name": data['name'], "dt": data['dt'],
                                  "wind": data['wind']}).encode('utf-8')
        future2 = publisher.publish(topic_path2, data=data_topic2)

        print(future2.result(), data_topic2)