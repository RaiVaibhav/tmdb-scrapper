# Movie Search using TMDB API

A UI for which help user in filtering the movies on the basis of their popularity, using TMDB API


## Platform

```
    python: 3.7.1
    vs code: 1.25.1
    ubuntu: 18.04
```

## Dependencies

- **`Django`**: A high-level Python web framework.
- **`tmdbsimple`**: A Python wrapper on the TMDb V3 API.


### Install Dependencies

- **Set API_KEY in environment variable:**
    **On local platform**
  ```
    export API_KEY=<your-tmdb-token>
  ```
  **On heroku**
  ```
    heroku config:set API_KEY=<your-tmdb-token>
  ```

- **For pip:**
  ```
    python3 -m virtualenv <environment name>
    source <environment name>/bin/activate
    pip install -r requirements.txt
  ```

### Run
    ```
        python manage.py runserver
    ```

### Demo
**Url** - https://tmdb-spoonshot.herokuapp.com/


![demogif](https://user-images.githubusercontent.com/22278438/50423846-e443de80-0880-11e9-96eb-eb9032656e9c.gif)
