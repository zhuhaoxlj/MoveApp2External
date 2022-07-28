# MacOS 软件移动到外置硬盘

> 由于苹果电脑的固态硬盘性价比太低了（好吧是我太穷了），所以我购买的是256G M1 Macmini（没有屏幕、键盘更便宜了，是真的香啊）搭配三星970 evo plus，搭配雷电3硬盘盒，完全可以平替系统自带的固态。

![image-20220728141752091](https://markgosling.oss-cn-beijing.aliyuncs.com/img/202207281417196.png)

外接硬盘的写入速率甚至比自带的固态还要快，所以说视频剪辑也是可以胜任的。

![image-20220728142137662](https://markgosling.oss-cn-beijing.aliyuncs.com/img/202207281421705.png)

## MoveApp2External

> 本项目通过python脚本，一键化将系统自带的软件移动到外置硬盘中，并建立软连接，使移动后的软件可以正常使用（适用于pkg、dmg），启动台中也是可以找到对应软件的，像AE，PhotoShop这种有一整个软件包的也是可以迁移的。

1.下载并解压脚本

2.环境准备

> 确保电脑网络畅通，电脑已经装好python

3.双击move_app_start.sh脚本即可打开工具

![image-20220728142541046](https://markgosling.oss-cn-beijing.aliyuncs.com/img/202207281425098.png)

4.如果遇到什么问题欢迎点击issue进行反馈