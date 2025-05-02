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

========================================================================================

# 更新内容如下：

### 1. 操作系统概述  
**课程核心内容**：  
1. **Why**: 学习操作系统的必要性  
    - 操作系统是软件与硬件的桥梁，理解其本质（如状态机模型）对掌握系统行为至关重要。  
    - AI 时代需掌握基本概念与提问能力，结合工具（如搜索引擎、大语言模型）快速解决问题。  

2. **What**: 操作系统的定义  
    - 封装计算机系统状态（CPU、内存等），通过指令执行驱动状态机迁移。  
    - 通过系统调用与硬件交互，程序执行时感知不到操作系统存在，但系统调用会触发状态切换。  

3. **How**: 学习方法  
    - 实践导向：运行代码示例（如最小程序）、使用调试工具（如 strace）。  
    - 结合开源项目（如 GNU Coreutils、Toybox）理解命令行工具实现。  

**课后实践**：  
- 尝试编译运行最小二进制程序，观察系统调用序列。  
- 定制开发环境（如 fish、tmux），探索工具链与 AI 辅助编程的结合。  

---

### 2. 应用视角的操作系统  
**核心模型与工具**：  
1. **状态机模型**：  
    - 程序本质是状态机，编译器将高级语言翻译为指令序列。  
    - 系统调用是程序与操作系统交互的唯一接口（如 x86-64 的 `syscall` 指令）。  

2. **最小程序分析**：  
    - 空 `main` 函数生成的二进制仍包含初始化代码，可通过调整链接脚本实现最小化。  
    - 系统调用示例：`exit` 直接终止进程，体现操作系统对程序生命周期的控制。  

3. **工具链应用**：  
    - `strace` 追踪系统调用序列，结合过滤选项（如 `-e trace=open,read`）提高可读性。  
    - 逆向工具（如 `objdump`、`gdb`）分析二进制文件结构，探索程序执行流。  

**实践任务**：  
- 实现非递归汉诺塔，模拟递归执行流。  
- 扩展函数互相调用场景（如 `fff` 和 `ggg`），观察栈帧变化。  

---

### 3. 硬件视角的操作系统  
**硬件与固件机制**：  
1. **计算机系统模型**：  
    - 硬件行为严格遵循指令规范，Reset 后固件（如 OpenSBI）初始化硬件并加载操作系统。  
    - 处理器为无状态执行单元，状态由寄存器与内存内容定义。  

2. **固件与操作系统加载**：  
    - 固件规范（如 UEFI）确保硬件兼容性，复杂代码库（如 OpenSBI）需借助 AI 辅助理解。  
    - 编译 OpenSBI 时，可通过分析 Makefile 依赖关系与目标定位核心流程。  

3. **内核角色**：  
    - 操作系统内核作为特权级软件，管理硬件资源并提供系统调用接口。  
    - 系统调用实现需遵循 ABI（如寄存器传参约定），硬件通过异常机制切换至内核态。  

**实践与工具**：  
- 使用 `gdb` 的 TUI 模式与反向调试功能，深入分析程序执行细节。  
- 探索硬件模拟器（如 QEMU）行为，观察 Reset 后固件到操作系统的启动流程。  

---

### 4. 数学视角的操作系统  
**核心模型与工具**：  
1. **程序与状态机模型**：  
    - 程序本质是状态机，编译器将代码转换为状态转移序列。  
    - 操作系统通过中断和系统调用控制状态机执行流，构建多任务并行假象。  

2. **Curry-Howard 对应**：  
    - 命题即类型：逻辑命题对应程序类型（如蕴含 `A→B` 对应函数类型）。  
    - 证明即程序：构造性证明对应具体程序实现，形成直觉逻辑基础。  

3. **模型检查与形式验证**：  
    - 使用 Python 等工具建模操作系统行为，通过状态机遍历验证程序正确性。  
    - 形式化验证缩小错误窗口，但不保证绝对正确（需结合人工检查）。  

