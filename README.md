# Global Temperatures

In this exercise, your goal is to demonstrate to us that you have a solid understanding of python when used as a backend service, that uses a database and exposes a REST interface. We expect Python code for this task and a docker containerized solution. First, download this [climate change kaggle dataset](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data). You will only use this file:

- [GlobalLandTemperaturesByCity.csv](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalLandTemperaturesByCity.csv) 

The dataset contains the observations of monthly average temperature of cities and of countries.

## To Run (Via Docker)

### Run for Development Area:

To run the development server, run this task:

```bash
docker-compose -f ./docker-compose.yml up --build
```

### To deploy and run in production area:

To run the production server, run this task:

```bash
docker-compose -f ./docker-compose-deploy.yml up --build
```

## Import CSV file

To import GlobalLandTemperaturesByCity.csv file into database. Copy GlobalLandTemperaturesByCity.csv file into app directory and execute this command:

```bash
docker-compose -f ./docker-compose.yml run --rm app sh -c "python manage.py importcsv GlobalLandTemperaturesByCity.csv"
```

## Testing the server

Once the Development area started, you can navigate to http://127.0.0.1:8000/ to view the Task overview.

Once the Production area started, you can navigate to http://127.0.0.1/ to view the Task overview.

## REST API

The REST API for this app is described below.

### Get list of GlobalLandTemperaturesByCity

#### Request

    `GET /api/`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/

    Optional query string parameters
        - count = int
        - date_from = string like 2021-12-01
        - date_to = string like 2021-12-01

    curl -i -H 'Accept: application/json' http://localhost:8000/api/?count=10&date_from=2020-01-01&date_to=2020-12-01

#### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [...]

## Examples

#### A. Find the entry whose city has the highest AverageTemperature since the year 2000.

Request:

    GET /api/?count=1&date_from=2000-01-01

Response:

    HTTP 200 OK
    Allow: POST, GET, OPTIONS
    Content-Type: application/json
    Vary: Accept

    [
        {
            "id": 117013,
            "dt": "2013-07-01",
            "AverageTemperature": 39.15600000000001,
            "AverageTemperatureUncertainty": 0.37,
            "City": "Ahvaz",
            "Country": "Iran",
            "Latitude": "31.35N",
            "Longitude": "49.01E"
        }
    ]

#### B. Following above: assume the temperature observation of the city last month breaks the record. It is 0.1 degree higher with the same uncertainty. Create this entry.

Request:

    POST /api/

    payload

        {
            "dt": "2021-09-01",
            "AverageTemperature": 39.25600000000001,
            "AverageTemperatureUncertainty": 0.47,
            "City": "Ahvaz",
            "Country": "Iran",
            "Latitude": "31.35N",
            "Longitude": "49.01E"
        }

Response:

    HTTP 200 OK
    Allow: POST, GET, OPTIONS
    Content-Type: application/json
    Vary: Accept

    [
        {
            "id": 465453,
            "dt": "2021-09-01",
            "AverageTemperature": 39.25600000000001,
            "AverageTemperatureUncertainty": 0.47,
            "City": "Ahvaz",
            "Country": "Iran",
            "Latitude": "31.35N",
            "Longitude": "49.01E"
        }

]

#### C. Following question 1: assume the returned entry has been found erroneous. The actual average temperature of this entry is 2.5 degrees lower. Update this entry.

Request:

    PATCH /api/Ahvaz/2021-09-01/

    payload:

        {
            "AverageTemperature": 41.65600000000001,
            "AverageTemperatureUncertainty": 2.87
        }

Response :

    HTTP 204 No Content
    Allow: OPTIONS, GET, PATCH
    Content-Type: application/json
    Vary: Accept

    {
        "id": 465453,
        "dt": "2021-09-01",
        "AverageTemperature": 41.65600000000001,
        "AverageTemperatureUncertainty": 2.87,
        "City": "Ahvaz",
        "Country": "Iran",
        "Latitude": "31.35N",
        "Longitude": "49.01E"
    }
