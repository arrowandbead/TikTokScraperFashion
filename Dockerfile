FROM python:3.9
ARG chromedriver_url="https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_mac64.zip"
ARG num_videos=100
ENV NUM_VIDEOS $num_videos
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "main.py"]