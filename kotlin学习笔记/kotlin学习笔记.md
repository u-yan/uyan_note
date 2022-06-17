# [kotlin](https://try.kotl.in/)
[在线练习kotlindemo](https://play.kotlinlang.org/#eyJ2ZXJzaW9uIjoiMS43LjAiLCJwbGF0Zm9ybSI6ImphdmEiLCJhcmdzIjoiIiwibm9uZU1hcmtlcnMiOnRydWUsInRoZW1lIjoiaWRlYSIsImNvZGUiOiIvKipcbiAqIFlvdSBjYW4gZWRpdCwgcnVuLCBhbmQgc2hhcmUgdGhpcyBjb2RlLlxuICogcGxheS5rb3RsaW5sYW5nLm9yZ1xuICovXG5mdW4gbWFpbigpIHtcbiAgICBwcmludGxuKFwiSGVsbG8sIHdvcmxkISEhXCIpXG59In0=)

## 类和属性
```
class Person(
    val name: String,        // 1 只读属性生成和琐碎获取器
    var isMarried: Boolean   // 2 可写属性：一个字段，一个获取函数和一个设置函数
)
```
`val`是只读的，`var`是可写的

## 注解
### @JvmOverloads
合并成一个构造函数，
Instructs the Kotlin compiler to generate overloads for this function that substitute default parameter values.
If a method has N parameters and M of which have default values, M overloads are generated: the first one takes N-1 parameters (all but the last one that takes a default value), the second takes N-2 parameters, and so on.
### 记录常用的问题

1. system out 直接`println("xxx")`
2. 类继承
```kotlin
class TitleLayout  (context: Context, attrs: AttributionSource): LinearLayout(context) {
    init {
        
    }
}
```

