# Text Emotion Detection with Flask and Docker

This project is a Text Emotion Detection application built with Flask, which loads a pre-trained model to predict emotions based on text input. The app also provides probabilities for each emotion class and displays an emoji representation of the predicted emotion. The app is dockerized for easy deployment.

## Features

- Predicts emotions in text input using a pre-trained model.
- Shows confidence scores for each emotion.
- Uses Flask for the backend and Docker for containerization.

## Project Structure

```
Text Emotion Detection/
├── app.py                # Main Flask app
├── model/
│   └── text_emotion.pkl   # Pre-trained model file
├── requirements.txt       # Dependencies
├── Dockerfile             # Docker configuration
└── templates/
    └── index.html         # HTML template for the app
```

## Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8+
- Docker

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/srivigneshs09/text-emotion-detection.git
cd text-emotion-detection
```

### 2. Install dependencies

If you'd like to run the app locally without Docker, you can install dependencies via `pip`:

```bash
pip install -r requirements.txt
```

### 3. Run the Application Locally (Optional)

To test the app without Docker, you can run the Flask application with:

```bash
python app.py
```

## Dockerization

The application can be run in a Docker container. Follow these steps to build and run the Docker container.

### 1. Build the Docker Image

In the project directory, run:

```bash
docker build -t text-emotion-detection-app .
```

### 2. Run the Docker Container

Once the image is built, run the following command to start the container:

```bash
docker run -p 5000:5000 text-emotion-detection-app
```

Now, the app should be accessible at `http://127.0.0.1:5000` in your web browser.

### 3. Stopping the Container

To stop the container, press `CTRL+C` in the terminal where it’s running, or use the following command to stop it from another terminal:

```bash
docker ps         # Locate the container ID of the running container
docker stop <container_id>
```

## Troubleshooting

- **Error: `ERR_EMPTY_RESPONSE`**  
  Make sure `app.py` is set to listen on `0.0.0.0` by updating the code as follows:

    ```python
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
    ```

- **Viewing Docker Logs**  
  To check logs if there are issues, find the container ID and use `docker logs`:

    ```bash
    docker ps             # Locate the container ID
    docker logs <container_id>
    ```
