import argparse
import os
import json
from pathlib import Path
from typing import Any, Dict, Union
import questionary
import shlex
from robot.run import RobotFramework
from lzstring import LZString
from urllib.parse import quote_plus
try:
    import pyperclip
except ImportError:
    pyperclip = None


def generate_project_link(project_dict: Dict[str, Any], directory: Path):
    files = [
        {
            "fileName": file.get("fileName"),
            "hidden": file.get("hidden", False),
            "content": (directory / file.get("fileName")).read_text(),
        }
        for file in project_dict["files"]
    ]
    project_dict["files"] = files
    project_json = json.dumps(project_dict)
    base64_encoded_data = LZString.compressToEncodedURIComponent(project_json)
    url = f"https://robotframework.org/embed/?codeProject={quote_plus(base64_encoded_data)}"
    if pyperclip:
        pyperclip.copy(url)
        print("URL copied to clipboard.")
    print(f"\n{url}")
    return url

def get_files(directory) -> list[Path]:
    return [
        f
        for f in Path(directory).rglob("*")
        if f.is_file() and f.name not in ["readme.md", "config.json"]
    ]


def get_hidden_files(files: list[Path]):
    hidden_files = questionary.checkbox(
        "Select files to hide:", choices=[f.name for f in files]
    ).ask()
    return [
        {"fileName": file.name, "hidden": file.name in hidden_files} for file in files
    ]


def main(directory: Union[str, Path]):
    directory = Path(directory)
    if not directory.is_dir():
        raise FileNotFoundError(f"Directory {directory} does not exist.")

    action = questionary.select(
        "What do you want to do?",
        choices=[
            "Create URL from config",
            "Create config for directory",
        ],
    ).ask()

    if action == "Create URL from config":
        # Call the function to create URL from config
        with (directory / "config.json").open() as f:
            project_dict = json.load(f)
            generate_project_link(project_dict, directory)
    elif action == "Create config for directory":

        name = questionary.text("Enter name:", default=directory.name).ask()
        robot_version = questionary.text("Enter robot version [optional]:").ask()
        req_answer = questionary.text(
            "Enter requirements (comma separated) [optional]:"
        ).ask()
        requirements = req_answer.split(",") if req_answer else []
        robot_args = questionary.text(
            "Enter robot arguments (space separated) [optional]:"
        ).ask()

        files_in_dir = get_files(directory)
        files = get_hidden_files(files_in_dir)
        splitted = shlex.split(robot_args)
        options, _ = RobotFramework().parse_arguments([*splitted, "."])

        config = {"name": name, "description": "readme.md", "files": files}
        if options:
            config["robotArgs"] = options
        if robot_version:
            config["robotVersion"] = robot_version
        if requirements:
            config["requirements"] = requirements

        with (directory / "config.json").open("w") as f:
            json.dump(config, f, indent=4)
            generate_project_link(config, directory)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate config.json")
    parser.add_argument("directory", nargs="?", default=os.getcwd())
    args = parser.parse_args()
    main(args.directory)
