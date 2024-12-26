def compress_string(s):
    """
    Compresses a given string by counting consecutive occurrences of characters.

    Args:
        s: The input string to be compressed.

    Returns:
        The compressed string.
    """

    compressed = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1

    compressed += s[-1] + str(count)  # Add the last character and its count

    return compressed

# Get input from the user
input_string = input("Enter a string: ")

# Compress the string
compressed_string = compress_string(input_string)

# Print the compressed string
print("Compressed string:",compressed_string)