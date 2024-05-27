We are expecting to receive a simple application that shows your programming skills and knowledge. We consider that the average time to implement this project it's about 5 hours but because we understand you are a busy person you have a maximum of 48 hours after you receive the test to send us your answer.

We will evaluate the following:

+ REST API with CRUD operations.
+ Link to the repository (Github, Bitbucket)

You are working for a startup called Melp, which has a revolutionary idea about building an app that will provide useful information about restaurants to users.

You were provided with a CSV which contains raw data about the restaurants. Your first job consists in importing the raw data into a relational database and expose a REST API that implements CRUD (Create, Read, Update, Delete) operations.

The Restaurant table needs to have the following schema:

```sql
Restaurants (
  id TEXT PRIMARY KEY, -- Unique Identifier of Restaurant
  rating INTEGER, -- Number between 0 and 4
  name TEXT, -- Name of the restaurant
  site TEXT, -- Url of the restaurant
  email TEXT,
  phone TEXT,
  street TEXT,
  city TEXT,
  state TEXT,
  lat FLOAT, -- Latitude
  lng FLOAT) -- Longitude
```

You can find the CSV with the raw data at the following link (it contains dummy data): https://example.com/restaurantes.csv

Your second task consists in implementing the following endpoint:

```
/restaurants/statistics?latitude=x&longitude=y&radius=z
```

It receives latitude and a longitude as parameters, which correspond to the center of a circle, and a third parameter that corresponds to a radius in METERS.

Hint: A tool like PostGIS or equivalent may help you with the spatial queries ;)

This endpoint needs to return a JSON with the following data:

```
{
  count: Count of restaurants that fall inside the circle with center [x,y] y radius z,
  avg: Average rating of restaurant inside the circle,
  std: Standard deviation of rating of restaurants inside the circle
}
```

When you are finished, upload your project to:

https://www.heroku.com/

Once deployed send us the following:

+ Link to the heroku app
+ A Postman collection (https://www.getpostman.com/docs/collections) to test your API.

Bonus Points:

+ Endpoint with statistical data.
+ Deployment of the project.
+ Good use of Git.
+ Documentation of the API.
+ Correct use of HTTP verbs.
+ Good programming practices.
