# html开篇

**tag**: #web/html

## 标签

| 功能                |                代码                 |
| ------------------- |:-----------------------------------:|
| <b>加粗</b>         |   `<strong></strong>`, `<b></b>`    |
| <em>倾斜</em>       |       `<em></em>`, `<i></i>`        |
| <del>删除线</del>   |      `<del></del>`, `<s></s>`       |
| <ins>下划线</ins>   |      `<ins></ins>`, `<u></u>`       |
| <div>万能标签</div> |   `<div></div>`, `<span></span>`    |
| 注释标签            | `<!--这里是注释-->`, 快捷键`ctrl+/` | 

### 超链接
anchor 的缩写
```html
<a href='跳转目标' target="_self/_blank"> 文本或图像 </a>
<a href=./1-html-02.md target="_self"> 文本或图像 </a>
```
<a href=./1-html-02.md target="_blank"> <img src="images\MacType.ico" alt="这是图片的替换文字" title="鼠标放上后的提示语" border=5px/> </a>

#### 锚点链接

快速定位到本页面的某个位置。

```html
<a href='#自己加的标识'>介绍</a>
<a href='#02'>第二章</a>
<a href='#021'>第二章内容</a>

<h4 id='02'> 这段话是第二章标题 </h4>
<p id='021'> 这段话是第二章内容 </p>
```

> <a href='#021'>第二章内容</a>
> <p id='021'> 这段话是第二章内容 </p>

## 单标签

| 功能 |           代码           |
| ---- |:------------------------:|
| 图像 | `<img src="/111.png" />` |
| 换行 |         `<br />`         |

### 图像标签参数

```html
<img src="../2021-4-26 11-29-46.png" alt="这是图片的替换文字" title="鼠标放上后的提示语" width=240 height=360 border=5px/> 
```

<img src="images\MacType.ico" alt="这是图片的替换文字" title="鼠标放上后的提示语" width="25px" height=25px border=5px/>

![2021-4-26 11-29-46](2021-4-26%2011-29-46.png)

## 表格标签

```html
 <table border="2" cellpadding="20" cellspacing="5" width="500px">
 <thead>
 	<!-- <tr></tr> 为一个行的数据 -->
 	<tr align="center"> <!-- <th> 表头标签-->
		<th>name</th> <th>age</th> <th>score</th>
	</tr>
 </thead>
 <tbody>
 	<tr>
 		<td align="right">tom</td> <td align="center">32</td> <td>89</td>
 	</tr>
 </tbody>
 </table>
```

### 单元格合并

```html

```