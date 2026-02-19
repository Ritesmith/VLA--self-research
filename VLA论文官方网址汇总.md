# VLA论文官方网址汇总

本文档汇总了VLA核心论文的官方网站、GitHub仓库和相关数据库链接，包括经典论文和最新前沿研究。

## 1️⃣ RT-1: Robotics Transformer (2022)

### 基本信息
- **标题**: RT-1: Robotics Transformer for Real-World Control at Scale
- **发表时间**: 2022年
- **机构**: Google Robotics

### 官方网址
- **项目网站**: https://robotics-transformer1.github.io/
- **论文PDF**: https://robotics-transformer1.github.io/assets/rt1.pdf
- **GitHub仓库**: https://github.com/google-research/robotics_transformer
- **arXiv链接**: https://arxiv.org/abs/2212.06817

### 核心特点
- 首个大规模真实世界数据集
- 35M参数，3Hz实时推理
- 700+任务，97%成功率

---

## 2️⃣ RT-2: Vision-Language-Action Models (2023.7)

### 基本信息
- **标题**: RT-2: Vision-Language-Action Models - Transfer Web Knowledge to Robotic Control
- **发表时间**: 2023年7月
- **机构**: Google DeepMind

### 官方网址
- **项目网站**: https://robotics-transformer2.github.io/
- **论文PDF**: https://robotics-transformer2.github.io/assets/rt2.pdf
- **arXiv链接**: https://arxiv.org/abs/2307.15818

### 核心特点
- 动作作为文本令牌
- 联合微调，涌现语义推理
- 5B-55B参数

---

## 3️⃣ PaLM-E: An Embodied Multimodal Language Model (2023.3)

### 基本信息
- **标题**: PaLM-E: An Embodied Multimodal Language Model
- **发表时间**: 2023年3月
- **机构**: Google

### 官方网址
- **项目网站**: https://palm-e.github.io/
- **论文PDF**: https://arxiv.org/pdf/2303.03378
- **arXiv链接**: https://arxiv.org/abs/2303.03378
- **GitHub仓库**: https://github.com/kyegomez/PALM-E

### 核心特点
- 562B参数，最大具身多模态模型
- 多模态句子，连续传感器模态嵌入
- 链式思维推理

---

## 4️⃣ RT-X: Open X-Embodiment Models (2023.10)

### 基本信息
- **标题**: Open X-Embodiment: Robotic Learning Datasets and RT-X Models
- **发表时间**: 2023年10月
- **机构**: Open X-Embodiment Collaboration (21个机构)

### 官方网址
- **项目网站**: https://robotics-transformer-x.github.io/
- **arXiv链接**: https://arxiv.org/abs/2310.08864
- **数据集下载**: https://go.hyper.ai/JAeHn

### 核心特点
- 22种机器人，527种技能
- 160266个任务
- 跨具身训练，21机构合作

---

## 5️⃣ RT-H: Action Hierarchies Using Language (2024.3)

### 基本信息
- **标题**: RT-H: Action Hierarchies Using Language
- **发表时间**: 2024年3月
- **机构**: Google DeepMind, Stanford University

### 官方网址
- **项目网站**: https://rt-hierarchy.github.io/
- **论文PDF**: https://arxiv.org/pdf/2403.01823.pdf
- **arXiv链接**: https://arxiv.org/abs/2403.01823

### 核心特点
- 语言动作层次
- 人类干预学习
- 比RT-2提升15%

---

## 6️⃣ OpenVLA: An Open-Source Vision-Language-Action Model (2024.6)

### 基本信息
- **标题**: OpenVLA: An Open-Source Vision-Language-Action Model
- **发表时间**: 2024年6月
- **机构**: Stanford, UC Berkeley, CMU, MIT, Toyota Research Institute等

### 官方网址
- **项目网站**: https://openvla.github.io/
- **GitHub仓库**: https://github.com/openvla/openvla
- **arXiv链接**: https://arxiv.org/abs/2406.09246

### 核心特点
- 完全开源，7B参数
- LoRA微调，多视觉编码器
- 性能超越RT-2-X (55B参数)

---

## 7️⃣ RDT-1B: A Diffusion Foundation Model for Bimanual Manipulation (2024.10)

### 基本信息
- **标题**: RDT-1B: A Diffusion Foundation Model for Bimanual Manipulation
- **发表时间**: 2024年10月
- **机构**: 清华大学

