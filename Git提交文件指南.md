# Git 提交文件操作指南

## 基本流程

1. 本地新建仓库 mkdir 文件夹名

2. 右键打开 git bash

3. 初始化仓库 git init
    > 把这个文件夹变成Git可管理的仓库

4. 添加文件
    > 将项目粘贴到此仓库里
    > 添加单个文件：git add 目录/文件名
    > 添加文件夹： git add 文件夹目录
    > 添加所有文件：git add .

5. 提交文件
    > git commit -m"commit description"

6. 关联远程仓库
    > 在Github上新建仓库，复制网址
    > 提示输入用户名、邮箱和密码
    > git config --global user.name "user.name"
    > git config --global user.email "yourmail@youremail.com.cn"
    > windows 系统会弹出一个UI让你输入Github用户名和密码
    > git remote add origin https:/github.com/QiWang-SJTU/AID1906.git

7. 将本地仓库内容推送到远程仓库
    > git push -u origin master
    > 由于新建的远程仓库是空的，所以要加上-u这个参数，等远程仓库里面有了内容之后，下次再从本地库上传内容的时候只需下面这样就可以了：
    > git push origin master

8. Github上查看上传内容

## 注意事项(多个坑记录)

1. 文件目录有空格用 \ 代替：git add DataStructure\ And\ Algrithm/

2. Github创建远程仓库的时候，如果勾选了Initialize this repository with a README，那么当你push的时候就会报错，提示README文件不在本地仓库中。这时需要通过以下命令先将内容合并，再push就能成功了
    > git pull --rebase origin master

3. git add 后提示 The file will have its original line endings in your working directory.
    > 解决办法：git config -–global core.autocrlf false
    > 原因：路径中存在 / 的符号转义问题，false就是不转换符号。默认是true，相当于把路径的 / 符号进行转义，这样添加的时候就有问题。

4. git commit 后提示 fatal: Unable to create index.lock File exists.
    > 解决办法： 在.git文件夹下删除index.lock文件。
    > Linux：rm -f .git/index.lock

5. git remote 后提示 fatal: remote origin already exits.
    > 解决办法：git remote rm origin 再提交就好了

## 更新仓库文件

1. 将文件copy到仓库指定目录下

2. git add 目录/文件夹

3. git commit -m"描述"

4. git remote add origin 远程仓库网址

5. git push origin master

## 其他

- git status 查看当前仓库状态
- 本地仓库到远程仓库是深拷贝
