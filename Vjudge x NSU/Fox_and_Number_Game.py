{"metadata":{"language_info":{"name":"python","version":"3.7.8","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"},"kernelspec":{"name":"python3","display_name":"Python 3","language":"python"}},"nbformat_minor":5,"nbformat":4,"cells":[{"cell_type":"code","source":"import math\n\nn = int(input())\n\narr = [int(x) for x in input().split()]\n\ngcd = math.gcd(arr[0], arr[1])\n\nfor i in range(2, n):\n    gcd = math.gcd(gcd, arr[i])\n\nres = n * gcd\n\nprint(res)","metadata":{"trusted":true},"execution_count":26,"outputs":[{"output_type":"stream","name":"stdin","text":" 5\n 45 12 27 30 18\n"},{"name":"stdout","text":"15\n","output_type":"stream"}],"id":"4fba9996-ac29-4e2d-a8e7-a5ee2fe39315"},{"cell_type":"code","source":"","metadata":{"trusted":true},"execution_count":14,"outputs":[{"execution_count":14,"output_type":"execute_result","data":{"text/plain":"2"},"metadata":{}}],"id":"3ceab1f9-0903-4d56-9e3d-923d1ee34036"},{"cell_type":"code","source":"for i in range(0,6):\n    print(i)","metadata":{"trusted":true},"execution_count":22,"outputs":[{"name":"stdout","text":"0\n1\n2\n3\n4\n5\n","output_type":"stream"}],"id":"8cb8f8b6-e001-4b26-a4ba-a4f95f24827e"},{"cell_type":"code","source":"","metadata":{},"execution_count":null,"outputs":[],"id":"71dc9220-1967-4507-a798-276d60e5f4b2"}]}