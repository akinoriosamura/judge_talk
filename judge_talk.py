# !/usr/bin/env python
# coding: utf-8
import argparse
import io
import sys
import codecs
import datetime
import locale

# sample: python judge_talk.py gs://judge_talk/sample.flac

def transcribe_gcs(gcs_uri, save_name):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        sample_rate_hertz=48000,
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        #language_code='en-US')
        language_code='ja-JP')

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    operationResult = operation.result()

    fout = codecs.open(save_name, 'a', 'utf-8')

    for result in operationResult.results:
      for alternative in result.alternatives:
          fout.write(u'{}\n'.format(alternative.transcript))
    fout.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='GCS path for audio file to be recognized')
    args = parser.parse_args()
    d = datetime.datetime.today()
    today = d.strftime("%Y%m%d-%H%M%S")
    save_name = 'output{}.txt'.format(today)
    transcribe_gcs(args.path, save_name)

    with open(save_name) as f:
        content = f.read()
        print(len(content))
        if len(content) > 100:
            print("talking video")
        else:
            print("not talking video")
