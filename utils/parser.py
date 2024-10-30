import argparse


parser = argparse.ArgumentParser(
    description="create template for new task"
)

parser.add_argument(
    "--task-id",
    type=str,
    help="unique id for task folder",
)
