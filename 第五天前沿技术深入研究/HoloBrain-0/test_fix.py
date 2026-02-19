import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from dataclasses import dataclass

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
    
    def predict_depth(self, vision_features: torch.Tensor) -> tuple:
        depth_logits = self.depth_predictor(vision_features)
        depth_dist = F.softmax(depth_logits, dim=-1)
        
        depth_values = torch.linspace(0.1, self.max_depth, self.num_depth_bins, device=vision_features.device)
        expected_depth = torch.sum(depth_dist * depth_values[None, None, :], dim=-1)
        
        return depth_dist, expected_depth
    
    def forward(self, vision_features: torch.Tensor, camera_params_list: list) -> torch.Tensor:
        B, N, _ = vision_features.shape
        
        camera_embeddings = []
        for params in camera_params_list:
            emb = self.encode_camera_params(params)
            camera_embeddings.append(emb)
        
        camera_embeddings = torch.stack(camera_embeddings, dim=0)
        camera_embeddings = camera_embeddings.unsqueeze(1).expand(-1, N, -1)
        # 投影到视觉特征维度
        camera_embeddings = nn.Linear(self.hidden_dim, self.vision_dim)(camera_embeddings)
        
        depth_dist, expected_depth = self.predict_depth(vision_features)
        depth_embeddings = self.depth_predictor[:-1](vision_features)
        
        enhanced_features, _ = self.spatial_fusion(
            query=camera_embeddings,
            key=vision_features,
            value=vision_features
        )
        
        output = self.output_proj(enhanced_features)
        return output

# 测试
print("🔧 测试Spatial Enhancer...")

spatial_enhancer = SpatialEnhancer(
    vision_dim=768,
    hidden_dim=512,
    num_depth_bins=64,
    max_depth=10.0
)

# 创建测试输入
batch_size = 2
num_patches = 196
vision_features = torch.randn(batch_size, num_patches, 768)

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

print(f"✅ 输入形状: {vision_features.shape}")
print(f"✅ 输出形状: {enhanced_features.shape}")
print(f"✅ 模型参数量: {sum(p.numel() for p in spatial_enhancer.parameters()):,}")
print("🎉 测试成功！")
