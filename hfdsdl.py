import os
from datasets import load_dataset

# ==================== 核心配置（修改这两个参数）====================
# 1. 指定你要保存数据集的WSL绝对路径（替换为自己的路径）
TARGET_DIR = "yidongdata"  # 示例：WSL本地目录
# TARGET_DIR = "/mnt/d/medical_dataset"  # 示例：保存到Windows D盘（WSL挂载路径）

# 2. 设置Hugging Face镜像站（清华镜像，稳定可用）
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# ==================== 下载并保存数据集 ====================
# 确保目标目录存在
os.makedirs(TARGET_DIR, exist_ok=True)

try:
    # 从镜像站加载数据集（trust_remote_code适配自定义代码的数据集）
    dataset = load_dataset("joackimagno/filtered-filipino-recipes", "pretrain",trust_remote_code=True)

    # 保存到指定目录
    dataset.save_to_disk(TARGET_DIR)

    print(f"✅ 数据集已通过镜像站成功保存到：{TARGET_DIR}")
    # 可选：打印数据集信息验证
    print("\n📊 数据集结构：")
    print(dataset)
except Exception as e:
    print(f"❌ 下载失败：{e}")