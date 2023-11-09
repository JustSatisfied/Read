

Formily中的reactive模块的作用是独立于UI的一个响应式编程库

这块的核心实现跟Vue的核心响应模块有很多代码重合的部分

入口代码是通过obeservable，这个函数的作用就是把我们需要被代理的对象进行一层 可观察对象, 通过原生的Proxy

函数createObservable 

通过WeakMap创造的几个个弱引用对象(为了防止因为闭包造成的内存泄露问题)-ProxyRaw还有RawShallowProxy

1.必须是一个对象如果不是直接返回不会进行代理包装

2.判断该对象是否被代理过，如果代理过直接返回被包装的函数

 

