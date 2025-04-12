# 😄 感情認識アプリ（Flask + TensorFlow）

このアプリは、画像から人の感情（喜び、怒り、悲しみなど）を判別するWebアプリケーションです。PythonのFlaskとTensorFlowを使用して構築されており、FER2013データセットで学習したモデルを利用しています。

---

## 🚀 主な機能

- 顔画像をアップロードして、感情をリアルタイムで推定
- 結果を日本語で表示
- 推定結果の履歴をCSVファイルに保存
- ダークモード対応のシンプルなUI
- スピナー＆「感情を分析中…」のアニメーション付き

---

## 🛠 使用技術

- Python 3.10
- Flask 3.0.0
- TensorFlow 2.15.0
- OpenCV
- pandas / numpy
- HTML, CSS, JavaScript

---

## 📂 ディレクトリ構成

emotion-app/
├── app.py                        # Flaskメインアプリ
├── train_model.py                # 学習用スクリプト（オプション）
├── model/
│   └── emotion_model.h5         # 学習済みモデル
├── static/
│   ├── style.css                # スタイル（ダークモード対応）
│   └── script.js                # アニメーション・JS処理
├── templates/
│   └── index.html               # フロントエンドHTMLテンプレート
├── emotion_log.csv              # 感情履歴ログ
├── requirements.txt             # 必要なライブラリ一覧
└── README.md                    # プロジェクト概要（このファイル）


---

## 🖼️ 対応感情ラベル（7クラス）

- 😄 喜び（Happy）
- 😠 怒り（Angry）
- 😞 悲しみ（Sad）
- 😮 驚き（Surprise）
- 😐 中立（Neutral）
- 😣 恐れ（Fear）
- 🤢 嫌悪（Disgust）

---

## 🔧 セットアップ方法

```bash
git clone https://github.com/yourusername/emotion-app.git
cd emotion-app
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

ブラウザで http://localhost:5000 にアクセスしてください。

📊 ログファイルについて
emotion_log.csv に各推定結果が以下のように記録されます：

Timestamp	Emotion
2025-04-12 10:30:12	喜び
2025-04-12 10:31:07	怒り

👤 作成者
チャン・バン・ユアン (Trần Văn Doanh)


💡 今後の改善点
カメラ撮影からのリアルタイム感情認識

モバイル対応

MongoDB保存 & 履歴閲覧機能
