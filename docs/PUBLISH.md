# 公开版维护说明

公开仓库：https://github.com/Northwind-Tomato-Wang/distributed-corporate-risk-research

这是从研究目录中单独整理的公开版。原始项目、数据和内部归档不在这个Git仓库里。

更新时，只在本公开版目录中检查和提交文件：

```bash
git status
git diff
git add <需要更新的文件>
git commit -m "Describe the update"
git push
```

不要在原始研究根目录执行git add或上传全部文件。不要将CSMAR表、企业级缓存、通报全文、权重、商业字体、申报书或私人联系方式补入仓库。

本包可以核对汇总和重画图；历史代码快照保留供阅读，不是已封装的完整训练依赖。完整训练复现、软件授权和真实单位接入需要另行推进。
