class WorkerAgent:
    def execute(self, plan: list[str]) -> list[str]:
        if not plan:
            return []

        results = []

        for index, step in enumerate(plan, start=1):
            results.append(f"执行步骤 {index}: {step}")

        return results
