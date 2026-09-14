from agents.planner import PlannerAgent


def main():
    task = input("请输入任务: ")

    planner = PlannerAgent()
    plan = planner.plan(task)

    print("\nPlanner Agent 生成的计划：")

    for index, step in enumerate(plan, start=1):
        print(f"{index}. {step}")


if __name__ == "__main__":
    main()