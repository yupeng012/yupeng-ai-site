#!/usr/bin/env python3
"""
知识体系完善系统
完善知识管理体系，包括更新、版本管理、使用统计等
"""

import json
import os
from datetime import datetime
from pathlib import Path
import shutil
from collections import defaultdict

class KnowledgeManagementSystem:
    """知识管理体系系统"""

    def __init__(self, workspace_root):
        self.workspace_root = Path(workspace_root)
        self.knowledge_base = self.workspace_root / "knowledge_base"
        self.knowledge_versions = self.workspace_root / "knowledge_versions"
        self.knowledge_stats = self.workspace_root / "knowledge_stats.json"
        self.agents = self._load_agents()
        self._ensure_directories()

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

    def _ensure_directories(self):
        """确保目录存在"""
        if not self.knowledge_versions.exists():
            self.knowledge_versions.mkdir(parents=True, exist_ok=True)

    def update_knowledge(self, knowledge_file, new_content, updater, update_notes):
        """更新知识"""
        print(f"\n📝 更新知识: {knowledge_file}")

        # 创建版本备份
        version_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        version_dir = self.knowledge_versions / version_id
        version_dir.mkdir(parents=True, exist_ok=True)

        # 备份原文件
        if Path(knowledge_file).exists():
            backup_file = version_dir / Path(knowledge_file).name
            shutil.copy2(knowledge_file, backup_file)
            print(f"   备份到: {backup_file}")

        # 更新文件
        with open(knowledge_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        # 记录更新信息
        version_info = {
            "version_id": version_id,
            "knowledge_file": str(knowledge_file),
            "updater": updater,
            "update_notes": update_notes,
            "updated_at": datetime.now().isoformat(),
            "backup_file": str(backup_file) if Path(knowledge_file).exists() else None
        }

        # 保存版本信息
        version_info_file = version_dir / "version_info.json"
        with open(version_info_file, 'w', encoding='utf-8') as f:
            json.dump(version_info, f, ensure_ascii=False, indent=2)

        print(f"   版本ID: {version_id}")
        print(f"   更新者: {updater}")
        print(f"   更新说明: {update_notes}")

        return version_info

    def get_knowledge_versions(self, knowledge_file):
        """获取知识版本历史"""
        print(f"\n📜 知识版本历史: {knowledge_file}")

        versions = []

        # 遍历版本目录
        for version_dir in sorted(self.knowledge_versions.iterdir(), reverse=True):
            if version_dir.is_dir():
                version_info_file = version_dir / "version_info.json"

                if version_info_file.exists():
                    with open(version_info_file, 'r', encoding='utf-8') as f:
                        version_info = json.load(f)

                    if version_info["knowledge_file"] == str(knowledge_file):
                        versions.append(version_info)

        # 显示版本历史
        if versions:
            print(f"\n📊 共 {len(versions)} 个版本")

            for i, version in enumerate(versions, 1):
                print(f"\n{i}. 版本 {version['version_id']}")
                print(f"   更新者: {version['updater']}")
                print(f"   更新时间: {version['updated_at']}")
                print(f"   更新说明: {version['update_notes']}")
                print(f"   备份文件: {version['backup_file']}")
        else:
            print("⚠️ 没有找到版本历史")

        return versions

    def record_knowledge_usage(self, knowledge_file, user, usage_type, context):
        """记录知识使用"""
        print(f"📊 记录知识使用: {knowledge_file}")

        # 加载现有统计
        stats = {}
        if self.knowledge_stats.exists():
            with open(self.knowledge_stats, 'r', encoding='utf-8') as f:
                stats = json.load(f)

        # 添加使用记录
        usage_record = {
            "knowledge_file": str(knowledge_file),
            "user": user,
            "usage_type": usage_type,
            "context": context,
            "used_at": datetime.now().isoformat()
        }

        if "usage_records" not in stats:
            stats["usage_records"] = []

        stats["usage_records"].append(usage_record)

        # 更新统计
        if "usage_count" not in stats:
            stats["usage_count"] = {}

        key = str(knowledge_file)
        if key not in stats["usage_count"]:
            stats["usage_count"][key] = 0

        stats["usage_count"][key] += 1

        # 保存统计
        with open(self.knowledge_stats, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)

        print(f"   使用者: {user}")
        print(f"   使用类型: {usage_type}")
        print(f"   使用次数: {stats['usage_count'][key]}")

        return usage_record

    def show_usage_statistics(self):
        """显示使用统计"""
        print("\n" + "=" * 60)
        print("📊 知识使用统计")
        print("=" * 60)

        if not self.knowledge_stats.exists():
            print("❌ 没有使用统计")
            return

        with open(self.knowledge_stats, 'r', encoding='utf-8') as f:
            stats = json.load(f)

        # 总体统计
        total_usage = sum(stats.get("usage_count", {}).values())
        print(f"\n📊 总体统计:")
        print(f"   总使用次数: {total_usage}")

        # 按知识统计
        print(f"\n📁 知识使用排行:")
        usage_count = stats.get("usage_count", {})
        sorted_usage = sorted(usage_count.items(), key=lambda x: x[1], reverse=True)

        for i, (file_path, count) in enumerate(sorted_usage[:10], 1):
            file_name = Path(file_path).name
            print(f"   {i}. {file_name}: {count} 次")

        # 按用户统计
        print(f"\n👤 用户使用统计:")
        user_usage = defaultdict(int)

        for record in stats.get("usage_records", []):
            user_usage[record["user"]] += 1

        sorted_users = sorted(user_usage.items(), key=lambda x: x[1], reverse=True)

        for i, (user, count) in enumerate(sorted_users, 1):
            print(f"   {i}. {user}: {count} 次")

        # 按类型统计
        print(f"\n📋 使用类型统计:")
        type_usage = defaultdict(int)

        for record in stats.get("usage_records", []):
            type_usage[record["usage_type"]] += 1

        sorted_types = sorted(type_usage.items(), key=lambda x: x[1], reverse=True)

        for i, (usage_type, count) in enumerate(sorted_types, 1):
            print(f"   {i}. {usage_type}: {count} 次")

    def optimize_knowledge_structure(self):
        """优化知识结构"""
        print("\n" + "=" * 60)
        print("🔧 优化知识结构")
        print("=" * 60)

        # 检查分类
        categories = []
        for category_path in self.knowledge_base.iterdir():
            if category_path.is_dir():
                categories.append(category_path.name)

        print(f"\n📁 当前分类: {', '.join(categories)}")

        # 建议优化
        suggestions = []

        # 检查空分类
        for category in categories:
            category_path = self.knowledge_base / category
            files = list(category_path.glob("*.md"))
            if not files:
                suggestions.append(f"分类 '{category}' 为空，建议删除或添加知识")

        # 检查分类命名
        for category in categories:
            if category.startswith("_"):
                suggestions.append(f"分类 '{category}' 以下划线开头，建议重命名")

        # 检查知识文件命名
        for category_path in self.knowledge_base.iterdir():
            if category_path.is_dir():
                for file in category_path.glob("*.md"):
                    if file.name.startswith("20260420_"):
                        suggestions.append(f"文件 '{file.name}' 包含时间戳，建议重命名")

        # 显示建议
        if suggestions:
            print(f"\n💡 优化建议:")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"   {i}. {suggestion}")
        else:
            print("\n✅ 知识结构良好，无需优化")

        return suggestions

    def generate_knowledge_report(self):
        """生成知识报告"""
        print("\n" + "=" * 60)
        print("📊 知识体系报告")
        print("=" * 60)

        # 统计信息
        total_knowledge = 0
        by_category = defaultdict(int)
        by_agent = defaultdict(int)

        for category_path in self.knowledge_base.iterdir():
            if category_path.is_dir():
                category = category_path.name
                files = list(category_path.glob("*.md"))
                total_knowledge += len(files)
                by_category[category] = len(files)

                for file in files:
                    # 提取智能体信息
                    with open(file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        for agent_id, agent in self.agents.items():
                            if agent['name'] in content:
                                by_agent[agent_id] += 1
                                break

        # 显示统计
        print(f"\n📊 总体统计:")
        print(f"   总知识数: {total_knowledge}")
        print(f"   分类数: {len(by_category)}")
        print(f"   智能体数: {len(by_agent)}")

        print(f"\n📁 分类统计:")
        for category, count in sorted(by_category.items()):
            print(f"   {category}: {count} 个知识点")

        print(f"\n🤖 智能体贡献:")
        for agent_id, count in sorted(by_agent.items(), key=lambda x: x[1], reverse=True):
            agent = self.agents.get(agent_id, {})
            print(f"   {agent.get('name', agent_id)}: {count} 个知识点")

        # 显示使用统计
        self.show_usage_statistics()

        # 显示优化建议
        self.optimize_knowledge_structure()

        print(f"\n{'=' * 60}")
        print("✅ 知识报告生成完成")
        print(f"{'=' * 60}")

def main():
    """主函数"""
    workspace_root = os.path.expanduser("~/.openclaw/workspace")

    # 创建知识管理系统
    management_system = KnowledgeManagementSystem(workspace_root)

    # 生成知识报告
    management_system.generate_knowledge_report()

if __name__ == "__main__":
    main()
