# simpleDjango3-adminLTE
django3结合adminLTE3前端模板的简单实例。

## 方法一：
使用 [django-adminlte3](https://github.com/d-demirci/django-adminlte3)来结合使用  
该插件的adminlte3说明书打不开了,只能开2的文档 
文档 [django-adminlte2](https://django-adminlte2.readthedocs.io/en/latest/quickstart.htm)
```text
优点 ：
    支持pip直接安装，开包直接使用
    有使用文档
缺点：
    用了它，以后想换前端框架是不可能了；
    该插件的adminlte3说明书打不开了；
    模板继承不够直观，能看疯了。
```

## 方法二：
使用 [django-adminlte-ui](https://github.com/wuyue92tree/django-adminlte-ui)来结合使用  
文档[django-adminlte-ui 文档](https://django-adminlte-ui.readthedocs.io/en/latest/)
```text
优点 ：
    支持pip直接安装，开包直接使用
    有使用文档，有中英双语
    中国人开发的
缺点：
    用了它，以后想换前端框架是不可能了；
    adminlte封装的版本是 2.3.6，并不是最新的了。
```

## 方法三：
直接使用原生[adminlte](https://github.com/ColorlibHQ/AdminLTE/releases)来结合django使用  
本例子，使用的是此法。
使用的是 AdminLTE 3.0.2
```text
优点 ：
    adminlte 版本你想要多新就多新
    前端框架可换，耦合度不会那么高
缺点：
    不能支持pip直接安装，只能将它拆解放到django的templates和static里；
    需要自行修改引用路径；
```

# 快速替换引用路径

![Image text](https://raw.githubusercontent.com/DeSireFire/simpleDjango3-adminLTE/master/way.png)

# 部署成果的效果
demo  
![Image text](https://raw.githubusercontent.com/DeSireFire/simpleDjango3-adminLTE/master/demo.gif)

# Thanks
AdminLTE
django
django-adminlte-ui
django-adminlte3