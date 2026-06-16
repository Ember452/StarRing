# indexer.py - 代码 AST 解析 → 向量化入库
# 1. tree-sitter 解析 Java 代码 AST
# 2. 按 类/方法 粒度切分代码片段
# 3. 调用 embedding 模型向量化
# 4. 写入 Chroma Collection