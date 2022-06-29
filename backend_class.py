from tracemalloc import start


class Backend:
    def aboveBelow(numbers: list, compVal: int) -> map:
        output = {
            "above": 0,
            "below": 0
        }

        # input is unsorted, can not avoid linear iteration
        for num in numbers:
            if num < compVal:
                output["below"] += 1
            elif num > compVal:
                output["above"] += 1

        return output 
    

    def stringRotation(original: str, rotationVal: int) -> str:
        originalLength = len(original)

        # No need to rotate a string of length 0 or 1
        if originalLength <= 1:
            return original

        # Example: MyString becomes MyStringMyString
        # This contains all possible rotations
        letters = original + original

        # Real shift amount is between 0 and the length of original
        rotAmountAdjusted = rotationVal % originalLength

        start_index = originalLength - rotAmountAdjusted
        end_index = start_index + originalLength
        
        return letters[start_index:end_index]