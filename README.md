# 说明
这是一个[jyy老师](https://jyywiki.cn/)网站的本地镜像，方便离线浏览课件和代码示例。

# 步骤
可以通过下面的步骤在网页中唤起nvim/cLion/vscode等等文本编辑器或者IDE（和老师视频中演示的那样）

已经测试过：`nvim`，`clion`，`vscode`

如果只是浏览课件，并不需要唤醒IDE，那么只需要在打开Courseware文件夹下的index.html即可，下面的步骤可以忽略。

1. 环境变量

Windows下要把IDE或者文本编辑器路径放置在环境变量中，并修改`server.py`中的
```python
""" 调用 文本编辑器或IDE 打开文件夹 """
IDE = "code"
subprocess.run([f"{IDE}", full], check=True)
```
中的`code`为对应你要在网页中点击唤起的IDE或文本编辑器（code对应vscode）

2. 环境搭建
```pip
pip install -r requirements.txt
```

3. 执行

windows或者WSL下执行`python3 server.py`

windows下执行脚本，在浏览器访问下面网址时，点击会唤起windows下的IDE

WSL下执行脚本，也可以在windows浏览器访问下面网址，但点击会唤起WSL下的IDE

4. 浏览器输入`http://127.0.0.1:8001/index.html`

=========================================================================================================================
# 本周更新内容如下：  
1. **进程管理基础概念**  
   - 新增进程定义及特征说明，明确进程作为程序执行实体的动态性、并发性、独立性等核心属性。  
   - 引入进程状态模型，涵盖运行态、就绪态、阻塞态及其转换条件，并扩展状态转换图示例（如新增超时阻塞到就绪的触发机制）。  
   - 补充进程控制块（PCB）的详细结构，包括进程标识符、程序计数器、寄存器状态、内存分配表、优先级等字段的功能解释。  

2. **进程调度算法扩展**  
   - 更新先来先服务（FCFS）调度算法的优缺点分析，增加吞吐量与响应时间矛盾的实例说明。  
   - 新增短作业优先（SJF）算法的抢占式与非抢占式变体对比，强调平均等待时间优化效果及长作业“饥饿”问题。  
   - 补充时间片轮转（RR）算法的动态时间片调整策略，讨论时间片长度对上下文切换开销的影响。  

3. **同步与互斥机制深化**  
   - 细化临界区问题的三个核心条件（互斥、前进、有限等待），新增基于忙等待的软件解决方案（如Dekker算法）伪代码分析。  
   - 引入信号量（Semaphore）的底层实现原理，包括原子操作P()/V()的计数器与等待队列管理逻辑。  
   - 扩展经典同步问题案例，新增“读者-写者问题”的写者优先变体解决方案，对比读者优先模式的资源分配差异。  

4. **内存管理进阶内容**  
   - 更新地址绑定过程，明确编译时、加载时、运行时三种绑定阶段的适用场景与灵活性差异。  
   - 新增动态分区分配算法的详细对比，包括首次适应（First Fit）、最佳适应（Best Fit）、最坏适应（Worst Fit）的内存碎片率与分配效率分析。  
   - 补充分页机制中页表结构的多级设计（如二级页表），解释其如何通过减少连续内存占用解决大地址空间映射问题。  

5. **虚拟内存基础引入**  
   - 定义虚拟内存的核心目标（逻辑内存扩展与物理内存抽象），对比覆盖技术的局限性。  
   - 新增请求调页（Demand Paging）流程说明，涵盖缺页中断处理、页面置换策略触发条件及开销组成。  
   - 初步引入页面置换算法分类（如FIFO、OPT、LRU），概述其基本思想与未来课程关联性。  

6. **文件系统架构更新**  
   - 新增文件控制块（FCB）与目录结构的关联设计，解释硬链接与符号链接在FCB引用计数上的差异。  
   - 补充文件分配方法（连续、链表、索引）的碎片与随机访问性能对比，重点分析索引分配的多级块表扩展机制。  
   - 扩展文件系统层次模型（用户接口、逻辑文件系统、文件组织模块、存储设备驱动），明确各层职责与交互流程。  

7. **I/O系统管理优化**  
   - 更新I/O控制方式分类，新增DMA（直接内存访问）传输过程图示及通道控制器的并行处理优势。  
   - 引入缓冲技术的多级设计（单缓冲、双缓冲、循环缓冲），分析其对设备速度差异的平滑作用。  
   - 补充设备分配安全性策略，包括死锁预防中的线性请求顺序约束与资源预声明机制。  

本次内容聚焦进程调度、内存管理及I/O子系统的理论深化，强化算法设计与硬件协同的核心逻辑，为后续实践环节奠定基础。
=========================================================================================================================

# TODO
- [ ] 收集缺失的文件

```markdown
https://jyywiki.cn/pages/OS/img/GET-square.jpg (from https://jyywiki.cn/OI/linear-algebra.slides.html)
https://jyywiki.cn/OS/2024/slides/img/visicalc.webp (from https://jyywiki.cn/OS/2024/slides/1.3.html)
https://jyywiki.cn/OS/2024/slides/img/just-for-fun.webp (from https://jyywiki.cn/OS/2024/slides/1.4.html)
https://jyywiki.cn/OS/2024/slides/img/sc.webp (from https://jyywiki.cn/OS/2024/slides/5.4.html)
https://jyywiki.cn/OS/2024/slides/img/wmo.webp (from https://jyywiki.cn/OS/2024/slides/5.4.html)
https://jyywiki.cn/OS/2024/slides/img/the-world.webp (from https://jyywiki.cn/OS/2024/slides/6.1.html)
https://jyywiki.cn/OS/2024/slides/img/homura.webp (from https://jyywiki.cn/OS/2024/slides/6.1.html)
https://jyywiki.cn/OS/2024/slides/img/cyber-human.webp (from https://jyywiki.cn/OS/2024/slides/6.2.html)
https://jyywiki.cn/OS/2024/slides/img/first-bug.webp (from https://jyywiki.cn/OS/2024/slides/8.1.html)
https://jyywiki.cn/OS/2024/slides/img/orchestra.webp (from https://jyywiki.cn/OS/2024/slides/9.1.html)
https://jyywiki.cn/OS/2024/slides/img/locker.webp (from https://jyywiki.cn/OS/2024/slides/10.1.html)
https://jyywiki.cn/OS/2024/slides/img/locker-2.webp (from https://jyywiki.cn/OS/2024/slides/10.1.html)
https://jyywiki.cn/OS/img/dgx-1.webp (from https://jyywiki.cn/OS/2024/slides/11.4.html)
https://jyywiki.cn/OS/2024/slides/img/get.webp (from https://jyywiki.cn/OS/2024/slides/13.4.html)
https://jyywiki.cn/OS/2024/slides/img/linux-onion.webp (from https://jyywiki.cn/OS/2024/slides/17.1.html)
https://jyywiki.cn/OS/2024/slides/img/linker.webp (from https://jyywiki.cn/OS/2024/slides/19.2.html)
https://jyywiki.cn/OS/2024/slides/img/PATHCOV.webp (from https://jyywiki.cn/OS/2024/slides/23.3.html)
https://jyywiki.cn/OS/2024/slides/img/8088-mb.webp (from https://jyywiki.cn/OS/2024/slides/26.1.html)
https://jyywiki.cn/OS/img/FAT-number.webp (from https://jyywiki.cn/OS/2024/slides/28.3.html)
https://jyywiki.cn/OS/img/FAT-dent.webp (from https://jyywiki.cn/OS/2024/slides/28.3.html)
https://jyywiki.cn/OS/2024/slides/img/rosetta-stone.webp (from https://jyywiki.cn/OS/2024/slides/29.1.html)
https://jyywiki.cn/OS/2024/slides/img/silica-talk.webp (from https://jyywiki.cn/OS/2024/slides/29.1.html)
https://jyywiki.cn/OS/2024/slides/img/dian-nao.webp (from https://jyywiki.cn/OS/2024/slides/29.1.html)
https://jyywiki.cn/pages/OS/img/logo-text-white.svg (from https://jyywiki.cn/pages/OS/img/sel4-logo.svg)
https://jyywiki.cn/static/Virgil.woff2 (from https://jyywiki.cn/pages/ISER/2021/slides/img/static-analysis.svg)
```
