from main import get_new_levels

run_cases = [
    ([("Yuji", 75), ("Megumi", 48), ("Nobara", 60)], 150, [("Yuji", 225), ("Nobara", 180)]),
    ([], 150, []),
]

submit_cases = run_cases + [
    ([("Sukuna", 99)], 200, [("Sukuna", 297)]),
    ([("Mai", 30), ("Momo", 25)], 100, []),
    ([("Maki", 51), ("Yuta", 52), ("Panda", 40)], 150, [("Maki", 153), ("Yuta", 156)]),
    ([("Nanami", 50), ("Choso", 49)], 150, [("Nanami", 150)]),
    ([("Kashimo", 90), ("Hakari", 80)], 150, [("Kashimo", 270), ("Hakari", 240)]),
    ([("Higuruma", 70), ("Todo", 65), ("Yuki", 95)], 150, [("Higuruma", 210), ("Todo", 195), ("Yuki", 285)]),
]


def test(heroes, min_level, expected_output):
    print("---------------------------------")
    print(f"Inputs: heroes={heroes}, min_level={min_level}")
    result = get_new_levels(heroes, min_level)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
