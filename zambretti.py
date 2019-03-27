from datetime import datetime

def result(msg) :
    forecast_text = {
        'A' : "Settled fine",
        'B' : "Fine weather",
        'C' : "Becoming fine",
        'D' : "Fine, becoming less settled",
        'E' : "Fine, possible showers",
        'F' : "Fairly fine, improving",
        'G' : "Fairly fine, possible showers early",
        'H' : "Fairly fine, showery later",
        'I' : "Showery early, improving",
        'J' : "Changeable, mending",
        'K' : "Fairly fine, showers likely",
        'L' : "Rather unsettled clearing later",
        'M' : "Unsettled, probably improving",
        'N' : "Showery, bright intervals",
        'O' : "Showery, becoming less settled",
        'P' : "Changeable, some rain",
        'Q' : "Unsettled, short fine intervals",
        'R' : "Unsettled, rain later",
        'S' : "Unsettled, some rain",
        'T' : "Mostly very unsettled",
        'U' : "Occasional rain, worsening",
        'V' : "Rain at times, very unsettled",
        'W' : "Rain at frequent intervals",
        'X' : "Rain, very unsettled",
        'Y' : "Stormy, may improve",
        'Z' : "Stormy, much rain"
        }
    return forecast_text[msg]


def zamberetti (p):
    z = round(22 * (p - 950) / 100)
    return z


def change_press_wind(pressureGet, windGet):
    if 349.75 <= windGet < 360:
        return pressureGet + 6
    if 0 <= windGet < 12.25:
        return pressureGet + 6
    if 12.25 <= windGet < 34.75:
        return pressureGet + 5
    if 34.75 <= windGet < 57.25:
        return pressureGet + 5
    if 57.25 <= windGet < 79.75:
        return pressureGet + 2
    if 79.5 <= windGet < 102.25:
        return pressureGet - 0.5
    if 102.25 <= windGet < 124.75:
        return pressureGet - 2
    if 124.75 <= windGet < 147.25:
        return pressureGet - 5
    if 147.5 <= windGet < 169.75:
        return pressureGet - 8.5
    if 169.75 <= windGet < 192.25:
        return pressureGet - 12
    if 192.25 <= windGet < 214.75:
        return pressureGet - 10
    if 214.75 <= windGet < 237.25:
        return pressureGet - 6
    if 237.25 <= windGet < 259.75 :
        return pressureGet - 4.5
    if 259.75 <= windGet < 282.25:
        return pressureGet - 3
    if 282.25 <= windGet < 304.75:
        return pressureGet - 0.5
    if 304.75 <= windGet < 327.25:
        return pressureGet + 1.5
    if 327.25 <= windGet < 349.75:
        return pressureGet + 3


def trend_func(wetherDict):
    plast = wetherDict[0]['main']['pressure']
    preplast = wetherDict[1]['main']['pressure']
    prepreplast = wetherDict[2]['main']['pressure']

    if (plast - preplast >= 4) and (plast - prepreplast >= 4) and (preplast - prepreplast >= 4):
        return 'rise'
    elif (plast - preplast <= -4) and (plast - prepreplast <= -4)and (preplast - prepreplast <= -4):
        return 'fall'
    else:
        return 'stab'

def change_press_month(pressure, trend, month):
    if 3 < month < 9 and trend == 'rise':
        pressure += 7
    elif 3 < month < 9 and trend == 'fall':
        pressure -= 7
    return pressure


def fall_press(zam):
    fallP = ('Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'X', 'X', 'V',
             'U', 'R', 'O', 'H', 'D', 'B', 'B', 'B', 'A', 'A', 'A')
    return fallP[zam]

def rise_press(zam):
    riseP = ('Z', 'Z', 'Z', 'Y', 'Y', 'T', 'Q', 'M', 'L', 'J', 'I',
             'G', 'F', 'C', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A')
    return riseP[zam]

def stab_press(zam):
    stabP = ('Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'X', 'X', 'W', 'S', 'P',
             'N', 'K', 'E', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A')
    return stabP[zam]


def main():
    a = [{"coord":{"lon":139,"lat":35},
        "sys":{"country":"JP","sunrise":1369769524,"sunset":1369821049},
        "weather":[{"id":804,"main":"clouds","description":"overcast clouds","icon":"04n"}],
        "main":{"temp":289.5,"humidity":89,"pressure":1013,"temp_min":287.04,"temp_max":292.04},
        "wind":{"speed":7.31,"deg":187.002},
        "rain":{"3h":0},
        "clouds":{"all":92},
        "dt":1369824698,
        "id":1851632,
        "name":"Shuzenji",
        "cod":200},

    {"coord": {"lon": 139, "lat": 35},
         "sys": {"country": "JP", "sunrise": 1369769524, "sunset": 1369821049},
         "weather": [{"id": 804, "main": "clouds", "description": "overcast clouds", "icon": "04n"}],
         "main": {"temp": 289.5, "humidity": 89, "pressure": 1023, "temp_min": 287.04, "temp_max": 292.04},
         "wind": {"speed": 7.31, "deg": 187.002},
         "rain": {"3h": 0},
         "clouds": {"all": 92},
         "dt": 1369824698,
         "id": 1851632,
         "name": "Shuzenji",
         "cod": 200},

    {"coord": {"lon": 139, "lat": 35},
         "sys": {"country": "JP", "sunrise": 1369769524, "sunset": 1369821049},
         "weather": [{"id": 804, "main": "clouds", "description": "overcast clouds", "icon": "04n"}],
         "main": {"temp": 289.5, "humidity": 89, "pressure": 1023, "temp_min": 287.04, "temp_max": 292.04},
         "wind": {"speed": 7.31, "deg": 187.002},
         "rain": {"3h": 0},
         "clouds": {"all": 92},
         "dt": 1369824698,
         "id": 1851632,
         "name": "Shuzenji",
         "cod": 200}]





    pressure = a[0]['main']['pressure']
    wind = a[0]['wind']['deg']
    dt = datetime.fromtimestamp(a[0]['dt'])
    month = dt.month

    pressure = change_press_wind(pressure, wind)
    print(pressure)

    trend = trend_func(a)
    print(trend)

    pressure = change_press_month(pressure, trend, month)
    print(pressure)

    zamber = zamberetti(pressure)
    print("zamber = {0}".format(zamber))

    trendLetter = {'fall': fall_press, 'rise': rise_press, 'stab': stab_press}

    prognosis = result(trendLetter[trend](zamber))
    print(prognosis)


main()
