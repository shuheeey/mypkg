# mypkg
ロボットシステム学課題２提出用リポジトリ。

[![test](https://github.com/shuheeey/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/shuheeey/mypkg/actions/workflows/test.yml)[![test](https://github.com/shuheeey/mypkg/actions/workflows/test1.yml/badge.svg)](https://github.com/shuheeey/mypkg/actions/workflows/test1.yml)

# インストール方法
ROS2を動かすことのできる環境でこのリポジトリをクローンする。

```bash
git clone https://github.com/shuheeey/mypkg.git
```

# ノード

## トピックの説明
トピック/countupは、0.5秒ごとに0から1ずつ数字を増やしていく。

## talker
* パブリッシャーを持つノードである。
* トピック/countupを通じてメッセージを送信する。
* メッセージの型はInt16。

## listener
サブスクライバーを持つノードである。トピック/countupを通じてメッセージを受け取り、そのまま出力する。

## talker1
パブリッシャーをもつノードである。トピック/countupを通じてメッセージを送信する。メッセージの型はInt16。60秒間メッセージを送信する。メッセージを送っている間は"送信中"と表示され、60秒たったら"終了"と表示される。

## listener1
サブスクライバーを持つノードである。トピック/countupを通じて受け取ったメッセージを足し合わせていき出力する。足し合わせた合計値が素数であれば、素数であると表示する。さらに受け取ったメッセージの値が素数であるときも、素数であると表示する。

## listener2
サブスクライバーを持つノードである。実行してからの経過時間を10秒刻みで表示する。

## listener3
サブスクライバーを持つノードである。STARTとFINISHを表示させる。このコードを実行している間に大谷選手はどれだけ稼げて、自分はどれくらいしか稼げないかを計算し出力する。

# ローンチ

# 必要なソフトウェア
ROS2

Python

# テスト環境
Ubuntu 22.04.2 LTS

# ライセンス
このソフトウェアパッケージは、3条項BSDライセンスの下、再配布および使用が許可されます。
このパッケージのコードの一部は、Ryuichi Ueda氏の以下のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）を参考に、本人の許可を得て改変し自身の著作としたものです
	* [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2023 Shuhei Yanagihori
