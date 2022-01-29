# 使用方法
* 进入项目根目录

`
cd jump-helper
`
* 安装pipenv工具并下载项目依赖

`
pip install pipenv & pipenv install
`
* 根据自己的手机尺寸更改项目根目录下的config.py，其中`w`和`h`表示你的手机物理像素下的分辨率，分辨率可通过手机截屏查看截屏图片尺寸知晓。
    * `SIZE`：更改为自己手机的分辨率，格式为(`w`, `h`)。
    * `MIN_AREA`：该值表示跳跃平台的最小面积，建议设为`w * h * 0.001085`, 适当调小该值可以增强识别准确度，但太小则小几率将其它色块识别为目标平台。
    * `COEFFICIENT`: 按压系数，该系数会乘以距离得出跳跃所需按住屏幕的时间（ms），需通过多次运行本程序调节出最适合你手机分辨率的大小，跳跃如果越过了目标平台则调小该值，反之调大该值，建议每次调节幅度为`0.2`。
* 建议自行手机截屏跳一跳页面，裁剪出老虎的图片替换assets文件夹下的老虎模板图片。
* USB连接手机电脑，并在手机端开启USB调试。
* 本程序需要手动操作，默认开启了debug模式。运行后当终端输出提示等待屏幕截图时，按下enter键开始截图并进行图像识别，随后会弹出识别结果，如果识别结果无误再次按下enter键会执行跳跃操作。



# tips: 
* config.py中的配置参数基于1440 * 3200尺寸配置，请根据自己手机分辨率参照使用方法配置。
* 多次准确命中目标平台中心可能受到反作弊处理。
* 本程序仅供学习娱乐，毕竟资本家可不蠢🙄。