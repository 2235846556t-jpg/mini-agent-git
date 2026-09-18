class WorkerAgent:
    def execute(self, plan: list[str]) -> None:
        print("\nWorker Agent 开始执行任务：")

        for index, step in enumerate(plan, start=1):
            print(f"执行步骤 {index}: {step}")