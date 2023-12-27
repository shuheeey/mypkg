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

### 実行方法

```bash
$ ros2 run mypkg talker
```

### 実行結果

```bash
(何も表示されない)
```

## listener
* サブスクライバーを持つノードである。
* トピック/countupを通じてメッセージを受け取り、そのまま出力する。

### 実行方法

端末１でtalkerを動かし、端末２で以下のようにlistenerを動かす

```bash
$ ros2 run mypkg listener
```

### 実行結果

```bash
[INFO] [1703677804.729422151] [listener]: Listen: 0
[INFO] [1703677805.217397200] [listener]: Listen: 1
[INFO] [1703677805.717381445] [listener]: Listen: 2
[INFO] [1703677806.217560241] [listener]: Listen: 3
[INFO] [1703677806.717461928] [listener]: Listen: 4
[INFO] [1703677807.217671900] [listener]: Listen: 5
[INFO] [1703677807.717565586] [listener]: Listen: 6
[INFO] [1703677808.217695207] [listener]: Listen: 7
[INFO] [1703677808.717276717] [listener]: Listen: 8
[INFO] [1703677809.217362977] [listener]: Listen: 9
[INFO] [1703677809.717622603] [listener]: Listen: 10
```

## talker1
* パブリッシャーをもつノードである。
* トピック/countupを通じてメッセージを送信する。
* メッセージの型はInt16。
* 60秒間メッセージを送信する。メッセージを送っている間は"送信中"と表示され、60秒たったら"終了"と表示される。

### 実行方法

```bash
$ ros2 run mypkg talker1
```

### 実行結果

```bash

```

## listener1
* サブスクライバーを持つノードである。
* トピック/countupを通じて受け取ったメッセージを足し合わせていき出力する。
* 足し合わせた合計値が素数であれば、素数であると表示する。さらに受け取ったメッセージの値が素数であるときも、素数であると表示する。

### 実行方法

端末１でtalker1を実行し、端末２で以下のようにlistener1を実行する

```bash
$ ros2 run mypkg listener1
```

### 実行結果

```bash

```

## listener2
* サブスクライバーを持つノードである。
* 実行してからの経過時間を10秒刻みで表示する。

### 実行方法

端末１でtalker1を実行し、端末２で以下のようにlistener2を実行する

```bash
$ ros2 run mypkg listener2
```

### 実行結果

```bash

```

## listener3
* サブスクライバーを持つノードである。
* STARTとFINISHを表示させる。
* このコードを実行している間に大谷選手はどれだけ稼げて、自分はどれくらいしか稼げないかを計算し出力する。

### 実行方法

端末１でtalker1を実行し、端末２で以下のようにlistener3を実行する

```bash
$ ros2 run mypkg listener3
```

### 実行結果

```bash

```

# ローンチ

## talkerとlistener
talkerとlistenerの２つのノードを１つの端末で同時に実行する


## talker1とlistener1, listener2, listener3
talker1とlistener1, listener2, listener3の４つのノードを１つの端末で同時に実行する


# 必要なソフトウェア
* ROS2
* Python

# テスト環境
Ubuntu 22.04.2 LTS

# ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再配布および使用が許可されます。
* このパッケージのコードの一部は、Ryuichi Ueda氏の以下のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）を参考に、本人の許可を得て改変し自身の著作としたものです
  * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2023 Shuhei Yanagihori
