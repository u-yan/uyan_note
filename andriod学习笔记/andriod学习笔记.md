# 1. 布局


这是一个项目简单框架，然后在```main```里的kt代码文件内容就是如下

```kotlin
package com.example.demo

import android.support.v7.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {
//    override fun onCreate(savedInstanceState: Bundle?) {
//        super.onCreate(savedInstanceState)
//        setContentView(R.layout.demolayout)
//    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)//内容即是~/项目目录/app/src/main/res/layout/里面xml里文件的名称
    }
}
```

可以调用

``````kotlin
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.名称)//内容即是~/项目目录/app/src/main/res/layout/里面xml里文件的名称
    }
``````

来选择自己想要的布局。

## 1.1 [textview](https://developer.android.com/reference/android/widget/TextView?hl=en)

```xml
    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/textview"
        android:textColor="#33691E"
        tools:layout_editor_absoluteX="16dp"
        tools:layout_editor_absoluteY="100dp"
        />
```

`android:id`是唯一表示的组件id，`android:layout_width，android:layout_height`是长宽的设置，`android:text`文本的设置，其中值`“@string/textview"`代表了<img src="/Users/dongxin05/Library/Application Support/typora-user-images/截屏2022-05-26 上午11.25.55.png" alt="截屏2022-05-26 上午11.25.55" style="zoom:70%;" />文件目录下`main/res/values`中`string`里面`textview`值。

## 1.2 [ImageView](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams)

首先遇到的一个问题是，在`main/layout/demo.xml`中简单添加了`imageView`	组件，但是却没有任何显示，然后发现一个属性`android:src="@drawable/my_image"`跟据上面`“@string/textview"`寻找值的经验，那么就把图片直接放入![截屏2022-05-26 上午11.54.56](/Users/dongxin05/Library/Application Support/typora-user-images/截屏2022-05-26 上午11.54.56.png)`drawable`目录里面，然后直接赋值`android:src="@drawable/background"`即可。

```xml
<ImageView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:src="@drawable/background"
    android:contentDescription="@string/text"
    />
```

发现问题是imageview不能全屏，那么是`android:layout_width` 和`android:layout_height`这两个设置的问题，然后查阅[android手册](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams)得

| Constant     | Value    | Description                                                  |
| :----------- | :------- | :----------------------------------------------------------- |
| fill_parent  | ffffffff | The view should be as big as its parent (minus padding). This constant is deprecated starting from API Level 8 and is replaced by `match_parent`. |
| match_parent | ffffffff | The view should be as big as its parent (minus padding). Introduced in API Level 8. |
| wrap_content | fffffffe | The view should be only big enough to enclose its content (plus padding). |

所以修改成`fill_parent`即可。

## 1.3 Button

## 1.4 [EditText](https://developer.android.com/reference/android/widget/EditText?hl=en)

```xml
<EditText
    android:id="@+id/plain_text_input"
    android:layout_height="50dp"
    android:layout_width="100dp"
    android:inputType="text"
    android:hint="请输入密码"/>
```

最需要注意的就是要固定`layout_height`和`layout_width`，这里自己尝试了一下就直接取值了，这样是一个输入框，并且密码的话，可以加入`hint`而不是`text`，`text`会被删掉。

## 1.5 [CheckBox](https://developer.android.com/guide/topics/ui/controls/checkbox?hl=zh-cn)

```xml
<CheckBox android:id="@+id/checkbox2"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@string/checkbox2"
    android:onClick="onCheckboxClicked"/>
```

`android:onClick`是新出现可方法，应在相应的`activity`中声明，所以在`main.kt`中加入

```kotlin
class MainActivity : AppCompatActivity() {
    fun onCheckboxClicked(view: View) {//相应的加入的函数，名称要和xml对应
        if (view is CheckBox) {
            val checked: Boolean = view.isChecked
            when (view.id) {
                R.id.checkbox1 -> {
                    if (checked) {//更改后可以得知状况
                        println("clicked")
                    } else {
                        println("noclicked")
                    }
                }
            }
        }
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.demolayout)
    }
}
```

## 1.6 ProgressBar

分成两种`ProgressBar`，一种是`Indeterminate Progress`，另一种是`Determinate Progress`







# 2. RecyclerView

# 3. [Activity](https://developer.android.com/guide/components/activities/activity-lifecycle)

## 3.1 [intent](https://developer.android.com/reference/android/content/Intent)

`Intent` 是在相互独立的组件（如两个 activity）之间提供运行时绑定功能的对象。他也可以在广播，服务之间进行通信



##

3.1 onCreat()

# XML
## 什么是xmlns 
其实`xmlns`是`XMLnamespace`


# 运行
1. 在



