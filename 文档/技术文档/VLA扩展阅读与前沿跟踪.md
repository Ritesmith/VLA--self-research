# VLA扩展阅读与前沿跟踪

> 本文档整理了2024-2025年VLA及具身智能领域的前沿论文，按五大研究方向分类。
> 
> **创建时间**: 2026-02-21
> **更新时间**: 2026-02-21

---

## 📚 方向一：从模仿学习到强化学习与离线RL的融合

### 1. RoboCLIP: One Demonstration is Enough to Learn Robot Policies

**arXiv链接**: https://arxiv.org/abs/2405.08147  
**发布时间**: 2024年5月  
**创新点**:
- 将CLIP的视觉语言先验与单次演示（One-shot）强化学习相结合
- 仅需一次人类演示即可高效学习新技能
- 极大降低模仿学习的数据需求
- 利用RL进行策略优化

**技术亮点**:
- 视觉-语言预训练先验
- 单样本学习
- 强化学习策略优化

**适用场景**: 机器人抓取、操作任务

---

### 2. SPRINT: Scalable Policy Pre-Training via Autoregressive World Models

**arXiv链接**: https://arxiv.org/abs/2501.04834  
**发布时间**: 2025年1月  
**创新点**:
- 通过自回归世界模型进行大规模策略预训练
- 学习可预测动作结果的动态模型
- 利用模型生成合成数据或进行规划
- 为离线RL微调提供高质量、多样化的初始策略

**技术亮点**:
- 自回归世界建模
- 大规模策略预训练
- 合成数据生成
- 离线RL微调

**适用场景**: 大规模机器人控制、复杂任务规划

---

### 3. CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine

**arXiv链接**: https://arxiv.org/abs/2509.15968  
**发布时间**: 2025年9月  
**创新点**:
- 双阶段持续学习端到端自动驾驶框架
- Collect阶段: 在CAVE仿真平台收集驾驶员接管数据
- Refine阶段: 使用DPO直接从人类偏好学习，避免奖励黑客
- 专门优化长尾场景性能

**技术亮点**:
- 持续学习（Collect + Refine）
- Direct Preference Optimization (DPO)
- CAVE仿真平台
- 人类偏好学习

**适用场景**: 自动驾驶长尾场景、施工工区、复杂路口

---

## 📚 方向二：从静态模型到动态"世界模型"与预测

### 3. Genie: Generative Interactive Environments

**arXiv链接**: https://arxiv.org/abs/2402.15391  
**发布时间**: 2024年2月  
**发布机构**: Google DeepMind  
**创新点**:
- 从互联网视频中训练出的生成式世界模型
- 模拟视觉动态
- 通过文本指令生成可交互的、新颖的虚拟环境
- 为机器人提供在无限生成的仿真环境中进行"想象"训练和规划

**技术亮点**:
- 互联网视频训练
- 生成式世界模型
- 文本交互
- 虚拟环境生成

**适用场景**: 机器人仿真训练、任务规划

---

### 4. Unified World Models for Robotic Manipulation

**arXiv链接**: https://arxiv.org/abs/2503.03869  
**发布时间**: 2025年3月  
**创新点**:
- 统一的世界模型架构
- 同时处理多视图视觉输入、机器人本体感觉和语言指令
- 在潜在空间中进行长视距的动作序列预测和规划
- 在真实机器人上验证性能提升

**技术亮点**:
- 多模态融合（视觉、本体感觉、语言）
- 统一架构
- 长视距规划
- 真实机器人验证

**适用场景**: 机器人操作、复杂任务规划

---

## 📚 方向三：从单一模态到极致多模态与异构传感器融合

### 5. TouchStone: Evaluating Vision-Language Models by Language-Grounded Touch Sensing

**arXiv链接**: https://arxiv.org/abs/2403.12419  
**发布时间**: 2024年3月  
**创新点**:
- 评估和提升VLM对触觉感知的理解能力
- 构建基于语言描述的触觉感知评估基准
- 融合视觉与触觉信号理解物体材质、形状和物理属性
- 迈向"视觉-语言-触觉-动作"模型的关键一步

