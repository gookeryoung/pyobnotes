---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:25:43 晚上
title: 'compile(source, Filename, Mode, flags=0, dont_inherit=False, optimize=-1)'
---

# compile(source, Filename, Mode, flags=0, dont_inherit=False, optimize=-1)

将 source 编译成代码或 AST 对象，可被 exec() 或 eval() 执行。

## 参数说明

- source 可以是常规的字符串、字节字符串，或者 AST 对象；
- filename 是代码读取的文件名，如果不从文件中读取，则可传入一些可辨识值，例如 `'<string>'`；
- mode 指定了编译代码模式：
	- 若 source 是语句序列，可以是 `'exec'`；
	- 若是单一表达式，可以是 `'eval'`；
	- 若是单个交互式语句，可以是 `'single'`，这种情况下，若表达式执行结果不是 None 将会被打印出来。
- 可选参数 flags 和 dont_inherit 用于控制激活编译器选项，具体需参考 ast 模块中带有 `PYCF_` 前缀的选项；
- 可选参数 optimize 用于指定编译器优化级别：
	- -1 和 0 相同（代表没有优化， `debug` 为真）；
	- 1（断言被删除，`debug` 为假）；
	- 2（文档字符串也被删除）。

## 示例

```python
s1 = 'lis = [x**3 for x in range(10)]'
# {str}'[x**3 for x in range(10)]'
c1 = compile(s1, '<string>', 'exec')
# {code}<code object <module> at 0x????????, file"<string>", line 1>
c2 = eval(c1)
# c2:None
# lis:{list:10}[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```
