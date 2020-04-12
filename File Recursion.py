import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    global results
    if os.path.isfile(path):
        if path.endswith(suffix):
            results.append(path)
    elif os.path.isdir(path):
        for sub in os.listdir(path):
            if os.path.exists(os.path.join(path, sub)):
                pass
            else:
                continue
            find_files(suffix, os.path.join(path, sub))
    else:
        pass
    return results


if __name__ == "__main__":
    print("Test Case 1")
    PATH = "./testdir/"
    SUFFIX = ".c"
    results = []
    results = find_files(SUFFIX, PATH)
    print(results) # Expected console output: ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
    print("Test Case 2")
    SUFFIX = ".h"
    results = []
    results = find_files(SUFFIX, PATH)
    print(results) # Expected console output: ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']
    print("Test Case 3")
    SUFFIX = ".py"
    results = []
    results = find_files(SUFFIX, PATH)
    print(results) # Expected console output: [], since *.py file are not found