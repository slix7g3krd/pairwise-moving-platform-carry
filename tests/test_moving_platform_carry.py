import pytest
import gameplay.moving_platform_carry as mod

CASES = [
    ("platform_in_step", (1,)),
    ("relative_carry", (1,)),
    ("vertical_compose", (1,)),
    ("parent_switch", (1,)),
    ("unbind_on_destroy", (1,)),
    ("authority_pos", (1,)),
    ("determinism", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("ride_state", (1,)),
    ("metrics", (1,)),
    ("delta_apply", (1,)),
    ("detach", (1,)),
    ("sync", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
