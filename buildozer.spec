[app]

# 包名（唯一标识，用域名倒写）
package.name = myapp
package.domain = com.example

# App 显示在手机上的标题
title = 我的第一个App

# 版本号
version.code = 1
version.string = 1.0.0

# 入口 Python 文件
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 构建要求
requirements = python3,kivy

# 权限（Android）
android.permissions = INTERNET

# 屏幕方向（portrait=竖屏, landscape=横屏, sensor=自动旋转）
orientation = portrait

# 应用图标（留空使用默认）
# icon = icon.png

# 支持的架构
android.archs = arm64-v8a,armeabi-v7a

[buildozer]

# 编译日志级别
log_level = 2

# 是否在 root 用户下运行时发出警告（0=不警告，1=警告）
warn_on_root = 1
