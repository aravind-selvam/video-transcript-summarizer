import os

from flask import Flask, render_template, request

from videosum.components.generate_subtitle import Config, VideoToSubtitle
from videosum.components.summarize import summarize_text
from videosum.components.video_downloader import VideoDownloader

app = Flask(__name__)
app.config['upload_dir'] = os.path.join('uploads/')
os.makedirs(app.config['upload_dir'], exist_ok=True)


@app.route('/', methods=['GET'])
def index():
    """
    It renders the index.html file in the templates folder

    Returns:
      The index.html file is being returned.
    """
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def upload_file():
    """
    The function upload_file() takes in a video file or a video link, transcribes the video, and
    summarizes the transcript

    Returns:
      the transcript and summary text.
    """
    if request.method == 'POST':
        video_file = request.files["video_file"]
        subtitle_generator = VideoToSubtitle(config=Config)
        if video_file:
            filename = video_file.filename
            video_path = os.path.join(os.path.join(
                app.config['upload_dir'], filename))
            video_file.save(video_path)
            task = 'transcribe'
            if len(request.form.getlist('translate-btn')) > 0:
                task = 'translate'
                print("translate task is selected:", task)
            subtitle = subtitle_generator.get_subtitle(video_path=video_path,
                                                       model='tiny', task=task, verbose=False)
        else:
            video_link = request.form["link-input"]
            downloader = VideoDownloader(
                url=video_link, save_path=app.config['upload_dir'])
            video_path = downloader.download()
            task = 'transcribe'
            option = request.form.get('options')
            if option == 'translate':
                task = 'translate'
                print("translate task is selected:", task)
            print("task selected:", task)
            subtitle = subtitle_generator.get_subtitle(video_path=video_path,
                                                       model='tiny', task=task, verbose=False)

        transcript_text = subtitle[1]['text']
        summary_text = summarize_text(transcript_text)
        return render_template('index.html', transcript=transcript_text, summary=summary_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