### 官方网址
- **项目网站**: https://rdt-robotics.github.io/rdt-robotics/
- **论文PDF**: https://arxiv.org/pdf/2410.07864
- **arXiv链接**: https://arxiv.org/abs/2410.07864

### 核心特点
- 1.2B参数，最大扩散基础模型
- 物理可解释统一动作空间
- 双臂专精，成功率提升56%

---

## 8️⃣ Pi_0: A Vision-Language-Action Flow Model (2025.2)

### 基本信息
- **标题**: π0: A Vision-Language-Action Flow Model for General Robot Control
- **发表时间**: 2025年2月
- **机构**: Physical Intelligence

### 官方网址
- **论文PDF**: https://www.physicalintelligence.company/download/pi0.pdf
- **公司网站**: https://www.physicalintelligence.company/

### 核心特点
- 流匹配架构
- 50Hz实时推理
- 跨具身训练，复杂灵巧操作

---

## 9️⃣ ConRFT: A Reinforced Fine-tuning Method for VLA Models (RSS 2025)

### 基本信息
- **标题**: ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy
- **发表时间**: 2025年4月14日
- **会议**: RSS 2025
- **机构**: 自动化所 & 中国科学院大学

### 官方网址
- **arXiv链接**: https://arxiv.org/abs/2502.05450

### 核心特点
- 两阶段微调框架（离线 + 在线）
- 融合行为克隆（BC）与Q学习
- 统一的一致性训练目标
- 仅需40-60分钟视频演示即可微调

---

## 🔟 FiS-VLA: Fast-in-Slow VLA (2025)

### 基本信息
- **标题**: Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning
- **发表时间**: 2025年
- **机构**: 北京大学、香港中文大学、北京通用人工智能研究院

### 官方网址
- **arXiv链接**: https://arxiv.org/abs/2506.01953
- **论文PDF**: https://arxiv.org/pdf/2506.01953
- **项目主页**: https://fast-in-slow.github.io/
- **GitHub仓库**: https://github.com/CHEN-H01/Fast-in-Slow
- **实验室主页**: https://pku-hmi-lab.github.io/HMI-Web/index.html

### 核心特点
- 快慢双系统架构（System 1 & System 2）
- 异构模态输入与异步运行频率
- 快速执行模块嵌入预训练VLM中
- 高达117.7Hz控制频率
- 综合性能超越国际标杆Pi_0达30%

---

## 1️⃣1️⃣ Gemini Robotics (2025)

### 基本信息
- **标题**: Gemini Robotics: Bringing AI into Physical World
- **发表时间**: 2025年3月
- **机构**: Google

### 官方网址
- **论文PDF**: https://arxiv.org/pdf/2503.20020
- **arXiv链接**: https://arxiv.org/abs/2503.20020

### 核心特点
- 基于Gemini 2.0的VLA通用模型
- 首个可供微调的离线VLA模型
- 适用于机械臂、人形机器人等多种形态
- 遵循多样化、开放词汇的指令
- 对物体类型和位置变化具有鲁棒性

---

## 1️⃣2️⃣ HoloBrain-0 (2025)

### 基本信息
- **标题**: HoloBrain-0: Full-Stack VLA Framework with Embodied Prior
- **开源时间**: 2025年2月13日
- **机构**: 地平线（Horizon Robotics）

### 官方网址
- **论文arXiv**: https://arxiv.org/abs/2602.12062
- **GitHub仓库（核心算法）**: https://github.com/HorizonRobotics/RoboOrchardLab
- **GitHub仓库（真机基础设施）**: https://github.com/HorizonRobotics/RoboOrchard
- **开源公告**: 地平线HorizonRobotics公众号

### 核心特点
- 首创在架构中显式注入"具身先验"
- 将多视角相机参数与机器人运动学结构显式融入模型
- 大幅提升三维空间理解能力
- 具备统一的3D空间感知与跨本体控制能力
- 灵活适配单机械臂、双机械臂、移动机器人等多种机器人形态
- 应用场景：柔软衣物的灵巧折叠、未知物体的通用抓取
- 轻量化GD版本（0.2B）可适配地平线RDKS100机器人开发者套件

### 开源内容
- HoloBrain-0核心算法（RoboOrchardLab）
- 完整基础设施RoboOrchard（真机部署框架）

---

## 1️⃣3️⃣ DecisionNCE (ICML 2024)

### 基本信息
- **标题**: DecisionNCE: Embodied Multimodal Representations via Implicit Preference Learning
- **发表时间**: 2024年
- **会议**: ICML 2024

