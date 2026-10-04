class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    for key in ("dataset", "trainer", "evaluator"):
        if not body.get(key): failed.append(f"missing_{key}")
    return {"passed": not failed, "failed": failed, "applied": False}
