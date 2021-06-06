# 部署注意事项

## config.h

### /* appearance */

字体设置

```C
static const char *fonts[]          = { 
  "monospace:size=12",
  "WenQuanYi Micro Hei:size=12",
};
static const char dmenufont[]       = "monospace:size=10";
```

### /* commands */

脚本设置

```C

```

## config.mk

X11路径

```C
X11INC = /usr/include/X11
X11LIB = /usr/lib/X11
```

