from agents.planner import PlannerAgent
from agents.worker import WorkerAgent


def main():
    task = input("🤖 Mini Agent > 请输入需要 Agent 完成的任务: ")

    planner = PlannerAgent()
    plan = planner.plan(task)

    print("\nPlanner Agent 生成的计划：")

    for index, step in enumerate(plan, start=1):
        print(f"{index}. {step}")

    worker = WorkerAgent()
    results = worker.execute(plan)

    print("\nWorker Agent 开始执行任务：")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
    