**实践任务**：  
- 用 Python 实现简单状态机模型，模拟 `fork` 系统调用的行为。  
- 基于 Curry-Howard 对应，将逻辑命题转换为具体代码并验证。  

---

**延伸学习**：  
- 阅读 *Operating Systems: Three Easy Pieces* 第 1-2 章，巩固状态机与系统调用概念。  
- 实践 GNU Coreutils 命令（如 `tar`、`strace`），结合 BusyBox 源码理解工具实现。  

### 5. 程序和进程  
**核心模型与工具**：  
1. **进程本质与系统调用**：  
    - 进程是操作系统中最基本的资源分配单位，包含程序状态和操作系统内部状态。  
    - 系统调用 API：Linux 的 `fork`、`exec`、`wait`、`exit`，Windows 的 `CreateProcess` 和 `TerminateProcess`。  

2. **进程生命周期管理**：  
    - 进程创建时 PID 递增分配，32 位整数范围可能导致循环重用，需操作系统管理 PID 分配策略。  
    - 终止进程时，操作系统回收资源并更新进程状态表。  

3. **API 参数与功能**：  
    - Windows 的 `CreateProcess` 需指定可执行路径、命令行参数、安全属性等，`TerminateProcess` 强制终止进程。  
    - Linux 的 `fork` 复制父进程状态，`exec` 替换进程映像，`wait` 同步子进程状态。  

**实践任务**：  
- 编写多进程程序，验证进程创建、执行和终止流程。  
- 分析 PID 分配规律，探索操作系统进程管理机制。  

---

### 6. 进程的地址空间  
**核心模型与工具**：  
1. **虚拟内存与隔离机制**：  
    - 操作系统通过虚拟内存为每个进程提供独立地址空间，实现内存隔离和保护。  
    - 系统调用 `mmap` 和 `munmap` 管理地址空间的映射与释放。  

2. **地址空间操作工具**：  
    - `pmap` 命令通过解析 `/proc/pid/maps` 实现进程内存布局分析，Windows 可通过 API 或工具（如 VMMap）实现类似功能。  
    - 入侵进程地址空间：使用 `ptrace`、`process_vm_writev` 或共享内存机制修改其他进程内存（需权限）。  

3. **初始状态与动态扩展**：  
    - 进程启动时加载代码段、数据段和堆栈段，动态内存分配通过 `brk`/`sbrk` 或 `malloc`/`free` 实现。  

**实践任务**：  
- 使用 `mmap` 实现文件映射到内存，观察读写性能差异。  
- 编写程序通过 `ptrace` 修改其他进程内存，验证权限与可行性。  

---
  
### 7. 访问操作系统对象  
**核心模型与工具**：  
1. **文件描述符机制**：  
    - UNIX 系统中，文件描述符是操作系统中表示打开文件或操作系统对象的指针，Windows 使用更直接的 handle 机制。  
    - 系统调用（如 `open`, `read`, `write`）允许应用程序通过文件描述符操作对象。  

2. **对象序列化与通用机制**：  
    - UNIX 的 "Everything is a file" 原则简化对象访问，但也存在局限性（如非文件类对象的适配问题）。  
    - 操作系统通过 API（如 `mmap`, `fork`, `execve`）提供对象管理能力，支持进程生态构建。  

3. **操作系统对象访问策略**：  
    - 机制与策略分离：操作系统仅提供基础接口，应用程序自行实现复杂逻辑（如路径解析、权限管理）。  
    - 示例：`glob patterns` 扩展文件名匹配，支持通配符（如 `*`, `?`），提升文件操作灵活性。  

**实践任务**：  
- 通过 `strace` 追踪文件操作的系统调用序列，分析对象访问行为。  
- 阅读《Operating Systems: Three Easy Pieces》第 39 章，理解文件与目录的实现机制。  

---  