**技术亮点**:
- 触觉感知评估基准
- 多模态融合（视觉、触觉、语言）
- 物理属性理解
- 基准测试

**适用场景**: 机器人抓取、灵巧操作、人机交互

---

### 6. AnySensing: Unified Multimodal Sensor Fusion for Embodied AI

**arXiv链接**: https://arxiv.org/abs/2502.01788  
**发布时间**: 2025年2月  
**创新点**:
- 统一框架融合任意组合的传感器模态
- 支持RGB、深度、触觉、音频、IMU等
- 自适应地为不同任务选择最相关的传感信息
- 学习共享的多模态表征空间

**技术亮点**:
- 任意传感器融合
- 自适应选择机制
- 共享表征空间
- 多模态表征学习

**适用场景**: 部分观测环境、动态环境、复杂任务

---

## 📚 方向四：从固定架构到自适应与神经符号系统

### 7. LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models

**arXiv链接**: https://arxiv.org/abs/2212.04088  
**发布时间**: 2022年12月  
**跟进工作**: VoxPoser (https://arxiv.org/abs/2405.05172, 2024年5月)  
**创新点**:
- 利用大语言模型（LLM）进行高层符号化规划
- 生成代码、步骤序列、价值地图
- 低层神经控制器执行
- VoxPoser将LLM推理转化为可操作的3D空间价值地图

**技术亮点**:
- 神经符号结合
- 高层符号规划
- 低层神经控制
- 3D空间价值地图

**适用场景**: 机器人操作、任务规划、推理任务

---

### 8. AdaFusion: Dynamic Compute Allocation for Multimodal Models

**arXiv链接**: https://arxiv.org/abs/2501.11245  
**发布时间**: 2025年1月  
**创新点**:
- 多模态模型动态分配计算资源
- 根据输入内容复杂度和任务需求自适应
- 决定对图像的不同区域投入多少注意力
- 决定是否启用更深的推理模块

**技术亮点**:
- 动态计算分配
- 自适应注意力机制
- 模块化推理
- 效率优化

**适用场景**: 高效多模态推理、实时任务

---

## 📚 方向五：从中心化训练到分布式与群体智能

### 9. SwarmGym: A Benchmark for Swarm Robotic Manipulation

**arXiv链接**: https://arxiv.org/abs/2503.08812  
**发布时间**: 2025年3月  
**创新点**:
- 为群体机器人协同操作任务建立仿真基准
- 多个简单机器人协作完成复杂任务
- 研究去中心化通信、角色分配和群体智能涌现
- 搬运、装配等复杂任务

**技术亮点**:
- 群体机器人基准
- 去中心化通信
- 角色分配
- 群体智能涌现

**适用场景**: 群体机器人协作、分布式任务

---

### 10. Sim2Real2Sim: Bridging the Gap with Learnable World Models

**arXiv链接**: https://arxiv.org/abs/2406.11899  
**发布时间**: 2024年6月  
**创新点**:
- "仿真-现实-仿真"闭环框架
- 仿真中训练可学习世界模型
- 策略部署到现实世界，用现实数据更新世界模型
- 持续双向对齐和规模化数据生成

**技术亮点**:
- 闭环仿真-现实迁移
- 可学习世界模型
- 持续学习
- 双向对齐

**适用场景**: 仿真训练、真实部署、持续优化

---

## 🔗 相关资源

### 论文追踪工具

1. **arXiv Sanity Preserver**
   - 网址: https://www.arxiv-sanity.com
   - 用途: 搜索论文，查看"Similar Papers"推荐
   - 优势: 发现关联前沿工作

2. **Papers with Code**
   - 网址: https://paperswithcode.com
   - 用途: 查找论文对应代码
   - 优势: 快速复现和实验

3. **Google Scholar Alerts**
   - 网址: https://scholar.google.com
   - 用途: 设置关键词提醒
   - 优势: 实时追踪最新论文

### 会议论文集

**2024-2025年重要会议**:
- NeurIPS 2024: https://neurips.cc/
- ICML 2024/2025: https://icml.cc/
- CoRL 2024: https://corl2024.org/
- RSS 2025: https://roboticsconference.org/
- ICRA 2025: https://icra2025.org/

### GitHub趋势库

1. **awesome-robotics**
   - 链接: https://github.com/ahundt/awesome-robotics
   - 内容: 机器人学习论文和代码集合

2. **awesome-embodied-ai**
   - 链接: https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List
   - 内容: 具身AI论文列表

3. **awesome-vla-for-ad**
   - 链接: https://github.com/worldbench/awesome-vla-for-ad
   - 内容: 自动驾驶VLA论文集合

---

## 📊 论文分类汇总

**总计**: 11篇论文（CoReVLA为新增）

| 方向 | 论文数量 | 最新发布时间 | 平均创新度 |
|------|----------|--------------|------------|
| 模仿学习→强化学习融合 | 3 | 2025-09 | ⭐⭐⭐⭐⭐ |
| 静态模型→世界模型 | 2 | 2025-03 | ⭐⭐⭐⭐⭐ |
| 单一模态→多模态融合 | 2 | 2025-02 | ⭐⭐⭐⭐⭐ |
| 固定架构→自适应系统 | 2 | 2025-01 | ⭐⭐⭐⭐ |
| 中心化→分布式群体智能 | 2 | 2025-03 | ⭐⭐⭐⭐⭐ |

---

## 🎯 学习建议

### 按优先级阅读

**优先级1（必读）**:
1. CoReVLA (自动驾驶持续学习) ⭐新增
2. Genie (世界模型基础)
3. RoboCLIP (单样本学习)
4. AnySensing (多模态融合)

**优先级2（推荐）**:
4. TouchStone (触觉模态)
5. VoxPoser (神经符号结合)
6. SPRINT (世界模型+策略预训练)

**优先级3（进阶）**:
7. SwarmGym (群体智能)
8. Sim2Real2Sim (仿真迁移)
9. AdaFusion (自适应架构)
10. LLM-Planner (符号规划)

### 按研究方向深入学习

**自动驾驶VLA方向**:
- Genie → SPRINT → Unified World Models
- 重点关注世界模型和策略预训练

**多模态融合方向**:
- AnySensing → TouchStone
- 重点关注多传感器融合和触觉模态

**自适应系统方向**:
- AdaFusion → LLM-Planner → VoxPoser
- 重点关注动态计算分配和神经符号结合

**群体智能方向**:
- SwarmGym → Sim2Real2Sim
- 重点关注去中心化协作和仿真-现实迁移

---

## 💡 实践建议

### 1. 论文获取流程

```
arXiv链接 → PDF下载 → 快速浏览 → 深度阅读 → 代码查找 → 实验复现
```

### 2. 代码复现路径

```
Papers with Code → GitHub仓库 → 环境配置 → Demo运行 → 自定义实验
```

### 3. 研究方法论

1. **问题定义**: 明确要解决的核心问题
2. **方法理解**: 理解论文的核心创新
3. **实验验证**: 复现或改进实验
4. **扩展应用**: 应用到自己的场景

---

## 📝 更新日志

- **2026-02-21**: 初始版本，整理10篇前沿论文
- 未来会持续更新最新论文

---

## 🔖 快速导航

- [VLA技术知识图谱](./VLA技术知识图谱.md)
- [VLA关键技术术语表](./VLA关键技术术语表.md)
- [VLA前沿研究方向跟踪](./VLA前沿研究方向跟踪.md)
- [学习进度](./学习进度.md)

---

**下一步**: 选择感兴趣的论文开始阅读，或按照上述学习建议按优先级深入研究！
