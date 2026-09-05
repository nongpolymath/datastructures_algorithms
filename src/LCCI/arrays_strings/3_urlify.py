#URLify
# Write a method to replace all spaces in a string with '%20' . You may assume that the string has sufficient space at the end
# to hold additional characters and that you are given the 'true' length of the string.

def urlify(s: str , true_length: int) -> str:
    space_count = 0
    for i in range(true_length):
        if s[i] == " ":
            space_count += 1
    # write index
    w_ind = true_length + 2 * space_count - 1
    # r_ind -> read index
    for r_ind in range(true_length-1, -1, -1):
        if s[r_ind] == " ":
            s[w_ind-2: w_ind+1] = ["%" , "2", "0"]
            w_ind -= 3

        else:
            s[w_ind] = s[r_ind]
            w_ind -= 1
    return s


# test harness
if __name__ == "__main__":
    tests = [
        ("Mr John Smith", 13, "Mr%20John%20Smith"),
        ("abc", 3, "abc"),
        (" ", 1, "%20"),
        ("a  b", 4, "a%20%20b"),
        ("", 0, ""),
    ]

    for content, true_length, expected in tests:
        space_count = content[:true_length].count(" ")
        buf = list(content[:true_length]) + [" "] * (space_count * 2)
        result = "".join(urlify(buf, true_length))
        status = "OK" if result == expected else "FAIL"
        print(f"{content!r:20} -> {result!r:25} [{status}]")