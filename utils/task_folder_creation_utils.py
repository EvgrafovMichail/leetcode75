import os

from pathlib import PureWindowsPath


class TemplateCreator:
    PATH_TO_TASKS_FOLDER: str = "tasks"
    PATH_TO_README: str = "README.md"

    @staticmethod
    def create(task_id: str) -> None:
        path_to_task_folder = os.path.join(
            TemplateCreator.PATH_TO_TASKS_FOLDER, task_id
        )

        if os.path.exists(path_to_task_folder):
            raise Exception

        os.makedirs(path_to_task_folder)
        TemplateCreator._create_files(task_id, path_to_task_folder)
        TemplateCreator._update_readme(task_id, path_to_task_folder)

    @staticmethod
    def _create_files(task_id: str, path_to_folder: str) -> None:
        path_to_script = os.path.join(path_to_folder, f"{task_id}.py")
        indent = " " * 4
        script_content = (
            f"class Solution:\n{indent}pass\n\n\n"
            f"if __name__ == \"__main__\":\n{indent}pass\n"
        )

        with open(path_to_script, "w") as file:
            file.write(script_content)

        path_to_readme = os.path.join(path_to_folder, "README.md")
        readme_content = f"# {task_id}\n"

        with open(path_to_readme, "w") as file:
            file.write(readme_content)

    @staticmethod
    def _update_readme(task_id: str, path_to_folder) -> None:
        if os.path.sep == "\\":
            path_normalized = os.path.normpath(path_to_folder)
            path_to_folder = PureWindowsPath(path_normalized).as_posix()

        content_to_add = f"- [{task_id}]({path_to_folder});\n"

        with open(TemplateCreator.PATH_TO_README, "a") as file:
            file.write(content_to_add)
