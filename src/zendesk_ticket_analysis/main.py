#!/usr/bin/env python
import sys

from zendesk_ticket_analysis.crew import ZendeskTicketAnalysisCrew


def run():
    """
    Run the crew to fetch Zendesk tickets and generate a summary.
    """
    inputs = {
        "user_query": "How many tickets come from Jan 2024 and how many come from Mar 2025?",
    }

    # Kicking off the crew
    result = ZendeskTicketAnalysisCrew().crew().kickoff(inputs=inputs)

    # Save the summary result as a Markdown file
    with open("ticket_summary.md", "w") as f:
        f.write(result.raw)


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        ZendeskTicketAnalysisCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2]
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ZendeskTicketAnalysisCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """
    try:
        ZendeskTicketAnalysisCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2]
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
