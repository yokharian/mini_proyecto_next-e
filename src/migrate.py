from src.config import table
from src.models import OpenWeatherInsight

to_migrate = [
    {
        "dt": 62862200,
        "clouds": 73,
        "dew_point": 21.06,
        "dt_end": 1628625600,
        "feels_like": 33.99,
        "humidity": 55,
        "pop": 0.0,
        "pressure": 1012,
        "temp": 31.17,
        "uvi": 11.58,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04d",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 108,
        "wind_gust": 4.44,
        "wind_speed": 3.19,
    },
    {
        "dt": 62862560,
        "clouds": 62,
        "dew_point": 13.88,
        "dt_end": 1628629200,
        "feels_like": 33.13,
        "humidity": 30,
        "pop": 0.0,
        "pressure": 1013,
        "temp": 33.88,
        "uvi": 10.21,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04d",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 112,
        "wind_gust": 5.4,
        "wind_speed": 3.78,
    },
    {
        "dt": 62862920,
        "clouds": 59,
        "dew_point": 12.7,
        "dt_end": 1628632800,
        "feels_like": 32.62,
        "humidity": 28,
        "pop": 0.04,
        "pressure": 1013,
        "temp": 33.73,
        "uvi": 7.58,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04d",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 114,
        "wind_gust": 6.61,
        "wind_speed": 5.42,
    },
    {
        "dt": 62863280,
        "clouds": 57,
        "dew_point": 12.48,
        "dt_end": 1628636400,
        "feels_like": 32.96,
        "humidity": 27,
        "pop": 0.08,
        "pressure": 1013,
        "temp": 34.13,
        "uvi": 4.55,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04d",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 115,
        "wind_gust": 8.05,
        "wind_speed": 6.96,
    },
    {
        "dt": 62863640,
        "clouds": 52,
        "dew_point": 12.03,
        "dt_end": 1628640000,
        "feels_like": 32.99,
        "humidity": 26,
        "pop": 0.08,
        "pressure": 1013,
        "temp": 34.27,
        "uvi": 2.04,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04d",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 118,
        "wind_gust": 9.26,
        "wind_speed": 7.85,
    },
    {
        "dt": 62864000,
        "clouds": 46,
        "dew_point": 12.18,
        "dt_end": 1628643600,
        "feels_like": 32.52,
        "humidity": 27,
        "pop": 0.08,
        "pressure": 1012,
        "temp": 33.77,
        "uvi": 0.57,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03d",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 123,
        "wind_gust": 10.55,
        "wind_speed": 7.47,
    },
    {
        "dt": 62864360,
        "clouds": 33,
        "dew_point": 13.18,
        "dt_end": 1628647200,
        "feels_like": 30.96,
        "humidity": 32,
        "pop": 0.06,
        "pressure": 1013,
        "temp": 31.92,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03d",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 119,
        "wind_gust": 11.72,
        "wind_speed": 7.04,
    },
    {
        "dt": 62864720,
        "clouds": 21,
        "dew_point": 13.56,
        "dt_end": 1628650800,
        "feels_like": 28.72,
        "humidity": 44,
        "pop": 0.06,
        "pressure": 1014,
        "temp": 28.75,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "algo de nubes",
            "icon": "02n",
            "id": 801,
            "main": "Clouds",
        },
        "wind_deg": 112,
        "wind_gust": 10.97,
        "wind_speed": 6.59,
    },
    {
        "dt": 62865080,
        "clouds": 23,
        "dew_point": 15.43,
        "dt_end": 1628654400,
        "feels_like": 27.87,
        "humidity": 54,
        "pop": 0.01,
        "pressure": 1015,
        "temp": 27.19,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "algo de nubes",
            "icon": "02n",
            "id": 801,
            "main": "Clouds",
        },
        "wind_deg": 114,
        "wind_gust": 9.84,
        "wind_speed": 5.38,
    },
    {
        "dt": 62865440,
        "clouds": 29,
        "dew_point": 16.2,
        "dt_end": 1628658000,
        "feels_like": 26.44,
        "humidity": 59,
        "pop": 0.01,
        "pressure": 1016,
        "temp": 26.44,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03n",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 121,
        "wind_gust": 6.99,
        "wind_speed": 3.91,
    },
    {
        "dt": 62865800,
        "clouds": 28,
        "dew_point": 16.14,
        "dt_end": 1628661600,
        "feels_like": 26.16,
        "humidity": 60,
        "pop": 0.01,
        "pressure": 1016,
        "temp": 25.94,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03n",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 124,
        "wind_gust": 5.69,
        "wind_speed": 3.13,
    },
    {
        "dt": 62866160,
        "clouds": 26,
        "dew_point": 15.57,
        "dt_end": 1628665200,
        "feels_like": 25.69,
        "humidity": 60,
        "pop": 0.01,
        "pressure": 1016,
        "temp": 25.52,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03n",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 124,
        "wind_gust": 5.02,
        "wind_speed": 2.66,
    },
    {
        "dt": 62866520,
        "clouds": 10,
        "dew_point": 15.44,
        "dt_end": 1628668800,
        "feels_like": 25.07,
        "humidity": 61,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 24.93,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 122,
        "wind_gust": 4.15,
        "wind_speed": 2.14,
    },
    {
        "dt": 62866880,
        "clouds": 14,
        "dew_point": 15.31,
        "dt_end": 1628672400,
        "feels_like": 24.58,
        "humidity": 63,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 24.44,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "algo de nubes",
            "icon": "02n",
            "id": 801,
            "main": "Clouds",
        },
        "wind_deg": 130,
        "wind_gust": 3.13,
        "wind_speed": 1.54,
    },
    {
        "dt": 62867240,
        "clouds": 21,
        "dew_point": 15.21,
        "dt_end": 1628676000,
        "feels_like": 24.09,
        "humidity": 65,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 23.94,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "algo de nubes",
            "icon": "02n",
            "id": 801,
            "main": "Clouds",
        },
        "wind_deg": 119,
        "wind_gust": 2.57,
        "wind_speed": 1.01,
    },
    {
        "dt": 62867600,
        "clouds": 34,
        "dew_point": 15.38,
        "dt_end": 1628679600,
        "feels_like": 23.66,
        "humidity": 68,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 23.48,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03n",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 126,
        "wind_gust": 2.4,
        "wind_speed": 0.88,
    },
    {
        "dt": 62867960,
        "clouds": 43,
        "dew_point": 15.58,
        "dt_end": 1628683200,
        "feels_like": 23.25,
        "humidity": 70,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 23.06,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03n",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 129,
        "wind_gust": 2.16,
        "wind_speed": 0.72,
    },
    {
        "dt": 62868320,
        "clouds": 36,
        "dew_point": 20.41,
        "dt_end": 1628686800,
        "feels_like": 23.65,
        "humidity": 85,
        "pop": 0.0,
        "pressure": 1017,
        "temp": 23.07,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03n",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 138,
        "wind_gust": 1.77,
        "wind_speed": 0.51,
    },
    {
        "dt": 62868680,
        "clouds": 31,
        "dew_point": 21.06,
        "dt_end": 1628690400,
        "feels_like": 23.83,
        "humidity": 88,
        "pop": 0.0,
        "pressure": 1017,
        "temp": 23.16,
        "uvi": 0.27,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03d",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 125,
        "wind_gust": 1.64,
        "wind_speed": 0.45,
    },
    {
        "dt": 62869040,
        "clouds": 34,
        "dew_point": 20.65,
        "dt_end": 1628694000,
        "feels_like": 24.11,
        "humidity": 84,
        "pop": 0.0,
        "pressure": 1017,
        "temp": 23.51,
        "uvi": 1.3,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03d",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 78,
        "wind_gust": 1.26,
        "wind_speed": 0.85,
    },
    {
        "dt": 62869400,
        "clouds": 43,
        "dew_point": 20.21,
        "dt_end": 1628697600,
        "feels_like": 25.03,
        "humidity": 77,
        "pop": 0.0,
        "pressure": 1017,
        "temp": 24.51,
        "uvi": 3.38,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03d",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 66,
        "wind_gust": 1.15,
        "wind_speed": 1.37,
    },
    {
        "dt": 62869760,
        "clouds": 42,
        "dew_point": 19.67,
        "dt_end": 1628701200,
        "feels_like": 26.28,
        "humidity": 67,
        "pop": 0.0,
        "pressure": 1018,
        "temp": 26.28,
        "uvi": 6.12,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03d",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 63,
        "wind_gust": 1.45,
        "wind_speed": 1.78,
    },
    {
        "dt": 62870120,
        "clouds": 40,
        "dew_point": 19.04,
        "dt_end": 1628704800,
        "feels_like": 29.97,
        "humidity": 56,
        "pop": 0.0,
        "pressure": 1017,
        "temp": 28.68,
        "uvi": 8.93,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03d",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 78,
        "wind_gust": 2.3,
        "wind_speed": 2.15,
    },
    {
        "dt": 62870480,
        "clouds": 35,
        "dew_point": 15.7,
        "dt_end": 1628708400,
        "feels_like": 31.95,
        "humidity": 42,
        "pop": 0.0,
        "pressure": 1016,
        "temp": 31.53,
        "uvi": 10.83,
        "visibility": 10000,
        "weather": {
            "description": "nubes dispersas",
            "icon": "03d",
            "id": 802,
            "main": "Clouds",
        },
        "wind_deg": 96,
        "wind_gust": 3.18,
        "wind_speed": 2.54,
    },
    {
        "dt": 62870840,
        "clouds": 0,
        "dew_point": 14.77,
        "dt_end": 1628712000,
        "feels_like": 33.06,
        "humidity": 37,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 32.92,
        "uvi": 11.36,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 106,
        "wind_gust": 4.44,
        "wind_speed": 3.13,
    },
    {
        "dt": 62871200,
        "clouds": 0,
        "dew_point": 13.9,
        "dt_end": 1628715600,
        "feels_like": 33.76,
        "humidity": 33,
        "pop": 0.0,
        "pressure": 1014,
        "temp": 33.94,
        "uvi": 10.02,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 113,
        "wind_gust": 5.59,
        "wind_speed": 3.82,
    },
    {
        "dt": 62871560,
        "clouds": 1,
        "dew_point": 13.03,
        "dt_end": 1628719200,
        "feels_like": 34.4,
        "humidity": 29,
        "pop": 0.0,
        "pressure": 1013,
        "temp": 34.95,
        "uvi": 7.43,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 111,
        "wind_gust": 6.16,
        "wind_speed": 5.12,
    },
    {
        "dt": 62871920,
        "clouds": 3,
        "dew_point": 12.34,
        "dt_end": 1628722800,
        "feels_like": 34.55,
        "humidity": 28,
        "pop": 0.0,
        "pressure": 1012,
        "temp": 35.2,
        "uvi": 4.46,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 106,
        "wind_gust": 6.97,
        "wind_speed": 6.18,
    },
    {
        "dt": 62872280,
        "clouds": 4,
        "dew_point": 12.02,
        "dt_end": 1628726400,
        "feels_like": 34.04,
        "humidity": 28,
        "pop": 0.0,
        "pressure": 1012,
        "temp": 34.83,
        "uvi": 1.99,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 105,
        "wind_gust": 7.45,
        "wind_speed": 6.14,
    },
    {
        "dt": 62872640,
        "clouds": 4,
        "dew_point": 12.46,
        "dt_end": 1628730000,
        "feels_like": 33.25,
        "humidity": 30,
        "pop": 0.0,
        "pressure": 1012,
        "temp": 33.97,
        "uvi": 0.55,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 107,
        "wind_gust": 8.46,
        "wind_speed": 6.22,
    },
    {
        "dt": 62873000,
        "clouds": 4,
        "dew_point": 14.07,
        "dt_end": 1628733600,
        "feels_like": 31.65,
        "humidity": 39,
        "pop": 0.02,
        "pressure": 1013,
        "temp": 31.67,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 103,
        "wind_gust": 9.84,
        "wind_speed": 6.75,
    },
    {
        "dt": 62873360,
        "clouds": 4,
        "dew_point": 15.86,
        "dt_end": 1628737200,
        "feels_like": 30.17,
        "humidity": 49,
        "pop": 0.02,
        "pressure": 1014,
        "temp": 29.48,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 116,
        "wind_gust": 10.47,
        "wind_speed": 6.84,
    },
    {
        "dt": 62873720,
        "clouds": 5,
        "dew_point": 17.24,
        "dt_end": 1628740800,
        "feels_like": 28.8,
        "humidity": 59,
        "pop": 0.02,
        "pressure": 1016,
        "temp": 27.61,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 121,
        "wind_gust": 10.5,
        "wind_speed": 6.07,
    },
    {
        "dt": 62874080,
        "clouds": 4,
        "dew_point": 17.73,
        "dt_end": 1628744400,
        "feels_like": 26.48,
        "humidity": 66,
        "pop": 0.02,
        "pressure": 1016,
        "temp": 26.48,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 123,
        "wind_gust": 8.11,
        "wind_speed": 4.76,
    },
    {
        "dt": 62874440,
        "clouds": 3,
        "dew_point": 17.63,
        "dt_end": 1628748000,
        "feels_like": 26.25,
        "humidity": 67,
        "pop": 0.0,
        "pressure": 1016,
        "temp": 25.86,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 122,
        "wind_gust": 6.28,
        "wind_speed": 3.68,
    },
    {
        "dt": 62874800,
        "clouds": 8,
        "dew_point": 17.34,
        "dt_end": 1628751600,
        "feels_like": 25.88,
        "humidity": 67,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 25.52,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 114,
        "wind_gust": 4.82,
        "wind_speed": 2.67,
    },
    {
        "dt": 62875160,
        "clouds": 52,
        "dew_point": 17.35,
        "dt_end": 1628755200,
        "feels_like": 25.47,
        "humidity": 69,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 25.1,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04n",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 117,
        "wind_gust": 4.14,
        "wind_speed": 2.26,
    },
    {
        "dt": 62875520,
        "clouds": 57,
        "dew_point": 17.32,
        "dt_end": 1628758800,
        "feels_like": 25.04,
        "humidity": 70,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 24.69,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04n",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 117,
        "wind_gust": 3.25,
        "wind_speed": 1.75,
    },
    {
        "dt": 62875880,
        "clouds": 68,
        "dew_point": 17.28,
        "dt_end": 1628762400,
        "feels_like": 24.54,
        "humidity": 72,
        "pop": 0.0,
        "pressure": 1014,
        "temp": 24.19,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04n",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 113,
        "wind_gust": 2.91,
        "wind_speed": 1.49,
    },
    {
        "dt": 62876240,
        "clouds": 76,
        "dew_point": 17.21,
        "dt_end": 1628766000,
        "feels_like": 24.22,
        "humidity": 73,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 23.87,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04n",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 112,
        "wind_gust": 2.51,
        "wind_speed": 1.09,
    },
    {
        "dt": 62876600,
        "clouds": 81,
        "dew_point": 17.3,
        "dt_end": 1628769600,
        "feels_like": 23.91,
        "humidity": 75,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 23.54,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04n",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 113,
        "wind_gust": 2.15,
        "wind_speed": 0.7,
    },
    {
        "dt": 62876960,
        "clouds": 84,
        "dew_point": 17.44,
        "dt_end": 1628773200,
        "feels_like": 23.59,
        "humidity": 78,
        "pop": 0.0,
        "pressure": 1016,
        "temp": 23.18,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04n",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 39,
        "wind_gust": 1.45,
        "wind_speed": 0.16,
    },
    {
        "dt": 62877320,
        "clouds": 100,
        "dew_point": 17.58,
        "dt_end": 1628776800,
        "feels_like": 24.08,
        "humidity": 76,
        "pop": 0.0,
        "pressure": 1017,
        "temp": 23.67,
        "uvi": 0.26,
        "visibility": 10000,
        "weather": {"description": "nubes", "icon": "04d", "id": 804, "main": "Clouds"},
        "wind_deg": 116,
        "wind_gust": 1.76,
        "wind_speed": 0.56,
    },
    {
        "dt": 62877680,
        "clouds": 88,
        "dew_point": 17.78,
        "dt_end": 1628780400,
        "feels_like": 25.48,
        "humidity": 71,
        "pop": 0.0,
        "pressure": 1017,
        "temp": 25.06,
        "uvi": 1.28,
        "visibility": 10000,
        "weather": {"description": "nubes", "icon": "04d", "id": 804, "main": "Clouds"},
        "wind_deg": 88,
        "wind_gust": 1.55,
        "wind_speed": 1.12,
    },
    {
        "dt": 62878040,
        "clouds": 87,
        "dew_point": 17.92,
        "dt_end": 1628784000,
        "feels_like": 26.62,
        "humidity": 65,
        "pop": 0.0,
        "pressure": 1017,
        "temp": 26.62,
        "uvi": 3.35,
        "visibility": 10000,
        "weather": {"description": "nubes", "icon": "04d", "id": 804, "main": "Clouds"},
        "wind_deg": 72,
        "wind_gust": 1.39,
        "wind_speed": 1.38,
    },
    {
        "dt": 62878400,
        "clouds": 79,
        "dew_point": 17.73,
        "dt_end": 1628787600,
        "feels_like": 29.77,
        "humidity": 57,
        "pop": 0.0,
        "pressure": 1017,
        "temp": 28.46,
        "uvi": 6.3,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04d",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 82,
        "wind_gust": 2.11,
        "wind_speed": 2.02,
    },
    {
        "dt": 62878760,
        "clouds": 64,
        "dew_point": 17.24,
        "dt_end": 1628791200,
        "feels_like": 31.49,
        "humidity": 50,
        "pop": 0.0,
        "pressure": 1016,
        "temp": 30.29,
        "uvi": 9.2,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04d",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 85,
        "wind_gust": 3.14,
        "wind_speed": 2.71,
    },
    {
        "dt": 62879120,
        "clouds": 53,
        "dew_point": 16.57,
        "dt_end": 1628794800,
        "feels_like": 32.71,
        "humidity": 44,
        "pop": 0.0,
        "pressure": 1016,
        "temp": 31.79,
        "uvi": 11.17,
        "visibility": 10000,
        "weather": {
            "description": "muy nuboso",
            "icon": "04d",
            "id": 803,
            "main": "Clouds",
        },
        "wind_deg": 91,
        "wind_gust": 3.91,
        "wind_speed": 3.17,
    },
    {
        "dt": 62879480,
        "clouds": 3,
        "dew_point": 15.78,
        "dt_end": 1628798400,
        "feels_like": 33.56,
        "humidity": 39,
        "pop": 0.0,
        "pressure": 1015,
        "temp": 32.99,
        "uvi": 11.31,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 97,
        "wind_gust": 4.6,
        "wind_speed": 3.67,
    },
    {
        "dt": 62879840,
        "clouds": 5,
        "dew_point": 15.04,
        "dt_end": 1628802000,
        "feels_like": 34.23,
        "humidity": 36,
        "pop": 0.0,
        "pressure": 1014,
        "temp": 33.84,
        "uvi": 9.97,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 105,
        "wind_gust": 5.48,
        "wind_speed": 4.34,
    },
    {
        "dt": 62880200,
        "clouds": 5,
        "dew_point": 13.67,
        "dt_end": 1628805600,
        "feels_like": 34.34,
        "humidity": 32,
        "pop": 0.32,
        "pressure": 1014,
        "temp": 34.48,
        "uvi": 7.39,
        "visibility": 10000,
        "weather": {
            "description": "lluvia ligera",
            "icon": "10d",
            "id": 500,
            "main": "Rain",
        },
        "wind_deg": 105,
        "wind_gust": 6.53,
        "wind_speed": 5.6,
    },
    {
        "dt": 62880560,
        "clouds": 5,
        "dew_point": 12.28,
        "dt_end": 1628809200,
        "feels_like": 33.9,
        "humidity": 29,
        "pop": 0.16,
        "pressure": 1013,
        "temp": 34.59,
        "uvi": 4.53,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 101,
        "wind_gust": 7.34,
        "wind_speed": 6.41,
    },
    {
        "dt": 62880920,
        "clouds": 6,
        "dew_point": 11.42,
        "dt_end": 1628812800,
        "feels_like": 33.26,
        "humidity": 28,
        "pop": 0.16,
        "pressure": 1013,
        "temp": 34.24,
        "uvi": 2.02,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 103,
        "wind_gust": 7.65,
        "wind_speed": 6.0,
    },
    {
        "dt": 62881280,
        "clouds": 6,
        "dew_point": 11.77,
        "dt_end": 1628816400,
        "feels_like": 32.69,
        "humidity": 30,
        "pop": 0.12,
        "pressure": 1013,
        "temp": 33.55,
        "uvi": 0.55,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 103,
        "wind_gust": 8.29,
        "wind_speed": 5.76,
    },
    {
        "dt": 62881640,
        "clouds": 8,
        "dew_point": 13.55,
        "dt_end": 1628820000,
        "feels_like": 31.37,
        "humidity": 38,
        "pop": 0.03,
        "pressure": 1013,
        "temp": 31.58,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01d",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 102,
        "wind_gust": 8.97,
        "wind_speed": 5.74,
    },
    {
        "dt": 62882000,
        "clouds": 10,
        "dew_point": 14.84,
        "dt_end": 1628823600,
        "feels_like": 30.3,
        "humidity": 45,
        "pop": 0.03,
        "pressure": 1015,
        "temp": 29.99,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 114,
        "wind_gust": 10.13,
        "wind_speed": 6.27,
    },
    {
        "dt": 62882360,
        "clouds": 14,
        "dew_point": 17.1,
        "dt_end": 1628827200,
        "feels_like": 29.22,
        "humidity": 57,
        "pop": 0.03,
        "pressure": 1016,
        "temp": 28.07,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "algo de nubes",
            "icon": "02n",
            "id": 801,
            "main": "Clouds",
        },
        "wind_deg": 122,
        "wind_gust": 11.4,
        "wind_speed": 6.81,
    },
    {
        "dt": 62882720,
        "clouds": 12,
        "dew_point": 18.25,
        "dt_end": 1628830800,
        "feels_like": 26.61,
        "humidity": 67,
        "pop": 0.08,
        "pressure": 1017,
        "temp": 26.61,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "algo de nubes",
            "icon": "02n",
            "id": 801,
            "main": "Clouds",
        },
        "wind_deg": 131,
        "wind_gust": 9.15,
        "wind_speed": 5.07,
    },
    {
        "dt": 62883080,
        "clouds": 11,
        "dew_point": 18.5,
        "dt_end": 1628834400,
        "feels_like": 26.44,
        "humidity": 71,
        "pop": 0.08,
        "pressure": 1017,
        "temp": 25.94,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "algo de nubes",
            "icon": "02n",
            "id": 801,
            "main": "Clouds",
        },
        "wind_deg": 126,
        "wind_gust": 6.23,
        "wind_speed": 3.78,
    },
    {
        "dt": 62883440,
        "clouds": 9,
        "dew_point": 18.38,
        "dt_end": 1628838000,
        "feels_like": 25.92,
        "humidity": 72,
        "pop": 0.08,
        "pressure": 1017,
        "temp": 25.44,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 113,
        "wind_gust": 4.58,
        "wind_speed": 2.55,
    },
    {
        "dt": 62883800,
        "clouds": 0,
        "dew_point": 18.07,
        "dt_end": 1628841600,
        "feels_like": 25.49,
        "humidity": 72,
        "pop": 0.0,
        "pressure": 1016,
        "temp": 25.05,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 108,
        "wind_gust": 3.63,
        "wind_speed": 1.86,
    },
    {
        "dt": 62884160,
        "clouds": 0,
        "dew_point": 17.99,
        "dt_end": 1628845200,
        "feels_like": 25.07,
        "humidity": 74,
        "pop": 0.0,
        "pressure": 1016,
        "temp": 24.62,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 104,
        "wind_gust": 3.17,
        "wind_speed": 1.43,
    },
    {
        "dt": 62884520,
        "clouds": 0,
        "dew_point": 17.97,
        "dt_end": 1628848800,
        "feels_like": 24.64,
        "humidity": 76,
        "pop": 0.0,
        "pressure": 1016,
        "temp": 24.18,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 99,
        "wind_gust": 2.8,
        "wind_speed": 1.21,
    },
    {
        "dt": 62884880,
        "clouds": 0,
        "dew_point": 18.02,
        "dt_end": 1628852400,
        "feels_like": 24.21,
        "humidity": 78,
        "pop": 0.0,
        "pressure": 1016,
        "temp": 23.74,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 102,
        "wind_gust": 2.56,
        "wind_speed": 1.04,
    },
    {
        "dt": 62885240,
        "clouds": 4,
        "dew_point": 17.97,
        "dt_end": 1628856000,
        "feels_like": 23.85,
        "humidity": 79,
        "pop": 0.0,
        "pressure": 1016,
        "temp": 23.39,
        "uvi": 0.0,
        "visibility": 10000,
        "weather": {
            "description": "cielo claro",
            "icon": "01n",
            "id": 800,
            "main": "Clear",
        },
        "wind_deg": 104,
        "wind_gust": 2.05,
        "wind_speed": 0.72,
    },
]


for insight in to_migrate:
    insight.pop('dt_end')
    insight['dt_difference'] = 3600
    print(OpenWeatherInsight(**insight).put(table=table))