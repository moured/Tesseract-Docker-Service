# OCR Webservice

This is a simple OCR webservice that uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) to perform OCR on images.

## Usage

The webservice currently features the following endpoints:

- `GET /heartbeat` - Returns `OK` if the webservice is running

- `POST /ocr/single` - Performs OCR on an image and returns the result as a JSON object\
Parameters:
    - `image` - The image to perform OCR on (in the form of a base64 encoded string)

## Running the webservice

1. Make sure you have [Docker](https://www.docker.com/) installed
2. Install [Docker Compose](https://docs.docker.com/compose/install/) if it is not already installed
3. Clone this repository
4. Run `docker-compose up` in the root directory of the repository