### 8. 终端和 UNIX Shell  
**核心模型与工具**：  
1. **终端与信号处理**：  
    - 终端模拟器通过伪终端（pty）管理输入输出流，`Ctrl+C` 发送 `SIGINT` 信号终止进程。  
    - `sigaction` 替代传统信号机制，支持更安全的信号处理（如阻塞竞争信号）。  

2. **进程与会话管理**：  
    - `session` 和 `process group` 机制隔离终端窗口的进程组，简化任务控制（如后台/前台切换）。  
    - `pipe` 和 `mkfifo` 实现进程间通信，支持 Shell 管道（`|`）功能。  

3. **Shell 编程语言**：  
    - Shell 作为系统调用的高级抽象，通过组合 `fork`, `execve`, `pipe` 实现复杂任务（如重定向、多任务）。  
    - 示例：Shell 脚本通过 `&` 启动后台进程，通过 `wait` 同步子进程。  

**实践任务**：  
- 实现简易 Shell 支持管道和重定向功能，观察进程间通信机制。  
- 分析 `strace` 跟踪的终端操作日志，理解信号与会话控制流程。  

---  

### 9. C 标准库和实现  
**核心模型与工具**：  
1. **libc 的抽象作用**：  
    - C 标准库（libc）封装系统调用（如 `malloc` 抽象 `mmap`），提供跨平台编程接口。  
    - 通过 `offsetof` 宏实现结构体成员偏移量计算，支持灵活的内存操作（如链表、序列化）。  

2. **动态内存管理**：  
    - `malloc` 和 `free` 基于堆管理算法（如伙伴系统、slab 分配器）实现动态内存分配。  
    - 内存碎片问题通过合并空闲块、按大小分类分配策略缓解。  

3. **系统调用与环境抽象**：  
    - libc 提供 `FILE` 结构体抽象文件描述符，支持缓冲 I/O（如 `fprintf` 减少系统调用开销）。  
    - 错误处理通过 `errno` 全局变量传递系统调用失败原因，简化调试流程。  

**实践任务**：  
- 阅读 musl libc 源码，分析 `printf` 或 `malloc` 的实现逻辑。  
- 使用 `objdump` 反汇编 libc 函数，观察系统调用与用户态代码的交互细节。  


### 10. 可执行文件  
**核心模型与工具**：  
1. **可执行文件本质**：  
    - 可执行文件是描述进程状态机初始状态的数据结构，通过加载器将初始状态映射到操作系统。  
    - ELF 文件的核心部分为 PT_LOAD 段，包含代码、数据等需加载至内存的内容。  

2. **静态链接机制**：  
    - 编译器工具链（如 `gcc`）将高级语言代码翻译为可执行文件，涉及符号解析、地址分配等步骤。  
    - 通过调整链接脚本（如 `ld`）可自定义程序内存布局，实现最小化二进制文件。  

3. **ELF 文件分析**：  
    - 使用工具（如 `readelf`、`objdump`）解析 ELF 头、程序头表和节头表，观察段与节的映射关系。  
    - 理解 ELF 设计中“不可读性”的原因：其数据结构面向加载器而非人类阅读。  

**实践任务**：  
- 动手构建自定义可执行文件格式，验证加载器如何通过 `mmap` 实现段映射。  
- 分析空 `main` 函数生成的二进制文件，探索初始化代码与链接脚本的关联。  

---  

### 11. 动态链接和加载  
**核心模型与工具**：  
1. **动态链接机制**：  
    - 库函数与应用程序分离，运行时通过动态链接加载共享库（如 `libc.so`）。  
    - 全局偏移表（GOT）和过程链接表（PLT）实现延迟绑定，优化函数调用性能。  

2. **虚拟内存与映射**：  
    - `mmap` 系统调用将共享库映射到进程地址空间，支持按需加载与内存共享。  
    - 虚拟内存管理通过页表实现物理内存与逻辑地址的解耦，保障进程隔离性。  

