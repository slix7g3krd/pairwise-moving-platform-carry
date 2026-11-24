# pairwise-moving-platform-carry

## 领域

游戏、图形与多媒体

## 主题

移动平台载人与相对位移

## 说明

平台位移入物理步、父节点同帧切换与销毁解绑。

初始状态下 `gameplay/moving_platform_carry.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
