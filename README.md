# プロジェクト概要

このリポジトリは、ICLR: In-Context Learning of Representations (https://arxiv.org/abs/2501.00070) の再現実験のために作成されました。

## 必要なライブラリ

必要なライブラリとそのバージョンは、`requirements.txt`ファイルに記述されています。

## 実行方法

1.  必要なライブラリをインストールします。
    ```bash
    pip install -r requirements.txt
    ```
2.  実験を実行します。
    ```bash
    python experiment.py
    ```
3.  評価を実行します。
    ```bash
    python evaluation.py
    ```
4.  グラフを作成します。
    ```bash
    python graph.py
    ```

## 各ファイルの役割

*   `model.py`: モデルの定義
*   `experiment.py`: 実験の実行
*   `evaluation.py`: 評価の実行
*   `graph.py`: グラフの作成
*   `analysis.py`: 実験結果の分析
*   `test.py`: テスト
*   `save_experiment_data.py`: 実験データの保存
*   `experiment_settings.md`: 実験設定
*   `walk.py`: グラフ上のランダムウォークを生成する関数

## ライセンス

MIT
