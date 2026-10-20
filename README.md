# python-cli-todo
## 第二周作业：Todo-CLI v2 命令行待办清单
## 项目简介
基于Python开发的命令行待办任务工具，使用JSON文件持久化存储任务，代码采用模块化拆分，并增加异常捕获提升程序稳定性。

## 功能指令
| 命令 | 作用 |
|------|------|
| add 任务名称 | 添加新任务 |
| list | 展示全部任务 |
| complete 编号 | 标记任务为已完成 |
| delete 编号 | 删除指定编号任务 |
| quit | 保存任务并退出程序 |

## 环境要求
Python 3.8 及以上版本

## 运行方式
```bash
# 克隆仓库（补上.git）
git clone https://github.com/18982834376qzq-collab/-.git
# 进入项目目录
cd python-cli-todo
# 运行程序
python main.py
```
## 技术实现要点

- JSON 文件持久化保存数据
- 代码模块化拆分
- try-except 异常捕获处理非法输入


