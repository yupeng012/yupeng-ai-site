#!/usr/bin/env python3
"""
知识检索系统
实现知识的搜索、检索和推荐
"""

import json
import os
from datetime import datetime
from pathlib import Path
import re
from collections import defaultdict

class KnowledgeRetrievalSystem:
    """知识检索系统"""

    def __init__(self, workspace_root):
        self.workspace_root = Path(workspace_root)
        self.knowledge_base = self.workspace_root / "knowledge_base"
        self.knowledge_index = self.workspace_root / "knowledge_index.json"
        self.agents = self._load_agents()
        self._build_index()

    def _load_agents(self):
        """加载所有智能体"""
        agents = {}
        agent_dirs = [
            ("main", "🐟", "小鱼儿"),
            ("stock", "📊", "股票分析师"),
            ("fundamental", "📈", "基本面分析师"),
            ("monitor", "👁️", "监控员"),
            ("reporter", "📝", "报告员"),
            ("learner", "🧠", "学习助手"),
            ("decision", "🎯", "决策助手"),
            ("risk", "⚠️", "风险管理员"),
            ("notifier", "🔔", "通知员")
        ]

        for agent_id, emoji, name in agent_dirs:
            agent_path = self.workspace_root / agent_id
            experience_file = agent_path / "experience.json"

            if experience_file.exists():
                with open(experience_file, 'r', encoding='utf-8') as f:
                    agent_data = json.load(f)
                    agents[agent_id] = {
                        **agent_data,
                        "emoji": emoji,
                        "name": name
                    }

        return agents

    def _build_index(self):
        """构建知识索引"""
        print("🔍 构建知识索引...")

        index = {
            "by_category": defaultdict(list),
            "by_agent": defaultdict(list),
            "by_tag": defaultdict(list),
            "by_keyword": defaultdict(list),
            "full_text": []
        }

        # 遍历所有知识文件
        for category_path in self.knowledge_base.iterdir():
            if category_path.is_dir():
                category = category_path.name

                for file in category_path.glob("*.md"):
                    knowledge = self._parse_knowledge_file(file)

                    # 按分类索引
                    index["by_category"][category].append(knowledge)

                    # 按智能体索引
                    if knowledge["agent_id"]:
                        index["by_agent"][knowledge["agent_id"]].append(knowledge)

                    # 按标签索引
                    for tag in knowledge["tags"]:
                        index["by_tag"][tag].append(knowledge)

                    # 按关键词索引
                    keywords = self._extract_keywords(knowledge["content"])
                    for keyword in keywords:
                        index["by_keyword"][keyword].append(knowledge)

                    # 全文索引
                    index["full_text"].append(knowledge)

        # 保存索引
        with open(self.knowledge_index, 'w', encoding='utf-8') as f:
            json.dump(index, f, ensure_ascii=False, indent=2, default=list)

        print(f"✅ 知识索引构建完成")
        print(f"   分类: {len(index['by_category'])}")
        print(f"   智能体: {len(index['by_agent'])}")
        print(f"   标签: {len(index['by_tag'])}")
        print(f"   关键词: {len(index['by_keyword'])}")
        print(f"   总知识: {len(index['full_text'])}")

    def _parse_knowledge_file(self, file_path):
        """解析知识文件"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 提取基本信息
        lines = content.split('\n')
        
        # 查找标题
        title = "未知标题"
        for line in lines:
            if line.startswith('#'):
                title = line.replace('#', '').strip()
                break
        
        # 查找作者
        author = "未知作者"
        for line in lines:
            if '**作者**:' in line or '作者:' in line:
                author = line.split(':')[-1].strip()
                break
        
        # 查找时间
        time_str = "未知时间"
        for line in lines:
            if '**时间**:' in line or '时间:' in line:
                time_str = line.split(':')[-1].strip()
                break
        
        # 查找分类
        category = "未分类"
        for line in lines:
            if '**分类**:' in line or '分类:' in line:
                category = line.split(':')[-1].strip()
                break
        
        # 查找标签
        tags_str = "无"
        for line in lines:
            if '**标签**:' in line or '标签:' in line:
                tags_str = line.split(':')[-1].strip()
                break
        
        tags = [tag.strip() for tag in tags_str.split(',') if tag.strip() and tag.strip() != '无']

        # 提取智能体ID
        agent_id = None
        for aid, agent in self.agents.items():
            if agent['name'] in author:
                agent_id = aid
                break

        return {
            'title': title,
            'author': author,
            'time': time_str,
            'category': category,
            'tags': tags,
            'content': content,
            'file_path': str(file_path),
            'agent_id': agent_id
        }

    def _extract_keywords(self, content):
        """提取关键词"""
        # 移除markdown标记
        content = re.sub(r'[#*`_\[\]]', ' ', content)

        # 分词
        words = content.split()

        # 过滤停用词和短词
        stop_words = {'的', '了', '是', '在', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很', '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这'}
        keywords = [word for word in words if len(word) > 1 and word not in stop_words]

        return keywords

    def search(self, query, search_type="full_text"):
        """搜索知识"""
        print(f"\n🔍 搜索: {query}")
        print(f"   搜索类型: {search_type}")

        # 加载索引
        if not self.knowledge_index.exists():
            self._build_index()

        with open(self.knowledge_index, 'r', encoding='utf-8') as f:
            index = json.load(f)

        results = []

        if search_type == "full_text":
            # 全文搜索
            query_lower = query.lower()
            for knowledge in index["full_text"]:
                if query_lower in knowledge["content"].lower():
                    results.append(knowledge)

        elif search_type == "category":
            # 分类搜索
            if query in index["by_category"]:
                results = index["by_category"][query]

        elif search_type == "agent":
            # 智能体搜索
            if query in index["by_agent"]:
                results = index["by_agent"][query]

        elif search_type == "tag":
            # 标签搜索
            if query in index["by_tag"]:
                results = index["by_tag"][query]

        elif search_type == "keyword":
            # 关键词搜索
            if query in index["by_keyword"]:
                results = index["by_keyword"][query]

        # 去重
        seen = set()
        unique_results = []
        for result in results:
            result_key = result['file_path']
            if result_key not in seen:
                seen.add(result_key)
                unique_results.append(result)

        # 显示结果
        print(f"\n📊 搜索结果: {len(unique_results)} 条")

        for i, result in enumerate(unique_results, 1):
            print(f"\n{i}. {result['title']}")
            print(f"   作者: {result['author']}")
            print(f"   分类: {result['category']}")
            print(f"   标签: {', '.join(result['tags'])}")
            print(f"   时间: {result['time']}")

        return unique_results

    def recommend(self, context, limit=5):
        """推荐知识"""
        print(f"\n💡 基于上下文推荐知识: {context}")

        # 加载索引
        if not self.knowledge_index.exists():
            self._build_index()

        with open(self.knowledge_index, 'r', encoding='utf-8') as f:
            index = json.load(f)

        # 提取上下文关键词
        context_keywords = self._extract_keywords(context)

        # 计算相关性
        scores = defaultdict(int)
        for keyword in context_keywords:
            if keyword in index["by_keyword"]:
                for knowledge in index["by_keyword"][keyword]:
                    scores[knowledge['file_path']] += 1

        # 排序
        sorted_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        # 获取推荐结果
        recommendations = []
        seen = set()
        for file_path, score in sorted_results[:limit]:
            for knowledge in index["full_text"]:
                if knowledge['file_path'] == file_path and file_path not in seen:
                    seen.add(file_path)
                    knowledge['relevance_score'] = score
                    recommendations.append(knowledge)
                    break

        # 显示推荐结果
        print(f"\n📊 推荐结果: {len(recommendations)} 条")

        for i, result in enumerate(recommendations, 1):
            print(f"\n{i}. {result['title']} (相关度: {result['relevance_score']})")
            print(f"   作者: {result['author']}")
            print(f"   分类: {result['category']}")
            print(f"   标签: {', '.join(result['tags'])}")

        return recommendations

    def get_related_knowledge(self, knowledge_file_path):
        """获取相关知识"""
        print(f"\n🔗 查找相关知识: {knowledge_file_path}")

        # 加载索引
        if not self.knowledge_index.exists():
            self._build_index()

        with open(self.knowledge_index, 'r', encoding='utf-8') as f:
            index = json.load(f)

        # 找到目标知识
        target_knowledge = None
        for knowledge in index["full_text"]:
            if knowledge['file_path'] == knowledge_file_path:
                target_knowledge = knowledge
                break

        if not target_knowledge:
            print("❌ 未找到目标知识")
            return []

        # 基于分类、标签、智能体查找相关知识
        related = set()

        # 同分类的知识
        category = target_knowledge['category']
        if category in index["by_category"]:
            for knowledge in index["by_category"][category]:
                if knowledge['file_path'] != knowledge_file_path:
                    related.add(knowledge['file_path'])

        # 同标签的知识
        for tag in target_knowledge['tags']:
            if tag in index["by_tag"]:
                for knowledge in index["by_tag"][tag]:
                    if knowledge['file_path'] != knowledge_file_path:
                        related.add(knowledge['file_path'])

        # 同智能体的知识
        if target_knowledge['agent_id']:
            agent_id = target_knowledge['agent_id']
            if agent_id in index["by_agent"]:
                for knowledge in index["by_agent"][agent_id]:
                    if knowledge['file_path'] != knowledge_file_path:
                        related.add(knowledge['file_path'])

        # 获取相关知识详情
        related_knowledge = []
        for knowledge in index["full_text"]:
            if knowledge['file_path'] in related:
                related_knowledge.append(knowledge)

        # 显示相关知识
        print(f"\n📊 相关知识: {len(related_knowledge)} 条")

        for i, result in enumerate(related_knowledge, 1):
            print(f"\n{i}. {result['title']}")
            print(f"   作者: {result['author']}")
            print(f"   分类: {result['category']}")
            print(f"   标签: {', '.join(result['tags'])}")

        return related_knowledge

    def show_statistics(self):
        """显示知识统计"""
        print("\n" + "=" * 60)
        print("📊 知识库统计")
        print("=" * 60)

        # 加载索引
        if not self.knowledge_index.exists():
            self._build_index()

        with open(self.knowledge_index, 'r', encoding='utf-8') as f:
            index = json.load(f)

        # 统计信息
        print(f"\n📁 分类统计:")
        for category, knowledges in index["by_category"].items():
            print(f"   {category}: {len(knowledges)} 个知识点")

        print(f"\n🤖 智能体统计:")
        for agent_id, knowledges in index["by_agent"].items():
            agent = self.agents.get(agent_id, {})
            print(f"   {agent.get('name', agent_id)}: {len(knowledges)} 个知识点")

        print(f"\n🏷️ 标签统计:")
        for tag, knowledges in index["by_tag"].items():
            print(f"   {tag}: {len(knowledges)} 个知识点")

        print(f"\n🔤 关键词统计:")
        print(f"   总关键词数: {len(index['by_keyword'])}")

        print(f"\n📚 总知识数: {len(index['full_text'])}")

def main():
    """主函数"""
    workspace_root = os.path.expanduser("~/.openclaw/workspace")

    # 创建知识检索系统
    retrieval_system = KnowledgeRetrievalSystem(workspace_root)

    # 显示统计
    retrieval_system.show_statistics()

    # 测试搜索
    print("\n" + "=" * 60)
    print("🔍 测试知识搜索")
    print("=" * 60)

    # 全文搜索
    retrieval_system.search("Python", "full_text")

    # 分类搜索
    retrieval_system.search("stock_analysis", "category")

    # 标签搜索
    retrieval_system.search("OpenClaw", "tag")

    # 测试推荐
    print("\n" + "=" * 60)
    print("💡 测试知识推荐")
    print("=" * 60)

    retrieval_system.recommend("如何优化股票分析系统", limit=3)

    # 测试相关知识
    print("\n" + "=" * 60)
    print("🔗 测试相关知识")
    print("=" * 60)

    # 获取第一个知识的相关知识
    if retrieval_system.knowledge_base.exists():
        first_category = list(retrieval_system.knowledge_base.iterdir())[0]
        first_file = list(first_category.glob("*.md"))[0]
        retrieval_system.get_related_knowledge(str(first_file))

    print("\n" + "=" * 60)
    print("✅ 知识检索系统测试完成")
    print("=" * 60)

if __name__ == "__main__":
    main()
