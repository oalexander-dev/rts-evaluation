from backend_class import Backend

# Basic test case with 4 positive nums above and below the compVal
def test_above_below_1():
    numbers = [0, 1, 2, 3, 5, 6, 7, 8]
    compVal = 4
    result = Backend.aboveBelow(numbers, compVal)
    assert(result["above"] == 4)
    assert(result["below"] == 4)

# Basic test case with some negative nums and zero
def test_above_below_2():
    numbers = [-3, -1, 0, 3, 5, 7, 8, 9]
    compVal = 6
    result = Backend.aboveBelow(numbers, compVal)
    assert(result["above"] == 3)
    assert(result["below"] == 5)

# Basic test case with some duplicate entries all lower than compVal
def test_above_below_3():
    numbers = [1, 1, 1, 2, 3, 4, 5, 5]
    compVal = 6
    result = Backend.aboveBelow(numbers, compVal)
    assert(result["above"] == 0)
    assert(result["below"] == 8)

# Edge test case with just the compVal in input
def test_above_below_4():
    numbers = [6, 6, 6, 6, 6, 6, 6]
    compVal = 6
    result = Backend.aboveBelow(numbers, compVal)
    assert(result["above"] == 0)
    assert(result["below"] == 0)

# Edge test case with no input
def test_above_below_5():
    numbers = []
    compVal = 6
    result = Backend.aboveBelow(numbers, compVal)
    assert(result["above"] == 0)
    assert(result["below"] == 0)

# Basic test case
def test_string_rotation_1():
    inputStr = "TestMessage"
    rotVal = 2
    result = Backend.stringRotation(inputStr, rotVal)
    assert(result == "geTestMessa")

# Basic test case with exactly a full rotation
def test_string_rotation_2():
    inputStr = "TestMessage"
    rotVal = 11
    result = Backend.stringRotation(inputStr, rotVal)
    assert(result == "TestMessage")

# Basic test case with more than a full rotation
def test_string_rotation_3():
    inputStr = "TestMessage"
    rotVal = 14
    result = Backend.stringRotation(inputStr, rotVal)
    assert(result == "ageTestMess")

# Edge test case with empty input
def test_string_rotation_4():
    inputStr = ""
    rotVal = 14
    result = Backend.stringRotation(inputStr, rotVal)
    assert(result == "")

# Edge test case with one char input
def test_string_rotation_5():
    inputStr = "T"
    rotVal = 14
    result = Backend.stringRotation(inputStr, rotVal)
    assert(result == "T")