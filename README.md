# kuromoji-sudachi-memory-test
OpenSearchにおいて、sudachiとkuromojiの形態素解析におけるヒープメモリの利用量を比較したい

## 検証の流れ
1. GCを発生させないため、OpenSearchのGCをEpsilonGCに変更して起動
2. Wikipediaの文書を79250件(jawiki-latest-pages-articles1分)入れる
3. ヒープダンプを取得してヒープメモリの状況確認

## 検証バージョン
* OpenSearch: 2.11.1
* kuromoji: OpenSearch2.11.1に同梱のもの(lucene9.8.0)
* elasticsearch-sudachiプラグイン: v3.1.0
* sudachi辞書 :v20230927-core


## 取得コマンド
GCを発生させたくないので`-all`を付与してGC取得する
```
jps -v
jcmd ${process_id} GC.heap_dump -all heapdmp.hprof
jcmd 105 GC.heap_dump -all heapdmp.hprof
```

## 結果
79250件insert(失敗)
### Sudachi
heap2GBでは、40件insertしたところでcircuit_breaking_exceptionが発生java。
heap4GBでは、384件insertしたところでcircuit_breaking_exceptionが発生java。

### kuromoji
heap2GBでは、509件insertしたところでcircuit_breaking_exceptionが発生。
heap4GBでは、8193件insertしたところでcircuit_breaking_exceptionが発

## 追加検証
思ったよりSudachiのcircuit_breaking_exceptionが早かったので、40件入れた状態のメモリ利用量を取得
### Sudachi
unreachable objectsの合計は1,963,734,816となった。
```
Class Name                            |    Objects |  Shallow Heap
-------------------------------------------------------------------
Total: 60 of 4,272 entries; 4,212 more| 37,714,248 | 1,963,734,816
-------------------------------------------------------------------
```

### kuromoji
unreachable objectsの合計は1,753,523,896となった。
```
Class Name                            |    Objects |  Shallow Heap
-------------------------------------------------------------------
Total: 35 of 4,197 entries; 4,162 more| 31,544,374 | 1,753,523,896
-------------------------------------------------------------------
```


### standard
比較のためstandard analyzerでも取得してみると1,710,096,048になった
```
Class Name                            |    Objects |  Shallow Heap
-------------------------------------------------------------------
Total: 35 of 4,089 entries; 4,054 more| 30,860,648 | 1,710,096,048
-------------------------------------------------------------------
```

## まとめ
追加検証でのstandard-kuromojiの差分が43MBであるのに対して、standard-sudachiの差分は253MBとなった。
メモリ使用量の差分が約6倍ということで、circuit_breaking_exceptionの発生タイミングの差もそれっぽい
