#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🐟 学习引擎 - 自我进化和知识管理
三层架构的核心层
"""

import json
from pathlib import Path
from datetime import datetime
import re
from typing import Dict, List, Optional, Any
from collections import defaultdict

# 配置
WORKSPACE_DIR = Path.home() / ".openclaw" / "workspace"
CORE_DIR = WORKSPACE_DIR / "core"
LEARNING_DIR = CORE_DIR / "learning_engine"
CONFIG_FILE = LEARNING_DIR / "learning_engine_config.json"
KNOWLEDGE_FILE = LEARNING_DIR / "knowledge_base.json"
LOG_DIR = Path.home() / ".openclaw" / "logs"
LOG_FILE = LOG_DIR / "learning_engine.log"

# 创建目录
LEARNING_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

class LearningEngine:
    """学习引擎 - 自我进化和知识管理"""

    def __init__(self):
        self.knowledge_base = {
            "trading": {
                "name": "交易知识",
                "topics": [],
                "progress": 0,
                "last_updated": None
            },
            "analysis": {
                "name": "分析知识",
                "topics": [],
                "progress": 0,
                "last_updated": None
            },
            "strategy": {
                "name": "策略知识",
                "topics": [],
                "progress": 0,
                "last_updated": None
            },
            "risk": {
                "name": "风险管理",
                "topics": [],
                "progress": 0,
                "last_updated": None
            },
            "psychology": {
                "name": "心理控制",
                "topics": [],
                "progress": 0,
                "last_updated": None
            }
        }

        self.learning_history = []
        self.improvements = []
        self.goals = []

    def log(self, message):
        """记录日志"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {message}\n"
        print(log_message.strip())
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_message)

    def extract_knowledge_from_modules(self) -> Dict[str, Any]:
        """从现有模块中提取知识"""
        self.log("🔍 从现有模块中提取知识...")

        extracted_knowledge = {
            "trading": [],
            "analysis": [],
            "strategy": [],
            "risk": [],
            "psychology": []
        }

        # 扫描工作空间中的Python文件
        workspace_files = list(WORKSPACE_DIR.glob("*.py"))

        for file_path in workspace_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 提取学习相关的内容
                if "学习" in content or "LEARNING" in content or "learn" in content.lower():
                    self.log(f"📖 发现学习内容: {file_path.name}")

                    # 提取知识点
                    knowledge_points = self._extract_knowledge_points(content)

                    # 分类知识点
                    for point in knowledge_points:
                        category = self._classify_knowledge(point)
                        if category in extracted_knowledge:
                            extracted_knowledge[category].append({
                                "source": file_path.name,
                                "content": point,
                                "timestamp": datetime.now().isoformat()
                            })

            except Exception as e:
                self.log(f"⚠️ 读取文件失败 {file_path.name}: {e}")

        return extracted_knowledge

    def _extract_knowledge_points(self, content: str) -> List[str]:
        """提取知识点"""
        points = []

        # 提取注释中的知识点
        comments = re.findall(r'#.*?(?:学习|掌握|了解|理解|学会).*', content)
        points.extend(comments)

        # 提取docstring中的知识点
        docstrings = re.findall(r'""".*?"""', content, re.DOTALL)
        points.extend(docstrings)

        # 提取函数名中的知识点
        function_names = re.findall(r'def\s+(\w+)', content)
        points.extend(function_names)

        return points

    def _classify_knowledge(self, knowledge_point: str) -> str:
        """分类知识点"""
        keywords = {
            "trading": ["交易", "买卖", "持仓", "止盈", "止损", "trading"],
            "analysis": ["分析", "指标", "K线", "均线", "技术", "基本面", "analysis"],
            "strategy": ["策略", "方法", "方案", "系统", "strategy"],
            "risk": ["风险", "控制", "管理", "仓位", "risk"],
            "psychology": ["心理", "情绪", "贪婪", "恐惧", "纪律", "psychology"]
        }

        for category, words in keywords.items():
            for word in words:
                if word in knowledge_point:
                    return category

        return "analysis"  # 默认分类

    def integrate_knowledge(self, extracted_knowledge: Dict[str, Any]):
        """整合知识"""
        self.log("🔄 整合知识...")

        for category, points in extracted_knowledge.items():
            if category in self.knowledge_base:
                # 去重
                existing_contents = {p['content'] for p in self.knowledge_base[category]['topics']}
                new_points = [p for p in points if p['content'] not in existing_contents]

                self.knowledge_base[category]['topics'].extend(new_points)
                self.knowledge_base[category]['last_updated'] = datetime.now().isoformat()

                # 计算进度
                total_topics = len(self.knowledge_base[category]['topics'])
                self.knowledge_base[category]['progress'] = min(100, total_topics * 5)  # 每个知识点5%

                self.log(f"✅ {self.knowledge_base[category]['name']}: +{len(new_points)} 个知识点")

    def set_learning_goal(self, goal: str, deadline: Optional[str] = None):
        """设置学习目标"""
        self.log(f"🎯 设置学习目标: {goal}")

        self.goals.append({
            "goal": goal,
            "deadline": deadline,
            "status": "in_progress",
            "created_at": datetime.now().isoformat()
        })

    def track_learning_progress(self) -> Dict[str, Any]:
        """跟踪学习进度"""
        progress_report = {
            "overall_progress": 0,
            "categories": {},
            "goals": self.goals,
            "recommendations": []
        }

        total_progress = 0
        category_count = len(self.knowledge_base)

        for category_id, category_data in self.knowledge_base.items():
            progress_report["categories"][category_id] = {
                "name": category_data["name"],
                "progress": category_data["progress"],
                "topics_count": len(category_data["topics"]),
                "last_updated": category_data["last_updated"]
            }
            total_progress += category_data["progress"]

        if category_count > 0:
            progress_report["overall_progress"] = total_progress / category_count

        # 生成学习建议
        progress_report["recommendations"] = self._generate_learning_recommendations()

        return progress_report

    def _generate_learning_recommendations(self) -> List[str]:
        """生成学习建议"""
        recommendations = []

        # 找出进度最低的类别
        sorted_categories = sorted(
            self.knowledge_base.items(),
            key=lambda x: x[1]['progress']
        )

        if sorted_categories:
            lowest_category = sorted_categories[0]
            recommendations.append(
                f"重点学习 {lowest_category[1]['name']}，当前进度: {lowest_category[1]['progress']}%"
            )

        # 检查未完成的目标
        for goal in self.goals:
            if goal['status'] == 'in_progress':
                recommendations.append(f"继续推进目标: {goal['goal']}")

        return recommendations

    def record_improvement(self, improvement: str, impact: str):
        """记录改进"""
        self.log(f"📈 记录改进: {improvement}")

        self.improvements.append({
            "improvement": improvement,
            "impact": impact,
            "timestamp": datetime.now().isoformat()
        })

    def get_improvements(self) -> List[Dict]:
        """获取改进记录"""
        return sorted(self.improvements, key=lambda x: x['timestamp'], reverse=True)

    def generate_learning_plan(self) -> str:
        """生成学习计划"""
        plan = []
        plan.append("=" * 80)
        plan.append("🐟 学习引擎 - 学习计划")
        plan.append("=" * 80)
        plan.append(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        plan.append("")

        # 总体进度
        progress = self.track_learning_progress()
        plan.append(f"📊 总体进度: {progress['overall_progress']:.1f}%")
        plan.append("")

        # 各类别进度
        plan.append("📚 知识类别:")
        for category_id, category_data in progress['categories'].items():
            progress_bar = self._generate_progress_bar(category_data['progress'])
            plan.append(f"  {progress_bar} {category_data['name']}: {category_data['progress']:.1f}% ({category_data['topics_count']} 个知识点)")

        plan.append("")

        # 学习目标
        plan.append("🎯 学习目标:")
        if self.goals:
            for goal in self.goals:
                status_icon = "✅" if goal['status'] == 'completed' else "🔄"
                plan.append(f"  {status_icon} {goal['goal']}")
                if goal['deadline']:
                    plan.append(f"     截止: {goal['deadline']}")
        else:
            plan.append("  无")

        plan.append("")

        # 学习建议
        plan.append("💡 学习建议:")
        for recommendation in progress['recommendations']:
            plan.append(f"  • {recommendation}")

        plan.append("")

        # 最近改进
        plan.append("📈 最近改进:")
        recent_improvements = self.get_improvements()[:5]
        if recent_improvements:
            for improvement in recent_improvements:
                plan.append(f"  • {improvement['improvement']}")
                plan.append(f"    影响: {improvement['impact']}")
        else:
            plan.append("  无")

        plan.append("")
        plan.append("=" * 80)

        return "\n".join(plan)

    def _generate_progress_bar(self, progress: float, width: 20) -> str:
        """生成进度条"""
        filled = int(width * progress / 100)
        bar = "█" * filled + "░" * (width - filled)
        return f"[{bar}]"

    def save_knowledge_base(self):
        """保存知识库"""
        with open(KNOWLEDGE_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge_base, f, ensure_ascii=False, indent=2)

        self.log(f"✅ 知识库已保存到: {KNOWLEDGE_FILE}")

    def load_knowledge_base(self):
        """加载知识库"""
        if KNOWLEDGE_FILE.exists():
            with open(KNOWLEDGE_FILE, 'r', encoding='utf-8') as f:
                self.knowledge_base = json.load(f)

            self.log(f"✅ 知识库已从 {KNOWLEDGE_FILE} 加载")
            return True
        return False

    def save_config(self):
        """保存配置"""
        config = {
            'knowledge_base': self.knowledge_base,
            'learning_history': self.learning_history,
            'improvements': self.improvements,
            'goals': self.goals,
            'last_updated': datetime.now().isoformat()
        }

        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

        self.log(f"✅ 配置已保存到: {CONFIG_FILE}")

    def load_config(self):
        """加载配置"""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)

            self.knowledge_base = config.get('knowledge_base', self.knowledge_base)
            self.learning_history = config.get('learning_history', [])
            self.improvements = config.get('improvements', [])
            self.goals = config.get('goals', [])

            self.log(f"✅ 配置已从 {CONFIG_FILE} 加载")
            return True
        return False

