from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test():
    working = "calculator"

    # -- get_files_info
    info_tests = [
        ".",
        "pkg",
        "/bin",
        "../",
        None,
    ]
    # for t in info_tests:
    #     print(get_files_info(working, t))
    #     print()

    # -- get_file_content
    content_tests = [
        "main.py",
        "pkg/calculator.py",
        "/bin/cat",
        "lorem.txt",
    ]
    # for t in content_tests:
    #     print(get_file_content(working, t))
    #     print()

    # -- write_file
    write_tests = [
        ("lorem.txt", "wait, this isn't lorem ipsum"),
        ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("/tmp/temp.txt", "this should not be allowed"),
        ("pkg", "this should not be allowed"),
    ]
    # for t in write_tests:
    #     print(write_file(working, t[0], t[1]))
    #     print()

    # # -- run_python_file
    run_tests = [
        "main.py",
        "tests.py",
        "../main.py",
        "nonexistent.py",
    ]
    for t in run_tests:
        print(run_python_file(working, t))
        print()


if __name__ == "__main__":
    test()