### 官方网址
- **arXiv链接**: https://arxiv.org/abs/2402.18137
- **GitHub仓库**: https://github.com/2toinf/DecisionNCE
- **项目主页**: https://2toinf.github.io/DecisionNCE/

### 核心特点
- 轨迹级别对齐（trajectory-level grounding）
- 解决语言和视频轨迹的对齐问题
- 利用无动作标签的分布外数据
- 为具身智能提供通用的表征预训练方案
- 缓解数据稀缺问题

---

## 1️⃣4️⃣ Genesis (2024)

### 基本信息
- **标题**: Genesis: A Generative and Universal Physics Engine for Robotics and Beyond
- **发表时间**: 2024年
- **机构**: Genesis Embodied AI团队（全球18所校企科研单位联合）

### 官方网址
- **项目主页**: https://genesis-embodied-ai.github.io/
- **GitHub仓库**: https://gitcode.com/GitHub_Trending/genesi/Genesis

### 核心特点
- 从头开始构建的通用物理引擎
- 模拟多种材料和物理现象
- 轻量级、超快速、Python友好
- 支持多种计算后端（CPU、Nvidia/AMD GPU、Apple Metal）
- 提供多种物理求解器（刚体、MPM、SPH、FEM等）
- 广泛的材料模型
- 模拟速度比实时快43万倍（Franka机械臂场景）
- 生成式代理框架，支持自然语言控制场景生成

---

## 1️⃣5️⃣ DWL (RSS 2024)

### 基本信息
- **标题**: Mastering Challenging Terrains with Denoising World Model Learning
- **发表时间**: 2024年
- **会议**: RSS 2024
- **机构**: 清华大学交叉信息研究院

### 官方网址
- **获奖情况**: RSS 2024杰出论文入围奖

### 核心特点
- 去噪世界模型学习
- 有效去除真实世界噪声扰动
- 全球范围内首次通过端到端RL和零样本仿真到真实转换
- 实现人形机器人通用适应各类复杂的现实世界地形

---

## 1️⃣6️⃣ ATM (RSS 2024)

### 基本信息
- **标题**: Any-point Trajectory Modeling for Policy Learning
- **发表时间**: 2024年7月12日
- **会议**: RSS 2024
- **机构**: UC Berkeley、清华大学IIIS、Stanford University、上海AI实验室、上海期智研究院、香港中文大学（CUHK）

### 官方网址
- **arXiv链接**: https://arxiv.org/abs/2401.00025
- **项目网站**: https://xingyu-lin.github.io/atm
- **GitHub仓库**: https://github.com/Large-Trajectory-Model/ATM

### 核心特点
- 任意点轨迹建模
- 通过预训练轨迹模型预测视频帧内任意点的未来轨迹
- 利用视频为机器人提供演示
- 实现以最少的动作标签数据学习鲁棒的视觉运动策略
- 为小样本和跨具身机器人学习提供新视角
- 获得RSS 2024全数审稿人满分评价
- 在130多个语言条件任务中平均成功率63%（vs 之前方法最高成功率37%），性能提升80%

---

## 1️⃣7️⃣ iRe-VLA (ICRA 2025)

### 基本信息
- **标题**: iRe-VLA: Stable and Efficient Reinforcement Learning Fine-tuning for Large Vision-Language-Action Models
- **发表时间**: 2025年
- **会议**: ICRA 2025
- **机构**: 清华大学、加州大学伯克利分校、上海期智研究院