def main():
    """主函数"""
    print("=" * 80)
    print("🐟 学习引擎 - 自我进化和知识管理")
    print("=" * 80)

    engine = LearningEngine()

    # 加载配置
    engine.load_config()
    engine.load_knowledge_base()

    # 提取知识
    extracted_knowledge = engine.extract_knowledge_from_modules()

    # 整合知识
    engine.integrate_knowledge(extracted_knowledge)

    # 生成学习计划
    print(engine.generate_learning_plan())

    # 保存配置
    engine.save_config()
    engine.save_knowledge_base()

    print("\n" + "=" * 80)
    print("✅ 学习引擎初始化完成")
    print("=" * 80)
    print("\n📝 可用命令:")
    print("  - extract_knowledge_from_modules(): 从模块提取知识")
    print("  - integrate_knowledge(extracted_knowledge): 整合知识")
    print("  - set_learning_goal(goal, deadline): 设置学习目标")
    print("  - track_learning_progress(): 跟踪学习进度")
    print("  - record_improvement(improvement, impact): 记录改进")
    print("  - generate_learning_plan(): 生成学习计划")
    print("\n📝 配置文件:")
    print(f"  - {CONFIG_FILE}")
    print(f"  - {KNOWLEDGE_FILE}")
    print("\n📝 日志文件:")
    print(f"  - {LOG_FILE}")
    print()

if __name__ == "__main__":
    main()
