# Features

## Base Host: http://127.0.0.1:8000/service/
- There are several rest APIs for fetching data.
    - You can get all data on **/getData/**.
    - You can get filtered data on **/getData/<key_to_filter>/value/**
        - Such as **/getData/genre/Platformer/** or **/getData/title/LittleBigPlanet%20PS%20Vita/**.
    - UI can be accessed on **/getView/** which gives the Dashboard and search filter to type on.
    - Search filter works for any field type and it will only filter if it **Starts with** the search query.
    - You can insert the data to DB by calling the endpoint **/insert/**.
    - Flush the DB by running **python manage.py flush**.