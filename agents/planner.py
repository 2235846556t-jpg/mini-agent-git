class PlannerAgent:
    def plan(self, task: str) -> list[str]:
        return [
            f"分析任务：{task}",
            "制定执行步骤",
            "交给 Worker Agent 执行",
        ]