3. **动态链接实现**：  
    - 手工实现动态加载器需解析 ELF 符号表，处理重定位项（如 `R_X86_64_JUMP_SLOT`）。  
    - 动态链接工具（如 `ld-linux.so`）扫描依赖库并递归加载，维护符号解析的一致性。  

**实践任务**：  
- 实现简易动态链接器，支持加载共享库并解析符号引用。  
- 使用 `gdb` 调试动态链接过程，观察 GOT/PLT 在函数调用时的填充机制。  

---  

### 12. 构建应用生态  
**核心模型与工具**：  
1. **操作系统抽象层次**：  
    - 硬件层提供指令集架构（ISA），操作系统基于 ISA 实现对象（如进程、文件）和系统调用接口。  
    - 系统工具链（如 `coreutils`、`shell`、`apt`）构建在系统调用之上，支撑应用开发与部署。  

2. **应用生态构成**：  
    - 包管理器（如 `apt`）管理软件依赖，通过仓库机制分发二进制与元数据。  
    - 编译器（如 `gcc`）与构建工具（如 `make`）将源代码转换为可执行文件，依赖动态链接库实现代码复用。  

3. **技术演化与兼容性**：  
    - 系统调用接口的稳定性保障向后兼容，形成技术壁垒（如 UNIX/Linux 生态）。  
    - 应用程序通过分层抽象（硬件→OS→工具→应用）实现功能扩展，生态复杂性源于历史积累。  

**实践任务**：  
- 分析 Linux 系统调用表（如 `/usr/include/asm/unistd.h`），理解系统调用编号与功能映射。  
- 编写 Shell 脚本整合系统工具（如 `grep`、`awk`），模拟应用级功能流水线。  


### 13. 多处理器编程从入门到放弃  
**核心模型与工具**：  
1. **共享内存线程模型**：  
    - 线程通过共享内存实现并行，允许多个执行流共享同一地址空间。  
    - 使用 POSIX Threads（`pthread`）库管理线程生命周期（如线程分离、栈配置）。  

2. **并发编程挑战**：  
    - 编译优化与处理器行为导致并发程序行为难以预测。  
    - 人类直觉（顺序逻辑）与并发执行（非确定性）存在根本冲突。  

3. **状态机扩展**：  
    - 多线程模型可视为共享内存上的多状态机交替执行，通过 `spawn` 和 `join` 接口协调执行流。  

**实践任务**：  
    - 理解线程库（如 `pthread`）的 API 设计，掌握线程创建、分离和同步方法。  
    - 探索并发程序在编译优化下的行为差异，分析共享内存访问的潜在问题。  

---

### 15. 并发控制同步 1  
**核心模型与工具**：  
1. **同步问题定义**：  
    - 线程需协作完成任务的执行顺序控制（如生产者-消费者模型）。  
    - 互斥锁无法解决执行顺序依赖问题，需引入同步机制。  

2. **条件变量**：  
    - 通过条件变量（如 `pthread_cond_t`）实现线程等待特定条件成立。  
    - 条件检查与临界区操作需绑定，避免“虚假唤醒”问题。  

3. **并发计算图**：  
    - 利用同步机制构建任务依赖关系图，确保线程按拓扑顺序执行。  

**实践任务**：  
    - 实现生产者-消费者模型，验证条件变量在同步中的作用。  
    - 分析条件变量与互斥锁的配合使用模式，总结同步编程的常见陷阱。  

---

### 16. 并发控制同步 2  
**核心模型与工具**：  
1. **信号量机制**：  
    - 信号量（Semaphore）是互斥锁的推广，通过计数器管理资源访问。  
    - 支持 `P()`（等待）和 `V()`（释放）操作，适用于多资源分配场景（如线程池）。  

2. **同步实现对比**：  
    - 信号量通过计数抽象简化同步逻辑（如停车场车位、游泳馆手环模型）。  
    - 条件变量依赖显式状态检查，信号量更适用于资源数量明确的场景。  

