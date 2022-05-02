# MayaLaunchPackage

Mayaを起動するbatファイル、各種設定ファイル、追加プラグイン、スクリプトなどをひとまとめにしたフォルダです。

## 背景
以前はあえて1フォルダにすべてまとめずに、社内の共有サーバなど各所から必要なものだけを参照するよう構成していました。
しかし、チーム（会社）外の方へ同一環境を用意してもらう際、パスの引き直しや必要ファイルの設置が煩雑で、準備に手間がかかりました。
このような背景から「プロジェクトで使用する必要最低限の設定は全てこのパッケージに収めてしまう」という運用で落ち着きました。

## 設計上のポイント
* パッケージフォルダの設置以外に作業者に行ってもらうことがないようにする。※Mayaなどのインストールは除きます。
* パッケージフォルダ（=PRJ_Mayaフォルダ）をどこに置かれても同一環境で起動するよう可能な限り相対パスで記述する。
* 同プロジェクト内でさらに起動方法を分岐できる。モデラー用、アニメーター用など。（=REGION）
* 各PCローカルの設定ファイル（C:\Users\<ユーザー名>\Documents\maya）を本パッケージにより改変しない。

## 起動方法
PRJ_Mayaフォルダを好きな場所に設置し、PRJ_Maya\_ANI(又は_MDL)\bat内にあるバッチファイルを実行するとMayaが起動します。

## 改変方法
### 環境変数, Mayaバージョンなどの設定
PRJ_Maya\_ANI(又は_MDL)\bat内にあるPRJ_maya2022_en_US.bat内の記述を編集します。
冒頭の4行で各相対パスを取得しています。
    set BAT_PATH=%~dp0
    set REGION_PATH=%BAT_PATH:bat\=%
    set REGION=%REGION_PATH:~-5,4%
    set ROOT_PATH=%REGION_PATH:~0,-5%
    
それ以降は環境変数の設定やスクリプトパスなどの設定です。
基本は相対パスから設定するように記述してあります。
※MAYA_PROJECTのみ起動パッケージと関連性が無いので絶対パスになっています。

### 起動時に実行したいスクリプトの設定
以下のuserSetup.pyに記述します。
PRJ_Maya\scripts\userSetup.py・・・共有
PRJ_Maya\_ANIなど\scripts\userSetup.py・・・REGION固有

参考までに以下の3つの関数を記述してあります。
* loadPlugin　・・・Maya起動時に指定プラグインをロードします。
* setfps　・・・NewScene実行時（起動時含む）にタイムレンジやフレームレートの設定を行います。
* drawHUD　・・・起動時にビューポートの左下に文字列を表示します。例：Running in PRJ_ANI mode (PY3)

### プロジェクト名
「PRJ_Maya」フォルダの「PRJ」の部分を任意の文字列に変更します

### REGION
PRJ_Maya内の「&underscore;ANI」「&underscore;MDL」がREGIONです。このフォルダの名前・数は任意ですが、フォルダ名を4文字以外に変更する場合は
バッチファイル内の以下の2行を変更する必要があります。
    set REGION=%REGION_PATH:~-5,4%
    set ROOT_PATH=%REGION_PATH:~0,-5%

例）REGIONフォルダ名を「MODEL」など5文字にした場合
    set REGION=%REGION_PATH:~-6,5%
    set ROOT_PATH=%REGION_PATH:~0,-6%

### 必要scripts, plug-ins, modulesの設置
PRJ_Maya直下のscripts, plug-ins, modulesはREGIONに関係なく共通でパスを参照するようbatファイルに記述してあります。
REGIONごとに固有のパスを参照したい場合はPRJ_Maya\_ANI(又は_MDL)内のscriptsフォルダが該当します。

### スプラッシュスクリーン
PRJ_Maya\icons内にMayaStartupImage.pngという名前で任意の画像ファイルを設置すると、起動時に表示されます。
