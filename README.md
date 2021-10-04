# Global Temperatures

# To Run (Via Docker)

## Run for Development Area:

To run the development server, run this task:

```bash
docker-compose -f ./docker-compose.yml up --build
```

## To deploy and run in production are:

To run the production server, run this task:

```bash
docker-compose -f ./docker-compose-deploy.yml up --build
```

## Import CSV file

To import GlobalLandTemperaturesByCity.csv file into database

```bash
docker-compose -f ./docker-compose.yml run --rm app sh -c "python manage.py importcsv GlobalLandTemperaturesByCity.csv"
```

# Examples

### A. Find the entry whose city has the highest AverageTemperature since the year 2000.

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

### B. Following above: assume the temperature observation of the city last month breaks the record. It is 0.1 degree higher with the same uncertainty. Create this entry.

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

### c. Following question 1: assume the returned entry has been found erroneous. The actual average temperature of this entry is 2.5 degrees lower. Update this entry.

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
