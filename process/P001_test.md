- [1. P01 test](#1-p01-test)
  - [1.1. 目的](#11-目的)
  - [1.2. 関係青果物](#12-関係青果物)
    - [1.2.1. 入力青果物](#121-入力青果物)
    - [1.2.2. 出力青果物](#122-出力青果物)

# 1. P01 test

## 1.1. 目的

- ＊＊＊＊＊＊を目的とするしれない

## 1.2. 関係青果物

### 1.2.1. 入力青果物

- D01_dTest1
- D02_dTest2

### 1.2.2. 出力青果物

- D03_dTest3

```mermaid
flowchart TD
    p01([P003_pTest3])
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click p01 "lop9940/link_fix/blob/master/process/P003_pTest3.md" %% url check NG
    p02([P004_pTest2])
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click p02 "lop9940/link_fix/blob/master/process/P004_pTest2.md" %% url check NG
    p03([P002_pTest1])
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click p03 "lop9940/link_fix/blob/master/process/P002_pTest1.md" %% url check OK
    p04([P005_pTest4])
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click p04 "lop9940/link_fix/blob/master/process/P005_pTest4.md" %% url check NG

    d01[/D001_dTest1/]
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click d01 "lop9940/link_fix/blob/master/document/D001_dTest1.md" %% url check OK
    d02[/D002_dTest2/]
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click d02 "lop9940/link_fix/blob/master/document/D002_dTest2.md" %% url check NG
    d03[/D003_dTest3/]
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click d03 "lop9940/link_fix/blob/master/document/D003_dTest3.md" %% url check NG
    d04[/D004_dTest4/]
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click d04 "lop9940/link_fix/blob/master/document/D004_dTest4.md" %% url check NG
    d05[/D005_dTest5/]
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click d05 "lop9940/link_fix/blob/master/document/D005_dTest5.md" %% url check NG
    d06[/D006_dTest6/]
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click d06 "lop9940/link_fix/blob/master/document/D006_dTest6.md" %% url check NG
    d07[/D007_dTest7/]
    %% このリンクはGithub actionsでの自動生成です。ノード名が変更になっても修正不要です。
    click d07 "lop9940/link_fix/blob/master/document/D007_dTest7.md" %% url check NG

    d01-->p01
    d01-->p02
    p01-->d05
    p01-->d06
    p02<-->|更新|d04
    p02-->d05
    d06-->p03
    d02-->p03
    p03-->d07
    d07-->p04
    p04-->d03
```
