### try-finally 대신 try-with-resouces

Try-finally

- Finally는 마지막에 동작한다

```java
try {
    sout("1");
    throw new Exception();
}finally {
    sout("3");
}
```

Exception시 Stack trace에 어려움이 있음

```java
static void copy(String src, String dst) throws IOException {
    InputStream in = new FileInputStream(src);
    try {
        OutputStream out = new FileOutputStream(src);
        try {
            byte[] buf = new byte[100];
            int n;
            while((n = in.read(buf)) >= 0) {
                out.write(buf, 0, n);
            }
        } finally {
            out.close(); // 
        }
    } finally {
        in.close(); //
    }
}
```



Try-with-resources

``` java
public class Resource implements AutoCloseable {
    @Override
    public void close() throws Exception {
        throw new Exception("inside Resource exception");
    }
}

try (Resource r1 = new Resource();
     Resource r2 = new Resource();) {
     throw new Exception("asd");
}
```



Cleaner with Try-with-resources

```java
public class CleanObject implements AutoCloseable {
    private static final Cleaner clenaer = Cleaner.create();
    private static class CleanData implements Runnalbe {
        @Override
        public void run() {
            // clean
        }
    }
    private final CleanData cleanData;
    private final Cleaner.Cleanable cleanable;
    public CleanObject() {
        this.cleanData = new CleanData();
        this.cleanable = cleaner.register(this, cleanData);
    }
    @Override
    public void close() {
        cleanable.clean();
    }
}
```

Clean이 실패해서 GC의 기회가 없어져도 AutoCloseable을 통해 이를 보완

Connection이 닫혀야 할 상황에서 사용하자!