3. **同步本质**：  
    - 同步的核心是建立“happens-before”关系，确保线程间操作顺序可控。  

**实践任务**：  
    - 使用信号量重构生产者-消费者模型，对比与条件变量实现的异同。  
    - 设计多线程协作任务（如并行计算流水线），验证信号量的灵活性与局限性。  


### 14. 并发控制互斥  
**核心模型与机制**：  
1. **互斥基础**：  
    - 互斥（mutual exclusion）用于阻止并发或并行执行，确保共享资源的独占访问。  
    - 并发编程的复杂性通过锁机制（`lock`/`unlock`）简化，串行化关键代码段以减少竞争。  

2. **共享内存实现**：  
    - 通过共享内存协调线程行为，但需解决同步问题（如竞态条件）。  
    - 示例：线程间共享变量需避免非原子操作的交叉执行。  

3. **原子指令与系统调用**：  
    - 原子指令（如 `CAS`）确保操作不可分割，避免中间状态干扰。  
    - 系统调用（如 `futex`）提供内核支持的互斥原语，结合自旋锁优化性能。  

**实践挑战**：  
- 实现互斥需权衡性能与正确性，避免过度串行化导致多核利用率下降。  
- 现代系统依赖硬件原子操作、中断管理及自旋机制提升互斥效率。  

---

### 17. 并发 Bugs  
**常见错误模式**：  
1. **数据竞争**：  
    - 未同步的共享内存访问导致不可预测结果（如 2003 年美加大停电事故）。  
    - 触发条件依赖罕见线程调度，难以通过常规测试覆盖。  

2. **死锁**：  
    - 多线程因循环等待资源陷入永久阻塞，需通过锁顺序约定或超时机制避免。  

3. **原子性与顺序违反**：  
    - 原子性违反：预期不可中断的代码段被线程切换打断（如非原子写操作）。  
    - 顺序违反：线程执行顺序未按预期同步（如未正确使用条件变量）。  

**应对策略**：  
- 使用事务内存（Transactional Memory）或数据库式事务增强原子性保障。  
- 通过编程模型（如 `channel` 通信、自动内存管理）减少开发者犯错可能。  

---

### 18. 真实世界的并发编程 1  
**领域特定模型**：  
1. **高性能计算（HPC）**：  
    - 使用 MPI（消息传递接口）和 OpenMP（共享内存并行）划分计算任务。  
    - 物理模拟中网格边界通过消息传递或共享内存同步处理。  

2. **Web 与数据中心**：  
    - 异步编程模型（如 Node.js 事件循环）避免线程阻塞，提升 I/O 密集型任务效率。  
    - Goroutines（Go 语言）结合轻量级线程与调度器，实现高并发服务。  

**技术演进**：  
- 领域特定并发模型通过限制灵活性换取易用性与性能优化（如 MapReduce 简化分布式计算）。  

---

### 18. 真实世界的并发编程 2  
**硬件加速与 AI 并行**：  
1. **CPU 的局限性**：  
    - 传统多线程在数据并行任务（如图形渲染、矩阵运算）中效率不足。  

2. **GPU 与 GPGPU**：  
    - GPU 通过大规模并行计算单元（CUDA 核心）加速 SIMD 类任务。  
    - GPGPU 通用化推动科学计算与深度学习（如 TensorFlow/PyTorch 利用 CUDA）。  

3. **AI 时代的编程模型**：  
    - 张量计算框架（如 CUDA、ROCm）抽象硬件细节，支持自动并行化。  
    - 领域专用语言（DSL）与编译器优化（如 TVM）提升模型训练与推理效率。  

**趋势与展望**：  
- 从通用 CPU 到领域加速器（如 TPU）的演进，反映算力需求驱动技术革新。  
- 未来并发编程或进一步融合硬件特性与高层抽象，降低开发者负担。  

---

========================================================================================

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
