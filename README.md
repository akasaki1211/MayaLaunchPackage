# MayaLaunchPackage

Mayaを起動するbat、各種設定ファイル、追加プラグイン、スクリプトなどをひとまとめにしたパッケージです。

## 背景
以前はあえて1フォルダにすべてまとめずに、必要な場所から必要なものだけを参照するよう構成していたのですが
チーム（会社）外の方へ同一環境を用意してもらう際など、プロジェクト外の要因で環境が変わってしまうケースが多く
「プロジェクトで使用する必要最低限の設定は全てこのパッケージに収める」という運用で落ち着きました。

## 設計上のポイント
* パッケージフォルダの設置以外に作業者に行ってもらうことがないようにする。※Mayaなどのインストールは除きます。
* パッケージフォルダ（=PRJ_Mayaフォルダ）をどこに置かれても同一環境で起動するよう可能な限り相対パスで記述する。
* 同プロジェクト内でさらに起動方法を分岐できる。モデラー用、アニメーター用など。（=REGION）

## 使用方法
