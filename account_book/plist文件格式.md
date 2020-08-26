## plist文件科普

* plist (Property list) 是IOS下一种存储序列化对象的文件格式，格式有2种: XML格式 和 二进制格式(bplist, Binary Plist). 文件头标识为`bplist`。

* plist二进制转xml格式可以使用plist Editor编辑器，或apple官方的`plutil.exe`工具。

* 在IOS下通常用`NSKeyedArchiver`和`NSKeyedUnarchiver`两个类来对数据进行归档（序列化/编码）和解档（反序列化/解码），python的bpylist2库即是实现的这两个类的功能。

## Python [bpylist2](https://github.com/Marketcircle/bpylist) 库

### 实现对bplist文件的解析

bpylist库可以对bplist文件进行解析，得到一个字典格式的数据。我最开始也是使用这种方式将plist文件解档，但是分析后发现存在部分数据不全的情况。我通过写脚本和手工的方式将这些数据进行了统计，结果很惊人：有75%的数据存在“不完整”的情况。

![image](F3BD17081BA346DDBD7F5F1761FFE82A)

这里的“不完整”是不是指数据缺失，而是指数据很凌乱。有部分账单要么没有金额，要么没有名称。我猜测是数据进行了压缩，对重复的常量数据只保存指针而不保存值。对此我进行了统计，果然，有金额的这部分账单中，金额的值都是唯一的，不存在重复项。

验证了这个猜测后，我查阅了一些资料，得知是bplist文件将数据的存储空间进行了优化。

### 归档和解档

Python bpylist库可以实现对数据的归档和解档，包括基本类型和自定类对象等。

对基本类型的归档和解档，如string、int、long、dict等，可以直接用archiver.archive()和archiver.unarchive()两个函数。
```
from bpylist import archiver

with open('my_archived_object', 'rb') as f:
    archiver.unarchive(f.read())  //解档

my_object = { 'foo':'bar', 'some_array': [1,2,3,4] }
archiver.archive(my_object)  //归档
```
但是对于自定义类，则需要自己定义编码和解码函数。

一个Demo，将FooArchive对象序列化后写入test.plist文件中。
```
from bpylist import archiver
from bpylist.archive_types import timestamp

class FooArchive:

    def __init__(self, title, stamp, count, cats, meta, empty, recursive):
        self.title = title
        self.stamp = stamp
        self.count = count
        self.categories = cats
        self.metadata = meta
        self.empty = empty
        self.recursive = recursive

    @staticmethod
    def encode_archive(obj, archive):
        archive.encode('title', obj.title)
        archive.encode('stamp', obj.stamp)
        archive.encode('count', obj.count)
        archive.encode('categories', obj.categories)
        archive.encode('metadata', obj.metadata)
        archive.encode('empty', obj.empty)
        archive.encode('recurse', obj.recursive)

    @staticmethod
    def decode_archive(archive):
        title = archive.decode('title')
        stamp = archive.decode('stamp')
        count = archive.decode('count')
        cats = archive.decode('categories')
        meta = archive.decode('metadata')
        empty = archive.decode('empty')
        recurse = archive.decode('recursive')
        return FooArchive(title, stamp, count, cats, meta, empty, recurse)

## 注册类
archiver.update_class_map({'crap.Foo': FooArchive}) //crap.Foo为FooArchive类在plist文件中对应的名称。

FooArchive('herp', timestamp(9001), 42,
                     ['strawberries', 'dragonfruit'],
                     {'key': 'value'},
                     False,
                     None)
with open('test.plist', 'wb') as f:
    f.write(archiver.archive(obj)) //写入序列化对象
```

用plist Editor打开test.plist:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>$archiver</key>
	<string>NSKeyedArchiver</string>
	<key>$objects</key>
	<array>
		<string>$null</string>
		<dict>                       //声明属性类型
			<key>$class</key>
			<dict>
				<key>CF$UID</key>
				<integer>2</integer>
			</dict>
			<key>categories</key>
			<dict>
				<key>CF$UID</key>
				<integer>6</integer>
			</dict>
			<key>count</key>
			<integer>42</integer>  //int类型的属性值跟在后面
			<key>empty</key>
			<false/>               //bool类型的属性值跟在后面
			<key>metadata</key>
			<dict>
				<key>CF$UID</key>
				<integer>10</integer>
			</dict>
			<key>recurse</key>
			<dict>
				<key>CF$UID</key>
				<integer>0</integer>
			</dict>
			<key>stamp</key>
			<dict>
				<key>CF$UID</key>
				<integer>4</integer>
			</dict>
			<key>title</key>
			<dict>
				<key>CF$UID</key>
				<integer>3</integer>
			</dict>
		</dict>
		<dict>
			<key>$classes</key>
			<array>
				<string>crap.Foo</string>
			</array>
			<key>$classname</key>
			<string>crap.Foo</string>
		</dict>
		<string>herp</string>     //字符串、字典等类型的属性值另外补充
		<dict>
			<key>$class</key>
			<dict>
				<key>CF$UID</key>
				<integer>5</integer>
			</dict>
			<key>NS.time</key>
			<real>-978298199</real>
		</dict>
		<dict>
			<key>$classes</key>
			<array>
				<string>NSDate</string>
			</array>
			<key>$classname</key>
			<string>NSDate</string>
		</dict>
		<dict>
			<key>$class</key>
			<dict>
				<key>CF$UID</key>
				<integer>7</integer>
			</dict>
			<key>NS.objects</key>
			<array>
				<dict>
					<key>CF$UID</key>
					<integer>8</integer>
				</dict>
				<dict>
					<key>CF$UID</key>
					<integer>9</integer>
				</dict>
			</array>
		</dict>
		<dict>
			<key>$classes</key>
			<array>
				<string>NSArray</string>
			</array>
			<key>$classname</key>
			<string>NSArray</string>
		</dict>
		<string>strawberries</string>
		<string>dragonfruit</string>
		<dict>
			<key>$class</key>
			<dict>
				<key>CF$UID</key>
				<integer>11</integer>
			</dict>
			<key>NS.keys</key>
			<array>
				<dict>
					<key>CF$UID</key>
					<integer>12</integer>
				</dict>
			</array>
			<key>NS.objects</key>
			<array>
				<dict>
					<key>CF$UID</key>
					<integer>13</integer>
				</dict>
			</array>
		</dict>
		<dict>
			<key>$classes</key>
			<array>
				<string>NSDictionary</string>
			</array>
			<key>$classname</key>
			<string>NSDictionary</string>
		</dict>
		<string>key</string>
		<string>value</string>
	</array>
	<key>$top</key>
	<dict>
		<key>root</key>
		<dict>
			<key>CF$UID</key>
			<integer>1</integer>
		</dict>
	</dict>
	<key>$version</key>
	<integer>100000</integer>
</dict>
</plist>
```
## 参考链接
* https://github.com/Marketcircle/bpylist
* http://devonios.com/ios-data-keyedarchiver.html
* https://www.shellcodes.org/Hacking/%E6%8F%AD%E7%A7%98Safari%E5%AF%86%E7%A0%81%E5%AD%98%E5%82%A8%E7%9A%84%E7%A7%98%E5%AF%86.html
* [Plist 文件详解 （一）](https://blog.csdn.net/u012839224/article/details/42770085/)