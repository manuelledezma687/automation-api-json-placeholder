import pytest
from _pytest.nodes import Item


def validate_only_run_env(item: Item):
    for mark in item.iter_markers(name="only_run_env"):
        env_name = mark.args[0]
        if item.config.getoption("--env") != env_name:
            if not len(mark.args) > 1:
                reason = "Not setting reason"
            else:
                reason = mark.args[1]
            pytest.skip(f"test requires environment {env_name} - Reason: {reason}")


def validate_skip_env(item: Item):
    for mark in item.iter_markers(name="skip_env"):
        env_name = mark.args[0]
        if item.config.getoption("--env") == env_name:
            if not len(mark.args) > 1:
                reason = "Not setting reason"
            else:
                reason = mark.args[1]
            pytest.skip(f"test not run in environment {env_name} - Reason: {reason}")


def validate_skip_device(item: Item):
    for mark in item.iter_markers(name="skip_device"):
        device_name = mark.args[0]
        if item.config.getoption("--device") == device_name:
            if not len(mark.args) > 1:
                reason = "Not setting reason"
            else:
                reason = mark.args[1]
            pytest.skip(f"test not run in environment {device_name} - Reason: {reason}")
