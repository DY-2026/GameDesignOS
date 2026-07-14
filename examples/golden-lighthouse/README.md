# Golden Lighthouse

这是 GameDesignOS 的公开 synthetic 黄金路径，用来证明运行时不只会生成文档，而能把 Decision、Assumption、Evidence、Experiment、Human Gate 和 rollback 串成可验证闭环。

在仓库根目录运行：

```bash
python scripts/create_golden_project.py --destination ../gamedesignos-golden-lighthouse
```

脚本只创建一个全新的 `public-synthetic` workspace；目标目录非空时会拒绝覆盖。完成后会自动执行 workspace validation。

黄金案例明确不证明真实留存、商业需求或发行表现。它只验证产品工作流、契约和安全门能够闭环运行。
