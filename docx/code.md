---
export_on_save:
  pandoc: true
---
# 软件源程序

@import "../app.py"

# 软件源程序

- 项目中的 Dash 应用。

@import "../app.py"

- 项目中的 Dash 应用运行主程序。

@import "../run.py"

## 网页应用的主题

网页应用的 `app` CSS 主题。

```css
.app-button {
    list-style-type: none;
    margin: 0;
    padding: 0;
    display: inline;
    
}

.app-button a {
    text-decoration-line: none;
}
```

网页应用的页面主题。

```css
body {
    font-family: cursive;
}

h1 {
    color: hotpink
}
```

## 网页应用的布局 `layouts/`

网页应用的主页布局。

@import "../layouts/index.py"

网页应用的 `about` 布局。

@import "../layouts/about.py"

网页应用的 `record` 布局。

@import "../layouts/record.py"

网页应用的 `replay` 布局。

@import "../layouts/replay.py"

网页应用的 `watch` 布局。

@import "../layouts/watch.py"

## 网页应用的布局参数 `options/`

网页应用的主页布局参数。

@import "../options/index.toml"

网页应用的 `about` 布局参数。

@import "../options/about.toml"

网页应用的 `record` 布局参数。

@import "../options/record.toml"

网页应用的 `replay` 布局参数。

@import "../options/replay.toml"

网页应用的 `watch` 布局参数。

@import "../options/watch.toml"

## 网页应用的回调 `callbacks/`

网页应用的 `record` 回调。

@import "../callbacks/record.py"

网页应用的 `replay` 回调。

@import "../callbacks/replay.py"

网页应用的 `watch` 回调。

@import "../callbacks/watch.py"

## 鸟瞰图

网页应用的鸟瞰图 `view` 回调。

@import "../apps/view.py"

## 工具

- 网页应用的鸟瞰图的 `shape` 框架。

@import "../tools/frame.py"

- 定义障碍物枚举类：

@import "../tools/obstacle/info.py"

- 定义障碍物 INFO：

@import "../tools/obstacle/loader.py"

- 为了方便使用，提供仿真环境：

@import "../tools/obstacle/simulate.py"
