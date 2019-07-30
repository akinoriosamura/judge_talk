# judge_talk
動画のtalking判定  

## install
```
pip install ffmpeg
```

## Flow
 - mp4動画を`/videos/に配置  `
 - 動画を音声に変換  
```
python video2voice.py ./videos/sample.mp4 ./voices/sample.flac
```
 - Google speech apiが使える状態に  
 https://qiita.com/knyrc/items/7aab521edfc9bfb06625
 - 作成したflacファイルを上で作成したバケットに追加  
 - Google音声認識で、動画音声を読み込ませて1000文字以上ならtalkingと判定  
 ```
 ・バケット名：judge_talk、音声ファイル名：sample.flacの時、
 python judge_talk.py gs://judge_talk/sample.flac
```

## price
 - 最初の60min	無料   
 - 以後	0.006$/15sec    
(30m -> 70円)     

## processing time
 - 合計約動画時間の半分
