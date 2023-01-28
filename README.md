# Speech-To-Text Transcription and Summarization Web Application: Unlocking the Power of Whisper and Transformers

#### Language and Libraries

<p>
<a><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" alt="python"/></a>
<a><img src="https://img.shields.io/badge/openai-181818?style=for-the-badge&logo=openai&logoColor=white" alt="numpy"/></a>
<a><img src="https://img.shields.io/badge/whisper-181818?style=for-the-badge&logo=openai&logoColor=green" alt="opencv"/></a>
<a><img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" alt="pytorch"/></a>
<a><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)" alt="docker"/></a>
<a><img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)" alt="aws"/></a>
<a><img src="https://img.shields.io/badge/circleci-343434?style=for-the-badge&logo=circleci&logoColor=white" alt="pandas"/></a>
</p>


## Problem statement
The goal of this project is to develop a web application that allows users to upload a video or provide a video link and automatically transcribe the video's audio into text, with the option to translate it to a different language. Additionally, the application will summarize the transcribed text to provide a brief overview of the video's content. The application will be built using the Flask framework and utilize the VideoToSubtitle, summarize, and video_downloader components. The project aims to make it easy for users to transcribe and understand the content of videos with minimal effort.

## Solution Proposed
The proposed solution for this project utilizes OpenAI's Whisper model to transcribe the audio of the video into text. For downloading YouTube videos, the PyTube library is used. To summarize the transcribed text, the BART-Large model is utilized. The application is built using the Flask framework and consists of three main components: video downloader, subtitle generator, summarizer.

### Components
- The video downloader component uses `PyTube` library to download the video from YouTube or accepts a video file uploaded by the user. 

- The subtitle generator component uses the `OpenAI's Whisper model` to transcribe the audio of the video and has the option to translate the transcript to a different language. 

- The summarizer component uses the `BART-Large model` to generate a summary of the transcribed text.

The user interacts with the application through a web interface, where they can upload a video file or provide a YouTube video link. The application processes the video, generates a transcript, and provides a summary of the video's content. The transcript and summary are displayed on the web page, allowing the user to easily understand the video's content. This solution aims to make it simple and easy for users to transcribe, translate and summarize videos with minimal effort.

### Deployment
This project also utilizes `CircleCI` for continuous integration and deployment using `Docker`. Docker allows to package an application and its dependencies in a virtual container that can run consistently across different environments.

CircleCI is configured to automatically build and test the application inside a Docker container after each code change is pushed to the source code repository. After successful testing, the application is then deployed to an `Amazon Web Services (AWS)` `Elastic Compute Cloud (EC2)` instance. This approach allows for easy and efficient updating and scaling of the application, as well as facilitating collaboration among the development team.

The use of CircleCI, AWS EC2 and Docker allows for a smooth and streamlined deployment process, ensuring that the application is always up-to-date and running efficiently in a consistent environment. This will also ensure that the application can be easily deployed and tested on different environments and platforms.

## How to run?

### Step 1: Clone the repository
```bash
git clone my repository link 
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -p env python=3.10 -y
```

```bash
conda activate env
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Run the application server
```bash
python app.py
```

### Step 6. Open the application
```bash
http://localhost:5000
```

## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image

```
docker build vsum -t . 
```
3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGEID>
```

👨‍💻 Tech Stack Used
1. Python
2. Flask
3. Pytorch
4. Docker
5. Transformers

🌐 Infrastructure Required.
1. AWS EC2
2. AWS ECR
3. Circle CI


## `videosum` is the main package folder which contains 

## Conclusion
One potential area for improvement in this project could be the integration of more advanced natural language processing techniques to improve the accuracy of the transcriptions and summaries like spell checks and  Additionally, the application could be enhanced to support more languages for transcription and translation.

This application could be used in a wide range of real-world scenarios, such as in the entertainment industry for subtitle generation, in education for creating transcripts of lectures, and in business for creating summaries of meetings and presentations. It could also be useful for individuals who have difficulty hearing or understanding spoken language, such as people with hearing impairments.


=====================================================================