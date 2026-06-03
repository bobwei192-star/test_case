"""GitLab Example — 用于演示 GitLab MR/PR 工作流的示例模块。"""


def add(a: int, b: int) -> int:
    """返回两数之和。"""
    return a + b


def subtract(a: int, b: int) -> int:
    """返回两数之差。"""
    return a - b


def multiply(a: int, b: int) -> int:
    """返回两数之积。"""
    return a * b


def divide(a: int, b: int) -> float:
    """返回两数之商。"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b
