# 環境構築
- .envファイルをメンバーからもらって直下に配置する  
- 下記を参考に init-letsencrypt.sh を実行する（dataディレクトリ配下を作成するコマンド。ssh証明書を取得するのに必要）
  - https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71
- logs/django.log を作成する(これがないとエラーになるらしい)
- `$ docker-compose up`でコンテナを立ち上げる
- 成功したら`https://localhost`を開いて確認する

# 注意
- `http://localhost:8000`などではnginxの設定上、cssを取ってこれないので崩れた画面が表示されてしまう。
- Chromeの場合、`NET::ERR_CERT_INVALID`が表示され画面を表示できないことがある。
  - safariなど別のブラウザで開くか`NET::ERR_CERT_INVALID`が表示されている画面で`thisisunsafe`と入力すると表示される。

