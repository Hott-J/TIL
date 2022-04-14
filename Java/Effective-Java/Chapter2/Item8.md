### finalizer, cleaner를 피하라

Finalizer (deprecated at java9)

```java
public class Item8 {
    @Override
    public void finalize(){
        sout("call finalize");
    }
}

public class MainApplication {
    private void run(){
        Item8 item8 = new Item8();
    }
    public static void main(String[] args) {
        MainApplication mainApplication = new MainApplication();
        mainApplication.run();
    }
}
```



System.gc()의 내부

```java
// Indicate to the virtual machine that it would be a good time to collect available memory. Note that, this is a hint only.

public static void gc() {
    RUNTIME.gc();
}
```



언제 써야 할 까 (안정망)

- 안전장치로 이중 체크

```java
public class Item8 {
    private boolean closed;
    public void close() throws Exception {
        // 객체 닫는다
    }
    @Override
    public void finalize() throws Throwable {
        if(!this.closed){
            close();
        }
    }
}
```

닫히지 않았을 수도 있으므로, 한번 더 닫음



특수한 상황이 아니라면 사용하지 않는 것을 추천

안정망 역할로 아주 제한적으로 사용 가능