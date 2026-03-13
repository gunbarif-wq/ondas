[app]

# App name
title = 온다스
package.name = ondas
package.domain = org.ondas

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf

version = 0.1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android specific
android.permissions = INTERNET
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

