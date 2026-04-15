from datasets import load_dataset
# 对应语料数据加载
# 请参考： 下面表格中的标签字段字段内容
# 如：序号1，arXiv文献的文本。，标签字典：academic_paper
dataset_arxiv = load_dataset("liwu/MNBVC", 'qa_mfa', split='train', streaming=False,cache_dir="data/wjb")