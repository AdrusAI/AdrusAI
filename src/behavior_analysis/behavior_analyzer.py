behavior_analyzer.py
class BehaviorAnalyzer:
    """
    A class for analyzing the behavior of AI agents.
    """

    def init(self, agent_id):
        """
        Initializes the behavior analyzer for a specific AI agent.

        :param agent_id: str, unique identifier for the AI agent.
        """
        self.agent_id = agent_id
        self.logs = []

    def log_activity(self, activity):
        """
        Logs an activity for the AI agent.

        :param activity: dict, a record of the activity (e.g., {'status': 'Completed', 'description': 'Task finished'}).
        """
        if not isinstance(activity, dict) or "status" not in activity:
            raise ValueError("Activity must be a dictionary containing at least a 'status' key.")
        self.logs.append(activity)

    def analyze_behavior(self):
        """
        Analyzes the behavior logs of the AI agent and identifies patterns.

        :return: dict, a summary of behavior analysis including efficiency and error count.
        """
        completed_tasks = len([log for log in self.logs if log.get("status") == "Completed"])
        error_tasks = len([log for log in self.logs if log.get("status") == "Error"])
        total_tasks = len(self.logs)

        efficiency = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

        return {
            "agent_id": self.agent_id,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "error_tasks": error_tasks,
            "efficiency": efficiency
        }
def generate_report(self):
        """
        Generates a human-readable report of the agent's behavior analysis.

        :return: str, a formatted report of the agent's performance.
        """
        analysis = self.analyze_behavior()
        report = (
            f"Behavior Analysis Report for Agent: {analysis['agent_id']}\n"
            f"----------------------------------------\n"
            f"Total Tasks: {analysis['total_tasks']}\n"
            f"Completed Tasks: {analysis['completed_tasks']}\n"
            f"Tasks with Errors: {analysis['error_tasks']}\n"
            f"Efficiency: {analysis['efficiency']:.2f}%\n"
        )
        return report
