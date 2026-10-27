import inspect
import json
import math
from datetime import datetime

__all__ = ["log_event", "log_state"]

_FPS = 60
_MAX_SECONDS = 16

_frame_count = 0                          # Will count the cycles of the main program cycle from the start
_state_log_initialized = False            # Denotes if the state log file was already created or not.
                                          # After creation if will be set True
_event_log_initialized = False            # Denotes if the state log file was already created or not.
_start_time = datetime.now()

def log_state() -> None:
    global _frame_count, _state_log_initialized

    print("logged state")
    if _frame_count > _FPS * _MAX_SECONDS:     # Stop logging after `_MAX_SECONDS` seconds. Later it might be modified
        return

    # Take a snapshot approx. once per second
    _frame_count += 1
    if _frame_count % _FPS != 0:
        return

    now = datetime.now()

    frame = inspect.currentframe()              # Frame, in this context mean the Python's actual execution stack from which
                                                # actual variable values may be taken
    if frame is None:
        return

    frame_back = frame.f_back
    if frame_back is None:
        return

    local_vars = frame_back.f_locals.copy()     # A copy of the actual variables. It is probably a dict[str, Any]

    screen_size: list[int] = []
    game_state: dict[str, object] = {}

    for key, value in local_vars.items():       # Traverses all local variables but currently writes log entries only for the screen size
        if "pygame" in str(type(value)) and hasattr(value, "get_size"):
            screen_size = list(value.get_size())

    entry: dict[str, object] = {
        "timestamp": now.strftime("%H:%M:%S.%f")[:-3],
        "elapsed_s": math.floor((now - _start_time).total_seconds()),
        "frame": _frame_count,
        "screen_size": screen_size,
        **game_state,
    }

    # New log file on each run
    mode = "w" if not _state_log_initialized else "a"
    with open("game_state.jsonl", mode) as f:
        _ = f.write(json.dumps(entry) + "\n")
    _state_log_initialized = True

def log_event(event_type: str, **details: object) -> None:
    global _event_log_initialized

    now = datetime.now()

    event: dict[str, object] = {
        "timestamp": now.strftime("%H:%M:%S.%f")[:-3],
        "elapsed_s": math.floor((now - _start_time).total_seconds()),
        "frame": _frame_count,
        "type": event_type,
        **details,
    }

    mode = "w" if not _event_log_initialized else "a"
    with open("game_events.jsonl", mode) as f:
        _ = f.write(json.dumps(event) + "\n")
    _event_log_initialized = True
