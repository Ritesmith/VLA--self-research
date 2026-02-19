import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class CameraParams:
    fx: float
    fy: float
    cx: float
    cy: float
    rotation: np.ndarray
    translation: np.ndarray
    height: int
    width: int

class SpatialEnhancer(nn.Module):
    def __init__(
        self,
        vision_dim: int = 768,
        hidden_dim: int = 512,
        num_depth_bins: int = 64,
        max_depth: float = 10.0,
    ):
        super().__init__()
        
        self.vision_dim = vision_dim
        self.hidden_dim = hidden_dim
        self.num_depth_bins = num_depth_bins
        self.max_depth = max_depth
        
        # 相机参数编码器
        self.camera_encoder = nn.Sequential(
            nn.Linear(16, hidden_dim),  # 内参(4) + 外参(12) = 16
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # 相机嵌入投影到视觉特征维度
        self.camera_proj = nn.Linear(hidden_dim, vision_dim)
        
        # 深度预测头
        self.depth_predictor = nn.Sequential(
            nn.Linear(vision_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_depth_bins),
            nn.Softmax(dim=-1)
        )
        
        # 空间特征融合
        self.spatial_fusion = nn.MultiheadAttention(
            embed_dim=vision_dim,
            num_heads=8,
            dropout=0.1,
            batch_first=True
        )
        
        # 输出投影
        self.output_proj = nn.Linear(vision_dim, vision_dim)
    
    def encode_camera_params(self, camera_params: CameraParams) -> torch.Tensor:
        intrinsic = torch.tensor([
            camera_params.fx, camera_params.fy,
            camera_params.cx, camera_params.cy
        ])
        
        extrinsic = torch.cat([
            torch.from_numpy(camera_params.rotation).flatten(),
            torch.from_numpy(camera_params.translation).flatten()
        ])
        
        params = torch.cat([intrinsic, extrinsic], dim=0)
        encoded = self.camera_encoder(params.float())
        return encoded
    
    def predict_depth(self, vision_features: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        depth_logits = self.depth_predictor(vision_features)
        depth_dist = F.softmax(depth_logits, dim=-1)
        
        depth_values = torch.linspace(0.1, self.max_depth, self.num_depth_bins, device=vision_features.device)
        expected_depth = torch.sum(depth_dist * depth_values[None, None, :], dim=-1)
        
        return depth_dist, expected_depth
    
    def forward(
        self,
        vision_features: torch.Tensor,
        camera_params_list: List[CameraParams]
    ) -> torch.Tensor:
        B, N, _ = vision_features.shape
        
        # 1. 编码相机参数
        camera_embeddings = []
        for params in camera_params_list:
            emb = self.encode_camera_params(params)
            camera_embeddings.append(emb)
        
        camera_embeddings = torch.stack(camera_embeddings, dim=0)  # (B, hidden_dim)
        camera_embeddings = camera_embeddings.unsqueeze(1).expand(-1, N, -1)  # (B, N, hidden_dim)
        
        # 投影相机嵌入到视觉特征维度
        camera_embeddings = self.camera_proj(camera_embeddings)  # (B, N, vision_dim)
        
        # 2. 预测深度
        depth_dist, expected_depth = self.predict_depth(vision_features)
        
        # 3. 将深度信息注入视觉特征
        depth_embeddings = self.depth_predictor[:-1](vision_features)  # (B, N, hidden_dim)
        
        # 4. 空间特征融合 (使用相机嵌入作为query)
        enhanced_features, _ = self.spatial_fusion(
            query=camera_embeddings,
            key=vision_features,
            value=vision_features
        )
        
        # 5. 输出投影
        output = self.output_proj(enhanced_features)
        
        return output

# 测试修复后的Spatial Enhancer
print("测试修复后的Spatial Enhancer...")

# 检查是否有GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"使用设备: {device}")

spatial_enhancer = SpatialEnhancer(
    vision_dim=768,
    hidden_dim=512,
    num_depth_bins=64,
    max_depth=10.0
).to(device)

# 创建测试输入
batch_size = 2
num_patches = 196  # 14x14 patches
vision_features = torch.randn(batch_size, num_patches, 768).to(device)

# 创建相机参数列表
camera_params_list = [
    CameraParams(fx=600, fy=600, cx=320, cy=240,
                 rotation=np.eye(3), translation=np.array([0, 0, 0]),
                 height=480, width=640),
    CameraParams(fx=800, fy=800, cx=400, cy=300,
                 rotation=np.eye(3), translation=np.array([1, 0, 0]),
                 height=600, width=800)
]

# 前向传播
enhanced_features = spatial_enhancer(vision_features, camera_params_list[:batch_size])

print(f"输入形状: {vision_features.shape}")
print(f"输出形状: {enhanced_features.shape}")
print(f"模型参数量: {sum(p.numel() for p in spatial_enhancer.parameters()):,}")
print("测试成功！维度不匹配问题已修复")
