# Dune API

The Dune API provides access to a vast collection of information related to the iconic Dune universe created by Frank Herbert. You can retrieve Dune quotes, explore various Dune books, discover their authors, delve into Dune series, explore short stories, and even find information about Dune comics and their illustrators. This API is designed to be simple to use, requiring no authentication and supporting only GET requests.

## Base URL

The base URL for accessing the Dune API is:

```
https://example.com/api/dune/
```

Replace `example.com` with the actual domain where the API is hosted.

## Endpoints

### Retrieve Dune Quotes

#### Endpoint: `/quotes/`
- Method: GET
- Description: Retrieve random Dune quotes.
- Example URL: `https://example.com/api/dune/quotes/`

### Explore Dune Books

#### Endpoint: `/books/`
- Method: GET
- Description: Get a list of all Dune books.
- Example URL: `https://example.com/api/dune/books/`

### Delve into Dune Series

#### Endpoint: `/series/`
- Method: GET
- Description: Get information about Dune series.
- Example URL: `https://example.com/api/dune/series/`

### Explore Short Stories

#### Endpoint: `/short-stories/`
- Method: GET
- Description: Get a list of Dune short stories.
- Example URL: `https://example.com/api/dune/short-stories/`

### Find Dune Comics and Illustrators

#### Endpoint: `/comics/`
- Method: GET
- Description: Get information about Dune comics and their illustrators.
- Example URL: `https://example.com/api/dune/comics/`

## Usage

To use the Dune API, simply make GET requests to the desired endpoints as shown in the examples above. You will receive JSON responses with the requested Dune-related information.

## Rate Limiting

This API has a rate limiting policy in place to ensure fair usage. The rate limits are as follows:

- Requests per minute: 60
- Requests per hour: 1000

## Feedback and Support

If you have any feedback, questions, or need support, please feel free to contact us at support@example.com.

---

