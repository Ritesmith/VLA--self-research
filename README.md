# VLA (Vision-Language-Action) Research

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-VLA-blue.svg)](https://arxiv.org/list/cs.RO/recent)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)

> 深入研究Vision-Language-Action模型及其在智能机器人领域的应用

## 📖 About This Project

This repository contains my research notes, code analysis, and implementation plans for **Vision-Language-Action (VLA)** models. VLA is an emerging paradigm that integrates large vision-language models into robotic control, enabling robots to understand natural language instructions and perform complex manipulation tasks.

### Research Focus
- **VLA Model Analysis**: Deep dive into state-of-the-art VLA architectures (RT-1/2, OpenVLA, Pi_0, etc.)
- **Embodied AI**: Explore how VLA models can interact with real-world environments
- **Reinforcement Learning Fine-tuning**: Investigate iRe-VLA and other RL-based improvement methods
- **Application Development**: Integrate VLA into autonomous vehicles and robotic systems

---

## 🎯 Research Objectives

### Core Goals
1. ✅ **Comprehensive Literature Review**: Study 15+ seminal VLA papers
2. ✅ **Technical Analysis**: Understand key architectural innovations
3. 🚧 **Code Implementation**: Develop practical VLA-based systems
4. 📋 **Thesis Project**: Integrate VLA into autonomous vehicle control

### Target Applications
- **Autonomous Vehicles**: VLA for perception-decision integration
- **Robotic Manipulation**: General-purpose robot control systems
- **Embodied AI**: Agents that learn through environment interaction

---

## 📚 Research Papers

### Core Papers (8 papers)
| Paper | Year | Venue | Status |
|-------|------|-------|--------|
| [RT-1](https://arxiv.org/abs/2212.06817) | 2022 | Google | ✅ Completed |
| [RT-2](https://arxiv.org/abs/2307.15818) | 2023 | Google | ✅ Completed |
| [RT-X](https://arxiv.org/abs/2310.08864) | 2023 | Google DeepMind | ✅ Completed |
| [RT-H](https://arxiv.org/abs/2403.01823) | 2024 | Google DeepMind | ✅ Completed |
| [PaLM-E](https://arxiv.org/abs/2303.03378) | 2023 | Google | ✅ Completed |
| [OpenVLA](https://arxiv.org/abs/2406.09246) | 2024 | OpenVLA | ✅ Completed |
| [RDT-1B](https://arxiv.org/abs/2410.07864) | 2024 | Tsinghua | ✅ Completed |
| [Pi_0](https://docs.physicalintelligence.company/) | 2025 | Physical Intelligence | ✅ Completed |

### Frontier Research (7 papers)
| Paper | Year | Venue | Focus |
|-------|------|-------|-------|
| [iRe-VLA](https://arxiv.org/abs/2501.16664) | 2025 | ICRA 2025 | Stable RL fine-tuning |
| [HoloBrain-0](https://arxiv.org/abs/2602.12062) | 2025 | Horizon Robotics | Embodied priors |
| [FiS-VLA](https://arxiv.org/abs/2506.01953) | 2025 | - | Fast-slow dual system |
| [ConRFT](https://arxiv.org/abs/2502.05450) | 2025 | RSS 2025 | Consistency policy RL |
| [Gemini Robotics](https://arxiv.org/abs/2503.20020) | 2025 | Google DeepMind | Gemini 2.0 integration |
| [ATM](https://arxiv.org/abs/2401.00025) | 2024 | RSS 2024 | Trajectory modeling |
| [DecisionNCE](https://arxiv.org/abs/2402.18137) | 2024 | - | Trajectory grounding |

---

## 🏗️ Repository Structure

```
VLA--self-research/
├── 📄 README.md                      # This file
├── 📄 学习进度.md                    # Learning progress tracker
├── 📄 VLA深度学习方向规划.md          # Research roadmap
├── 📄 VLA论文官方网址汇总.md          # Paper resources
│
├── 📂 核心概念/                      # Fundamental concepts
│   └── VLA核心概念.md
│
├── 📂 PDFs/                          # Paper PDFs (organized by paper)
│   ├── RT-1_2022/
│   ├── RT-2_2023.7/
│   ├── OpenVLA_2024.6/
│   ├── iRe-VLA_ICRA2025/
│   └── ...
│
├── 📂 第五天前沿技术深入研究/          # In-depth technical analysis
│   ├── HoloBrain-0/
│   │   ├── HoloBrain-0论文总结.md
│   │   ├── HoloBrain-0技术分析报告.md
│   │   └── HoloBrain-0代码分析.ipynb
│   └── iRe-VLA/
│       ├── iRe-VLA论文总结.md
│       └── iRe-VLA技术分析报告.md
│
├── 📂 技术栈/                        # Technical implementation
│   └── VLA技术栈学习报告.aux
│
├── 📂 毕设计划/                      # Thesis project plan
│   └── 毕设VLA集成计划.md
│
└── 📂 scripts/                       # Utility scripts
    ├── ocr_holobrain.py
    ├── ocr_irevla.py
    └── ocr_pdfs_corrected.py
```

---

## 🔬 Technical Highlights

### HoloBrain-0 (2025)
- **Key Innovation**: Explicit embodied prior injection
- **Components**: 
  - Spatial Enhancer (camera parameter fusion)
  - Embodiment-aware Action Expert (kinematics-aware)
  - SimpleRTC (real-time trajectory smoothing)
- **Performance**: +41.51% success rate on real-world tasks (0.2B model)
- **Application**: 3D spatial perception for autonomous vehicles

### iRe-VLA (2025)
- **Key Innovation**: Stable RL fine-tuning for large VLA models
- **Solutions**:
  - Stabilizer mechanism for training stability
  - Efficient RL strategies for reduced computation
  - Knowledge preservation to prevent catastrophic forgetting
- **Application**: Self-improving VLA models in real-world environments

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- PyTorch 2.0+
- Jupyter Notebook
- Required libraries (see requirements.txt)

### Installation
```bash
git clone https://github.com/yourusername/VLA-research.git
cd VLA-research
pip install -r requirements.txt
```

### Quick Start
1. **Read Paper Summaries**: Start with `第五天前沿技术深入研究/`
2. **Explore Code Analysis**: Open `.ipynb` notebooks for technical deep dive
3. **Check Progress**: Review `学习进度.md` for current status

---

## 📊 Research Progress

### Completed ✅
- [x] Literature review of 15+ VLA papers
- [x] Technical analysis of core VLA architectures
- [x] OCR extraction and summarization of all papers
- [x] Code analysis notebooks for key models
- [x] Research roadmap and implementation plan

### In Progress 🚧
- [ ] Deep code analysis of HoloBrain-0 and iRe-VLA
- [ ] Technical comparison report
- [ ] Thesis project design
- [ ] Prototype implementation

### Planned 📋
- [ ] VLA model fine-tuning on custom datasets
- [ ] Integration with autonomous vehicle platform
- [ ] Real-world testing and evaluation
- [ ] Thesis completion

---

## 🎓 Thesis Project

### Project Title
**Integrating Vision-Language-Action Models into Autonomous Vehicle Control Systems**

### Objectives
1. Design a lightweight VLA architecture for real-time vehicle control
2. Implement VLA-based perception-decision integration
3. Develop stable RL fine-tuning pipeline (inspired by iRe-VLA)
4. Evaluate on WheelTec autonomous vehicle platform

### Expected Outcomes
- 15-25% improvement in 3D spatial perception
- 30-50% improvement in training stability
- 50-70% reduction in cross-vehicle adaptation costs

---

## 🤝 Contributing

This is a personal research repository. However, I welcome:
- Bug reports and fixes
- Suggestions for additional papers to review
- Collaboration opportunities

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **OpenVLA Team** for open-sourcing their VLA architecture
- **Google DeepMind** for pioneering RT series and VLA research
- **Horizon Robotics** for open-sourcing HoloBrain-0
- **Physical Intelligence** for Pi_0 research

---

## 📞 Contact

- **Name**: [Your Name]
- **Email**: [your.email@example.com]
- **GitHub**: [@yourusername](https://github.com/yourusername)

---

## 📖 References

### Key Resources
- [OpenVLA](https://github.com/openvla/openvla) - Open-source VLA implementation
- [OpenX-Embodiment](https://github.com/google-research/open_x-embodiment) - Open-source robotics dataset
- [RT-1/RT-X](https://github.com/google-research/robotics_transformer) - Robotics Transformer papers

### Recommended Reading
- [RT-2: Vision-Language-Action Models](https://arxiv.org/abs/2307.15818) - VLA foundation
- [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) - Open-source implementation
- [HoloBrain-0: Full-Stack VLA Framework](https://arxiv.org/abs/2602.12062) - Embodied priors

---

**⭐ If you find this research helpful, please consider giving it a star!**

---

*Last Updated: February 2026*
