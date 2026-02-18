# Open X-Embodiment 模拟仓库

这个目录模拟了Open X-Embodiment GitHub仓库的基本结构，用于演示数据集的使用方法。

## 目录结构

```
open_x_embodiment/
├── README.md                # 项目说明
├── requirements.txt         # 依赖文件
├── data_loaders/            # 数据加载器
│   └── oxe_loader.py        # OXE数据集加载器
├── examples/                # 示例代码
│   └── load_oxe_data.py     # 加载OXE数据示例
├── scripts/                 # 脚本文件
│   └── download_dataset.py  # 数据集下载脚本
└── utils/                   # 工具函数
    └── data_utils.py        # 数据处理工具
```

## 核心文件说明

### 1. requirements.txt
```
numpy
opencv-python
pillow
matplotlib
jupyter
```

### 2. data_loaders/oxe_loader.py
```python
import os
import json
import numpy as np
from PIL import Image

class OXELoader:
    """Open X-Embodiment数据集加载器"""
    
    def __init__(self, dataset_path):
        """初始化加载器"""
        self.dataset_path = dataset_path
        self.dataset_metadata = self._load_dataset_metadata()
        self.episodes = self._list_episodes()
    
    def _load_dataset_metadata(self):
        """加载数据集元数据"""
        metadata_path = os.path.join(self.dataset_path, "dataset_metadata.json")
        if not os.path.exists(metadata_path):
            return {}
        
        with open(metadata_path, 'r') as f:
            return json.load(f)
    
    def _list_episodes(self):
        """列出所有episodes"""
        episodes_dir = os.path.join(self.dataset_path, "episodes")
        if not os.path.exists(episodes_dir):
            return []
        
        episodes = []
        for item in os.listdir(episodes_dir):
            item_path = os.path.join(episodes_dir, item)
            if os.path.isdir(item_path):
                episodes.append(item)
        return episodes
    
    def load_episode(self, episode_id):
        """加载指定episode"""
        episode_dir = os.path.join(self.dataset_path, "episodes", episode_id)
        if not os.path.exists(episode_dir):
            return None
        
        # 加载元数据
        metadata_path = os.path.join(episode_dir, "episode_metadata.json")
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
        else:
            metadata = {}
        
        # 加载观测数据
        observations = []
        obs_dir = os.path.join(episode_dir, "observations")
        if os.path.exists(obs_dir):
            for img_file in sorted(os.listdir(obs_dir)):
                if img_file.endswith('.jpg'):
                    img_path = os.path.join(obs_dir, img_file)
                    try:
                        img = Image.open(img_path)
                        observations.append(np.array(img))
                    except:
                        pass
        
        # 加载动作数据
        actions = []
        action_dir = os.path.join(episode_dir, "actions")
        if os.path.exists(action_dir):
            for action_file in sorted(os.listdir(action_dir)):
                if action_file.endswith('.npy'):
                    action_path = os.path.join(action_dir, action_file)
                    try:
                        action = np.load(action_path)
                        actions.append(action)
                    except:
                        pass
        
        return {
            'metadata': metadata,
            'observations': observations,
            'actions': actions
        }
    
    def load_batch(self, episode_ids, batch_size=8):
        """加载批量数据"""
        batch_data = []
        for episode_id in episode_ids[:batch_size]:
            episode_data = self.load_episode(episode_id)
            if episode_data:
                batch_data.append(episode_data)
        return batch_data
    
    def get_statistics(self):
        """获取数据集统计信息"""
        stats = {
            'total_episodes': len(self.episodes),
            'dataset_metadata': self.dataset_metadata
        }
        
        if self.episodes:
            # 分析第一个episode
            first_episode = self.load_episode(self.episodes[0])
            if first_episode:
                stats['first_episode_stats'] = {
                    'num_observations': len(first_episode['observations']),
                    'num_actions': len(first_episode['actions']),
                    'action_dim': len(first_episode['actions'][0]) if first_episode['actions'] else 0
                }
        
        return stats
```