import json
import os

# 你的数据集目录，和你的训练脚本一致
data_dir = "./data/finetune"
files = [f for f in os.listdir(data_dir) if f.endswith(".jsonl")]

for file_name in files:
    file_path = os.path.join(data_dir, file_name)
    new_lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            # 只保留 conversations 字段，删除所有其他多余字段（包括id）
            if "conversations" in data:
                clean_data = {"conversations": data["conversations"]}
                new_lines.append(json.dumps(clean_data, ensure_ascii=False))
    # 覆盖原文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))
    print(f"✅ 处理完成：{file_name}，已清理多余字段")