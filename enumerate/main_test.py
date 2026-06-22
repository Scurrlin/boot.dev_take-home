from main import numbered_inventory

run_cases = [
    (["Lute", "Flute", "Harp"], ["1. Lute", "2. Flute", "3. Harp"]),
    ([], []),
]

submit_cases = run_cases + [
    (["Drums"], ["1. Drums"]),
    (
        ["Guitar", "Piano", "Violin", "Cello", "Bass"],
        ["1. Guitar", "2. Piano", "3. Violin", "4. Cello", "5. Bass"],
    ),
    (["Euphonium", "Piccolo"], ["1. Euphonium", "2. Piccolo"]),
    (
        ["Clarinet", "Flute", "Oboe", "Bassoon"],
        ["1. Clarinet", "2. Flute", "3. Oboe", "4. Bassoon"],
    ),
    (["Stylophone"], ["1. Stylophone"]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = numbered_inventory(input1)
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
