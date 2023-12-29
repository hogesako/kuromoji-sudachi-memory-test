# kuromoji-sudachi-memory-test
OpenSearchにおいて、sudachiとkuromojiの形態素解析におけるヒープメモリの利用量を比較したい

## 検証の流れ
1. OpenSearchのGCをEpsilonGCに変更して起動
2. Wikipediaの文書を79250件(jawiki-latest-pages-articles1分)入れる
3. ヒープダンプを取得してヒープメモリの状況確認

## 検証バージョン
* OpenSearch: 2.11.1
* kuromoji: OpenSearch2.11.1に同梱のもの(lucene9.8.0)
* elasticsearch-sudachiプラグイン: v3.1.0
* sudachi辞書 :v20230927-core