### 官方网址
- **会议**: ICRA 2025 (https://www.icra2025.org/)
- **论文链接**: 待会议正式发布（ICRA 2025会议论文）
- **arXiv链接**: 待补充（会议发表后可能发布）
- **项目主页**: 待补充

**注意**: https://arxiv.org/abs/2502.05450 是 ConRFT 的链接，不是 iRe-VLA。iRe-VLA 将在 ICRA 2025 会议正式发表。

### 核心特点
- 解决VLA模型强化学习微调不稳定的问题
- 作为"稳定器"让VLA模型的RL学习过程平滑高效
- 解决灾难性遗忘问题
- 降低计算资源需求
- 让VLA模型能够通过真实环境互动（RL）自我提升

### 学习重点
- 稳定器（Stabilizer）机制
- 渐进式RL微调策略
- 预训练知识保持方法
- 高效训练算法

---

## 1️⃣8️⃣ Genie2 (2024)

### 基本信息
- **标题**: Genie2 - Foundation World Model
- **发表时间**: 2024年
- **机构**: Google DeepMind

### 官方网址
- **项目网站**: https://deepmind.google/discover/blog/genie-2/
- **论文PDF**: 待补充
- **arXiv链接**: 待补充

### 核心特点
- 基础世界模型（Foundation World Model）
- 从单张图像提示生成无限多样的可交互3D环境
- 不仅是视频生成器，更是可玩的游戏引擎
- 代理可以在其中通过键盘或动作交互
- 为VLA提供世界建模能力

### 学习重点
- 世界模型构建方法
- 可交互环境生成
- 物理规律遵循机制
- VLA预训练数据生成

---

## 📊 相关数据集和工具

### 主要数据集
- **Open X-Embodiment**: https://go.hyper.ai/JAeHn
  - 22种机器人，160266个任务
  - 迄今为止最大的开源机器人数据集

- **RoboCat**: 多任务机器人数据集
- **Bridge Data**: 真实世界机器人操作数据集
- **BEHAVIOR**: 机器人技能评估基准

### 主要工具库
- **PyTorch**: 深度学习框架
- **TensorFlow**: 深度学习框架
- **Hugging Face Transformers**: 预训练模型库
- **PyBullet**: 物理仿真引擎
- **MuJoCo**: 物理仿真引擎
- **Isaac Gym**: NVIDIA机器人仿真环境

### 评估基准
- **Real-World Robot Challenge**: 真实世界机器人挑战赛
- **BEHAVIOR**: 机器人技能评估基准
- **RoboNet**: 机器人操作数据集

---

## 🔗 快速访问链接

### 按类型分类

#### 项目网站
- RT-1: https://robotics-transformer1.github.io/
- RT-2: https://robotics-transformer2.github.io/
- PaLM-E: https://palm-e.github.io/
- RT-X: https://robotics-transformer-x.github.io/
- RT-H: https://rt-hierarchy.github.io/
- OpenVLA: https://openvla.github.io/
- RDT-1B: https://rdt-robotics.github.io/rdt-robotics/
- ATM: https://xingyu-lin.github.io/atm
- DecisionNCE: https://2toinf.github.io/DecisionNCE/
- ConRFT: https://cccedric.github.io/conrft/
- Gemini Robotics: 待补充
- FiS-VLA: https://fast-in-slow.github.io/

#### arXiv链接
- RT-1: https://arxiv.org/abs/2212.06817
- PaLM-E: https://arxiv.org/abs/2303.03378
- RT-2: https://arxiv.org/abs/2307.15818
- RT-X: https://arxiv.org/abs/2310.08864
- RT-H: https://arxiv.org/abs/2403.01823
- OpenVLA: https://arxiv.org/abs/2406.09246
- RDT-1B: https://arxiv.org/abs/2410.07864
- Pi_0: 论文PDF在公司网站
- ATM: https://arxiv.org/abs/2401.00025
- DecisionNCE: https://arxiv.org/abs/2402.18137
- ConRFT: https://arxiv.org/abs/2502.05450
- Gemini Robotics: https://arxiv.org/abs/2503.20020
- FiS-VLA: https://arxiv.org/abs/2506.01953

#### GitHub仓库
- RT-1: https://github.com/google-research/robotics_transformer
- PaLM-E: https://github.com/kyegomez/PALM-E
- OpenVLA: https://github.com/openvla/openvla
- RDT-1B: https://rdt-robotics.github.io/rdt-robotics/
- ATM: https://github.com/Large-Trajectory-Model/ATM
- DecisionNCE: https://github.com/2toinf/DecisionNCE
- ConRFT: 待补充
- Gemini Robotics: 待补充
- FiS-VLA: https://github.com/CHEN-H01/Fast-in-Slow

---

## 💡 使用建议

### 学习资源
1. **论文阅读**: 先阅读arXiv上的论文，理解核心思想
2. **项目网站**: 访问项目网站，了解详细实现和演示
3. **GitHub代码**: 查看GitHub仓库，学习代码实现细节
4. **数据集**: 下载相关数据集，进行实验和复现

### 实验建议
1. **环境配置**: 根据项目网站的要求配置实验环境
2. **数据准备**: 下载并预处理所需的数据集
3. **代码复现**: 参考GitHub代码，复现论文中的实验
4. **性能评估**: 使用标准基准评估模型性能

### 研究方向
1. **架构创新**: 研究新的VLA架构设计
2. **训练策略**: 探索更高效的训练和微调方法
3. **数据增强**: 研究数据增强技术，提升泛化能力
4. **应用拓展**: 将VLA应用到新的机器人平台和任务

---

## 📝 论文分类总结

### 经典VLA论文（8篇）
这些是VLA领域的基础性工作，建立了VLA的核心范式：

1. **RT-1 (2022)** - 首个大规模真实世界数据集
2. **RT-2 (2023.7)** - 动作作为文本令牌，联合微调
3. **PaLM-E (2023.3)** - 562B具身多模态模型
4. **RT-X (2023.10)** - 跨具身训练，21机构合作
5. **RT-H (2024.3)** - 语言动作层次，人类干预学习
6. **OpenVLA (2024.6)** - 开源7B，LoRA微调
7. **RDT-1B (2024.10)** - 1.2B扩散模型，双臂专精
8. **Pi_0 (2025.2)** - 流匹配，50Hz实时推理

### 前沿VLA论文（7篇）
这些是VLA领域的最新突破，代表了技术发展的前沿方向：

1. **ConRFT (RSS 2025)** - 强化学习微调方法
2. **FiS-VLA (2025)** - 快慢双系统架构
3. **Gemini Robotics (2025)** - 基于Gemini 2.0的VLA通用模型
4. **HoloBrain-0 (2025)** - 显式注入具身先验的全栈VLA框架
5. **DecisionNCE (ICML 2024)** - 轨迹级别对齐
6. **Genesis (2024)** - 通用物理平台
7. **DWL (RSS 2024)** - 去噪世界模型学习
8. **ATM (RSS 2024)** - 任意点轨迹建模
9. **iRe-VLA (ICRA 2025)** - 稳定RL微调

### 技术演进趋势

```
2022: RT-1 - 首个大规模真实世界数据集
  ↓
2023.3: PaLM-E - 562B具身多模态
  ↓
2023.7: RT-2 - 动作作为文本令牌
  ↓
2023.10: RT-X - 跨具身训练
  ↓
2024.3: RT-H - 语言动作层次
  ↓
2024.6: OpenVLA - 开源7B
  ↓
2024.10: RDT-1B - 1.2B扩散模型
  ↓
2025.2: Pi_0 - 流匹配，50Hz
  ↓
2025: FiS-VLA - 快慢双系统
  ↓
2025: iRe-VLA - 稳定RL微调
  ↓
2025: Gemini Robotics - Gemini 2.0 VLA
  ↓
2025: HoloBrain-0 - 具身先验注入
```

### 关键技术方向

1. **强化学习微调**: ConRFT, iRe-VLA
2. **快慢双系统**: FiS-VLA
3. **世界模型**: Genie2, DWL, Genesis
4. **具身先验**: HoloBrain-0
5. **轨迹建模**: DecisionNCE, ATM
6. **多模态扩展**: 触觉、力觉等
7. **实时性优化**: Pi_0 (50Hz), FiS-VLA (117.7Hz)

### 开源项目

**完全开源**:
- OpenVLA (7B参数）
- HoloBrain-0 (全栈VLA框架）
- Genesis (通用物理平台）
- DecisionNCE (表征预训练）
- ATM (轨迹建模）
- FiS-VLA (快慢双系统）

**部分开源**:
- RT-1 (代码）
- RT-X (数据集和工具）
- PaLM-E (代码）

**闭源**:
- RT-2
- RDT-1B
- Pi_0
- Gemini Robotics

### 中国团队贡献

**清华大学**:
- RDT-1B (2024.10) - 1.2B扩散模型
- DWL (RSS 2024) - 去噪世界模型
- ATM (RSS 2024) - 任意点轨迹建模
- iRe-VLA (ICRA 2025) - 稳定RL微调

**北京大学**:
- FiS-VLA (2025) - 快慢双系统

**地平线**:
- HoloBrain-0 (2025) - 具身先验注入

**自动化所 & 中国科学院大学**:
- ConRFT (RSS 2025) - 强化学习微调

**理想汽车**:
- VLA司机大模型 (2025) - 自动驾驶应用

---

**文档创建时间**: 2026-02-13
**最后更新**: 2026-02-15
**基于**: 15篇VLA核心论文（8篇经典 + 7篇前沿）的官方网址搜索
**目的**: 提供完整的VLA学习资源链接