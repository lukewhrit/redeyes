# 🌹 Redeyes

Redeyes is an extremely simple and compact url shortener in Python.

It is built with Flask and supports a wide range of different shortening styles and configuration methods. The primary and currently only database adapter is built using psycopg, for PostgreSQL, but redeyes is built in a way which it can be extended with many other adapters in the future.

**Abilities and Features:**

- Extensible design, but sane by default.
- Compact: it only requires a single server running Python and a database.
- Pure and pretty HTML UI; completely JavaScript-free!
- Simplistic— only two routes.
- Expiring links.
- Manage short links via a dashboard.
- Admin page and account system.
- Require password for links.

## Table of Contents

- [🌹 Redeyes](#-redeyes)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [via Docker](#via-docker)
    - [via PyPi](#via-pypi)
    - [Manual](#manual)
  - [Documentation](#documentation)
    - [Usage](#usage)
      - [API Routes](#api-routes)
        - [`/shorten`](#shorten)
        - [`/fetch`](#fetch)
    - [Configuration](#configuration)
      - [Host](#host)
      - [Port](#port)
      - [Slug Length](#slug-length)
      - [DSN](#dsn)
    - [API Reference](#api-reference)
  - [TODO](#todo)
  - [License](#license)

## Installation
### via Docker
### via PyPi
### Manual
## Documentation

### Usage

> [!TIP]
> Redeyes can be accessed on the web at [https://rdy.es](https://rdy.es).

#### API Routes

The API can be accessed at the `/api/v1/` prefix.

##### `/shorten`

* **Accepts:** `application/json`, `multipart/form-data`
* **Body Parameters:**
  * `link`: `string`: The long form URL you wish to shorten
* **Returns:**
  * `200 {"short":""}`: The random identifier for the shortened URL
  * `415 Unsupported Media Type`: Triggers when the Content-Type is not `application/json` or `multipart/form-data`
  * `400 Bad Request`: Triggers when `link` is missing or not a valid URL

##### `/fetch`
* **Query Parameters:**
  * `short`: `string`: The shortened URL identifier
* **Returns:**
  * `200 {"long":""}`: The long form URL
  * `400 Bad Request:` Missing required `short` parameter
  * `404 Not Found`: Could not find link for provided identifier

### Configuration

Redeyes is configurable via environment variables. All environment variables are prefixed with `REDEYES_`. All variables have default values, but you will probably want to set a value for at least `DSN`.

#### Host

`HOST` is the IP address/domain you wish to make the redeyes instance accessible on.

By default, `0.0.0.0`. This value is most likely good enough for your purposes, but feel free to change it.

#### Port

`PORT` is the port on which you wish to make the redeyes instance accessible.

By default, `80`.

#### Slug Length

`SLUG_LENGTH` is the length of the ids redeyes will generate when shortening URLs. Note that by making this value too low, you may begin to run into issues as the maximum possible combinations may now be too few to function properly.

By default, `6`.

#### DSN

`DSN` represents the connection string for the PostgreSQL database you wish to use. The format of these connection strings is available [here, on the Postgres docs](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING). Generally though, the format is as follows:

```
host=localhost port=5432 dbname= user=
```

By default, it uses `redeyes` for the dbname and user fields.

### API Reference

## TODO

- [X] Implement database functionality
- [X] API Routes
- [ ] Rate-limiting
- [ ] Error handling
  - [ ] Logging

## License

Redeyes is available under the [GNU General Public License, v3](LICENSE).
