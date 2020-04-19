# ------------  KATA DESCRIPTION ------------
"""
6 kyu
Array to HTML table

Overview

The task is simple - given a 2D array (list), generate an HTML table representing the data from this array.

You need to write a function called to_table/toTable, that takes three arguments:

    data - a 2D array (list),
    headers - an optional boolean value. If True, the first row of the array is considered a header (see below). Defaults to False,
    index - an optional boolean value. If True, the first column in the table should contain 1-based indices of the corresponding row. If headers arguments is True, this column should have an empty header. Defaults to False.

and returns a string containing HTML tags representing the table.
Details
HTML table is structured like this:

<table>
  <thead>                 <!-- an optional table header -->
    <tr>                  <!-- a header row -->
      <th>header1</th>    <!-- a single header cell -->
      <th>header2</th>
    </tr>
  </thead>
  <tbody>                 <!-- a table's body -->
    <tr>                  <!-- a table's row -->
      <td>row1, col1</td> <!-- a row's cell -->
      <td>row1, col2</td>
    </tr>
    <tr>
      <td>row2, col1</td>
      <td>row2, col2</td>
    </tr>
  </tbody>
</table>

The table header is optional. If header argument is False then the table starts with <tbody> tag, ommiting <thead>.

So, for example:

to_table([["lorem", "ipsum"], ["dolor", "sit amet"]], True, True)

returns

"<table><thead><tr><th></th><th>lorem</th><th>ipsum</th></tr></thead><tbody><tr><td>1</td><td>dolor</td><td>sit amet</td></tr></tbody></table>"

As you can see, no linebreaks or whitespaces (except for the ones present in the array values) are included, so the HTML code is minified.

IMPORTANT NOTE: if the value in the array happens to be None, the value of the according cell in the table should be en ampty string ("")! Otherwise, just use a string representation of the given value, so, dependent on the language, the output can be slightly different. No additional parsing is needed on the data.
Additional info

For your convenience, there is a preloaded function esc_html/escHtml that takes a string with HTML tags and escape them; it is necessary if you want to use print/console.log on your resulting strings, elsewise Codewars processes HTML tags, so they appear invisible in the stdout.

Test cases will always provide valid data, that is - up to three arguments, first a NxM array (list) with N and M > 0, second and third a boolean. The values in the array will always be either string, number, bool or None/null.

For more examples, see test cases.

P.S.: I understand, that with larger inputs checking for mismatches in the expected and actual output can be cumbersome, but as of now I can hardly come up with something that would make this easier. Any ideas would be helpful!
"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def to_table(data, header=False, index=False):

    html = "<table>"

    if header:
        html += "<thead><tr>"
        if index:
            html += "<th></th>"
        for h in data[0]:
            html += f"<th>{str(h)}</th>"
        html += "</tr></thead>"

        data = data[1:]

    html += "<tbody>"
    for i, row in enumerate(data, 1):
        html += "<tr>"

        if index:
            html += f"<td>{i}</td>"
        for c in row:
            html += f"<td>{str(c) if c is not None else ''}</td>"

        html += "</tr>"

    html += "</tbody></table>"

    return html


# ---------------  TEST CASES ---------------
cases = iter([
    {
        "input": ([["o"]]),
        "output": "<table><tbody><tr><td>o</td></tr></tbody></table>"
    },
    {
        "input": ([["lorem", "ipsum"], ["dolor", "sit amet"]], True, True),
        "output": "<table><thead><tr><th></th><th>lorem</th><th>ipsum</th></tr></thead><tbody><tr><td>1</td><td>dolor</td><td>sit amet</td></tr></tbody></table>"
    },
    {
        "input": ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], False, True),
        "output": "<table><tbody><tr><td>1</td><td>1</td><td>2</td><td>3</td></tr><tr><td>2</td><td>4</td><td>5</td><td>6</td></tr><tr><td>3</td><td>7</td><td>8</td><td>9</td></tr></tbody></table>"
    },
    {
        "input": (
            [
                ["id", "name", "price", "quantity"],
                [24351, "pen", 2.41, 500],
                [None, "pencil", 0.99, 25],
                [63401, "grizzly bear", None, 1],
                [3532, "rubber duck", 5.45, 24],
                [1523, None, 3.00, 6.8],
                [11765, "caviar", 67.95, None]
            ], True),
        "output": "<table><thead><tr><th>id</th><th>name</th><th>price</th><th>quantity</th></tr></thead><tbody><tr><td>24351</td><td>pen</td><td>2.41</td><td>500</td></tr><tr><td></td><td>pencil</td><td>0.99</td><td>25</td></tr><tr><td>63401</td><td>grizzly bear</td><td></td><td>1</td></tr><tr><td>3532</td><td>rubber duck</td><td>5.45</td><td>24</td></tr><tr><td>1523</td><td></td><td>3.0</td><td>6.8</td></tr><tr><td>11765</td><td>caviar</td><td>67.95</td><td></td></tr></tbody></table>"
    },
    {
        "input": ([["a", "b", "c", "d", "e"], [True, False, False, True, True]], True),
        "output": "<table><thead><tr><th>a</th><th>b</th><th>c</th><th>d</th><th>e</th></tr></thead><tbody><tr><td>True</td><td>False</td><td>False</td><td>True</td><td>True</td></tr></tbody></table>"
    },
])

@test.describe("Sample tests")
def sample():
    for case in cases:
        expected = case["output"]
        actual = to_table(*case["input"])
        test.assert_equals(actual, expected)