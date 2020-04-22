# TCB Code

##First Code Project

### 1.fake webhook 模拟器 (参数可以自己输入，需要支持3种以上bot的webhook格式)

- 支持 Cyber, Tks, Balko 等主流bot的 webhook 格式(在程序中可以自主选择最好，可以使用input()来实现)
- 支持自己输入webhook信息，如单品标题，尺码，profile名称，标题图片等信息
- 支持自定义webhook link
- 支持自定义 webhook发送的author名字以及author avatar(头像)

###2.shopify单品监控
简单shopify 监控器(指定网站及单品，如undefeated.com,不需要通用，单品补货监控即可)

- 支持如undefeated网站的单品尺码监控，即当监控的单品更新尺码时，发送提醒到自定义的webhook
- 支持自定义webhook
- 做好错误处理，需要能够长期运行
- 附加题 实现undfeated的上新监控

####hint:

- 对于一个单品 如 https://undefeated.com/collections/all/products/nike-x-undefeated-air-max-90-pacificblue-vividpurple 可以在后面加.json获取一个json的页面(shopify特性)
- https://undefeated.com/products.json 可以看到一个shopify站的所有商品（某些站会关闭，但本project只要实现未关闭的站即可)

###3. footlocker eu 账号激活器
跑过大象的都知道，之前yeezy 350有一次发售，需要强制账号才能加车
用大象注册时，会给你的邮箱发送一封 verify 邮件
本项目要求:

- 输入为一个verify邮件中的激活链接的列表（提取方式有很多，可以读取你的email，也可以通过页面的正则等)
- 自行研究ftl eu的账号激活流程
- 利用程序实现，并将激活的结果进行输出

####hint:
- ftl eu的激活就是对链接进行访问，但需要带上一些headers等信息，否则会失败
- 成功与否需要对返回的html进行解析，具体字段请自行实验

###4.一个可以自动gen resi proxy 并且分给不同bot的proxy脚本
- 以smart为例，如果你用过oxy geo 或者netnut，请自行扩展，不要求支持多家proxy，但能支持是附加分
- 自行获取smart的地区列表
- 输入为 你想要的地区（可能是一个地区列表），你想要使用的bot(一个bot列表), 以及每个bot想要多少条proxy
- 输出直接是当前目录下的文件，为 bot名字开头的txt文件，分别代表给每个bot生成的 proxy 列表

####hint:
- smart的地区列表请自行到smart官网注册账号查看(或者到resi game 的dc server中查看)
- 请自行研究smart proxy的resi generate规则并写成程序
- 请使用 random 这个模块


###5. 简单的proxy筛选脚本(支持保存延迟在预设值以下的proxy列表，测试最好能实现多测几次取平均值的逻辑)
- 通过对google的request测试来测试proxy连通性（ 如果你想支持别的网站，可以作为附加项）
- 利用requests 模块实现
- 每条proxy，最好测试多次取其平均值，因为网络有其不稳定性
- 输入为一个proxy列表的txt
- 输出为一个筛选过可以达到程序设置要求的proxy列表（延迟小于 xxx ms)
- 要求在console输出每条proxy的延迟结果

####hint:
- requests 的 proxy使用，需要https和http proxy都设置才会生效，并且格式不一样
- 运行该脚本不要再你的本地运行, 需要去服务器或者国外的local
- 延迟设定要根据你的网络情况来决定